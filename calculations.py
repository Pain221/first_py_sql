import pandas as pd
import psycopg2 as pc2

tariff_data={'service':['HVS', 'GVS', 'EE','EE_daytime', 'EE_night','GVS_heat_carrier', 'GVS_thermal_energy' ],
             'tariff(rub/unit_of_measurement)':[35.78, 158.98, 4.28, 4.9, 2.31, 35.78, 998.69],
             'standard':[4.85, 4.01, 164, '-', '-', 4.01, 0.05349],
             'units_of_measurement':['m^3', 'm^3', 'kW/h','kW/h', 'kW/h','m^3','Gcal']
             }
standard_frame=pd.DataFrame(tariff_data)

conn=pc2.connect("dbname=komunalka user=postgres password=123 port=5432")
cursor=conn.cursor()

#создает в базе запись с номером ЛС и датой
def database_record_accrual(number_LS,request_date):
    cursor.execute("""INSERT INTO Accruals (number_ls, accrual_date) VALUES (%s, %s);""",(number_LS, request_date))

#определяет какие функции выполнять
def Execute_calculations(HVS_device, indications_HVS, GVS_device,indications_GVS, number_of_residents, number_LS,request_date):
    if HVS_device == 'НЕТ':
        HVS_without_device(number_of_residents, number_LS, request_date)
    if HVS_device == 'ДА':
        HVS_with_device(number_LS, request_date, indications_HVS)
    if GVS_device=='НЕТ':
        GVS_heat_carrier_without_device(number_LS, request_date, number_of_residents)
    if GVS_device == 'ДА':
        GVS_heat_carrier_with_device(number_LS, request_date,indications_GVS)
    GVS_thermal_energy(number_LS, request_date, number_of_residents, volume_of_consumption_GVS_heat_carrier)

#начисления за ХВС без счётчика
def HVS_without_device(number_of_residents, number_LS, request_date):
    volume_of_consumption=number_of_residents*standard_frame['standard'][0]
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][0] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_hvs=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual, number_LS, request_date))
        conn.commit()
        print('Начисления за ХВС вычислены:', accrual, 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)

#начисления за ХВС со счётчиком
def HVS_with_device(number_LS, request_date, indications_HVS):
    volume_of_consumption=indications_HVS
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][0] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_hvs=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual, number_LS, request_date))
        conn.commit()
        print('Начисления за ХВС вычислены:', accrual, 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)

#начисления за ГВС Теплоноситель без счетчика
def GVS_heat_carrier_without_device(number_LS, request_date, number_of_residents):
    global volume_of_consumption_GVS_heat_carrier
    volume_of_consumption_GVS_heat_carrier =number_of_residents*standard_frame['standard'][1] #accrual - начисление
    accrual=volume_of_consumption_GVS_heat_carrier*standard_frame['tariff(rub/unit_of_measurement)'][1]
    try:
        cursor.execute("""UPDATE Accruals SET accrual_gvs_heat_carrier=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual, number_LS, request_date))
        conn.commit()
        print('Начисления за ГВС Теплоноситель вычислены:', accrual, 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 

#начисления за ГВС Теплоноситель со счётчиком
def GVS_heat_carrier_with_device(number_LS, request_date,indications_GVS):
    global volume_of_consumption_GVS_heat_carrier #
    volume_of_consumption_GVS_heat_carrier = indications_GVS
    accrual=volume_of_consumption_GVS_heat_carrier*standard_frame['tariff(rub/unit_of_measurement)'][1]
    try:
        cursor.execute("""UPDATE Accruals SET accrual_gvs_heat_carrier=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual, number_LS, request_date))
        conn.commit()
        print('Начисления за ГВС Теплоноситель вычислены:', accrual, 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 


#начисления за ГВС Тепловая энергия
def GVS_thermal_energy(number_LS, request_date, number_of_residents, volume_of_consumption_GVS_heat_carrier):
    volume_of_consumption=volume_of_consumption_GVS_heat_carrier*standard_frame['standard'][6]
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][6] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_gvs_thermal_energy=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual, number_LS, request_date))
        conn.commit()
        print('Начисления за ГВС Тепловая энергия вычислены:', accrual, 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 

#начисления за Электроэнергию без счетчика
def EE_without_device(number_LS, request_date, number_of_residents):
    volume_of_consumption=number_of_residents*standard_frame['standard'][2]
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][2] #accrual - начисление
    #добавить внос начисления в базу 

#главная функция для main
def activate_calculations():
    from prototype import number_of_residents, HVS_device, number_LS, request_date, GVS_device, indications_HVS, indications_GVS
    database_record_accrual(number_LS,request_date)
    Execute_calculations(HVS_device, indications_HVS, GVS_device, indications_GVS, number_of_residents, number_LS,request_date)
