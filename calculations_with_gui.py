import pandas as pd
import psycopg2 as pc2

tariff_data={'service':['HVS', 'GVS', 'EE','EE_daytime', 'EE_night','GVS_heat_carrier', 'GVS_thermal_energy' ],
             'tariff(rub/unit_of_measurement)':[35.78, 158.98, 4.28, 4.9, 2.31, 35.78, 998.69],
             'standard':[4.85, 4.01, 164, '-', '-', 4.01, 0.05349],
             'units_of_measurement':['м. куб', 'м. куб', 'кВт.ч','кВт.ч', 'кВт.ч','м. куб','Гкал']
             }
standard_frame = pd.DataFrame(tariff_data)

conn = pc2.connect("dbname=komunalka user=postgres password=123 port=5432")
cursor = conn.cursor()

#создает в базе запись с номером ЛС и датой
def database_record_accrual(number_LS,request_date):
    cursor.execute("""INSERT INTO Accruals (number_ls, accrual_date) VALUES (%s, %s);""",(number_LS, request_date))

#определяет какие функции выполнять
def Execute_calculations(HVS_device, GVS_device, EE_device, number_of_residents, number_LS,request_date):
    if HVS_device == 2:
        HVS_without_device(number_of_residents, number_LS, request_date)
    elif HVS_device == 1:
        HVS_with_device(number_LS, request_date)
    if GVS_device==2:
        GVS_heat_carrier_without_device(number_LS, request_date, number_of_residents)
    elif GVS_device == 1:
        GVS_heat_carrier_with_device(number_LS, request_date)
    GVS_thermal_energy(number_LS, request_date,  volume_of_consumption_GVS_heat_carrier)
    Total_GVS(number_LS, request_date, accrual_GVS_thermal_energy,accrual_GVS_heat_carrier)
    if EE_device == 2:
        EE_without_device(number_LS, request_date, number_of_residents)
    elif EE_device == 1:
        EE_with_device(number_LS, request_date)
    Total_accrual(number_LS,request_date)

#начисления за ХВС без счётчика
def HVS_without_device(number_of_residents, number_LS, request_date):
    global accrual_HVS, volume_of_consumption_HVS
    volume_of_consumption_HVS = number_of_residents * standard_frame['standard'][0]
    accrual_HVS = volume_of_consumption_HVS * standard_frame['tariff(rub/unit_of_measurement)'][0] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_hvs=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_HVS, number_LS, request_date))
        conn.commit()
        print('Начисления за ХВС вычислены:', ("{:8.2f}".format(accrual_HVS)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)

#начисления за ХВС со счётчиком
def HVS_with_device(number_LS, request_date, indications_HVS):
    #вытаскивание показаний за прошлый месяц
    try:
        cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' ORDER BY indications_date DESC LIMIT 1 OFFSET 1;""",(number_LS,)) 
        datas = cursor.fetchall()
        last_record_DF = pd.DataFrame(datas)
        last_HVS_indications=int(last_record_DF[2][0])
    except Exception as e:
        last_HVS_indications = 0

    global accrual_HVS, volume_of_consumption_HVS
    volume_of_consumption_HVS = indications_HVS - last_HVS_indications
    accrual_HVS = volume_of_consumption_HVS * standard_frame['tariff(rub/unit_of_measurement)'][0] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_hvs=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_HVS, number_LS, request_date))
        conn.commit()
        print('Начисления за ХВС вычислены:', ("{:8.2f}".format(accrual_HVS)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)

#начисления за ГВС Теплоноситель без счетчика
def GVS_heat_carrier_without_device(number_LS, request_date, number_of_residents):
    global volume_of_consumption_GVS_heat_carrier, accrual_GVS_heat_carrier
    volume_of_consumption_GVS_heat_carrier = number_of_residents * standard_frame['standard'][5] #accrual - начисление
    accrual_GVS_heat_carrier = volume_of_consumption_GVS_heat_carrier * standard_frame['tariff(rub/unit_of_measurement)'][5]
    try:
        cursor.execute("""UPDATE Accruals SET accrual_gvs_heat_carrier=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_GVS_heat_carrier, number_LS, request_date))
        conn.commit()
        print('Начисления за ГВС Теплоноситель вычислены:', ("{:8.2f}".format(accrual_GVS_heat_carrier)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 

#начисления за ГВС Теплоноситель со счётчиком
def GVS_heat_carrier_with_device(number_LS, request_date,indications_GVS):
    #вытаскивание показаний за прошлый месяц
    try:
        cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' ORDER BY indications_date DESC LIMIT 1 OFFSET 1;""",(number_LS,)) 
        datas = cursor.fetchall()
        last_record_DF = pd.DataFrame(datas)
        last_GVS_indications = int(last_record_DF[3][0])
    except Exception as e:
        last_GVS_indications = 0

    global accrual_GVS_heat_carrier, volume_of_consumption_GVS_heat_carrier

    volume_of_consumption_GVS_heat_carrier = indications_GVS - last_GVS_indications
    accrual_GVS_heat_carrier = volume_of_consumption_GVS_heat_carrier * standard_frame['tariff(rub/unit_of_measurement)'][5]
    try:
        cursor.execute("""UPDATE Accruals SET accrual_gvs_heat_carrier=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_GVS_heat_carrier, number_LS, request_date))
        conn.commit()
        print('Начисления за ГВС Теплоноситель вычислены:', ("{:8.2f}".format(accrual_GVS_heat_carrier)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 


#начисления за ГВС Тепловая энергия
def GVS_thermal_energy(number_LS, request_date, volume_of_consumption_GVS_heat_carrier):
    global accrual_GVS_thermal_energy,volume_of_consumption_GVS_thermal_energy
    volume_of_consumption_GVS_thermal_energy = volume_of_consumption_GVS_heat_carrier * standard_frame['standard'][6]
    accrual_GVS_thermal_energy = volume_of_consumption_GVS_thermal_energy * standard_frame['tariff(rub/unit_of_measurement)'][6] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_gvs_thermal_energy=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_GVS_thermal_energy, number_LS, request_date))
        conn.commit()
        print('Начисления за ГВС Тепловая энергия вычислены:', ("{:8.2f}".format(accrual_GVS_thermal_energy)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 

#итоговые начисления за ГВС
def Total_GVS(number_LS, request_date, accrual_GVS_thermal_energy,accrual_GVS_heat_carrier):
    global accrual_GVS
    accrual_GVS = accrual_GVS_thermal_energy + accrual_GVS_heat_carrier
    try:
        cursor.execute("""UPDATE Accruals SET accrual_total_gvs=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_GVS, number_LS, request_date))
        conn.commit()
        print('Итоговые начисления за ГВС:', ("{:8.2f}".format(accrual_GVS)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)


#начисления за Электроэнергию без счетчика
def EE_without_device(number_LS, request_date, number_of_residents):
    global accrual_EE,volume_of_consumption_EE
    volume_of_consumption_EE = number_of_residents * standard_frame['standard'][2]
    accrual_EE = volume_of_consumption_EE * standard_frame['tariff(rub/unit_of_measurement)'][2] #accrual - начисление
    try:
        cursor.execute("""UPDATE Accruals SET accrual_ee=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_EE, number_LS, request_date))
        conn.commit()
        print('Начисления за Электроэнергию вычислены:', ("{:8.2f}".format(accrual_EE)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 

#начисления за Электроэнергию со счётчиком
def EE_with_device(number_LS, request_date, indications_EE_daytime, indications_EE_night):
    #вытаскивание показаний за прошлый месяц
    try:
        cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' ORDER BY indications_date DESC LIMIT 1 OFFSET 1;""",(number_LS,)) 
        datas = cursor.fetchall()
        last_record_DF = pd.DataFrame(datas)
        last_indications_EE_daytime = int(last_record_DF[4][0])
        last_indications_EE_night = int(last_record_DF[6][0])
    except Exception as e:
        last_indications_EE_daytime = 0
        last_indications_EE_night = 0

    global accrual_EE, volume_of_consumption_EE
    volume_of_consumption_EE = (indications_EE_daytime - last_indications_EE_daytime) + (indications_EE_night - last_indications_EE_night)
    volume_of_consumption_daytime=(indications_EE_daytime - last_indications_EE_daytime)
    volume_of_consumption_night=(indications_EE_night - last_indications_EE_night)

    accrual_daytime = volume_of_consumption_daytime * standard_frame['tariff(rub/unit_of_measurement)'][3]
    accrual_night = volume_of_consumption_night * standard_frame['tariff(rub/unit_of_measurement)'][4]
    accrual_EE = accrual_daytime + accrual_night

    try:
        cursor.execute("""UPDATE Accruals SET accrual_ee=%s WHERE number_LS=%s and accrual_date=%s;""",(accrual_EE, number_LS, request_date))
        conn.commit()
        print('Начисления за Электроэнергию вычислены:', ("{:8.2f}".format(accrual_EE)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e) 

#Общий итог по начислениям
def Total_accrual(number_LS,request_date):
    global total_accrual
    total_accrual = accrual_HVS+accrual_GVS + accrual_EE
    try:
        cursor.execute("""UPDATE Accruals SET total_accrual=%s WHERE number_LS=%s and accrual_date=%s;""",(total_accrual, number_LS, request_date))
        conn.commit()
        print('Общий итог по начислениям: ', ("{:8.2f}".format(total_accrual)), 'рублей!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)


#-----------------------
#квитанция?
def receipt(EE_device):
    if EE_device == 2:
        receipt_data_without_EE_device = {#'Квитанция':[номер лс, адрес, дата, ''],
                    'Вид услуг':['Холодное водоснабжение', 'Горячее водоснабжение теп. носитель', 'Горячее водоснабжение теп. энергия', 'Электроэнергия','Всего'],
                    'Ед. изм': [standard_frame['tariff(rub/unit_of_measurement)'][0], standard_frame['tariff(rub/unit_of_measurement)'][5], standard_frame['tariff(rub/unit_of_measurement)'][6], standard_frame['tariff(rub/unit_of_measurement)'][2], ''],
                    'Тариф':[standard_frame['tariff(rub/unit_of_measurement)'][0], standard_frame['tariff(rub/unit_of_measurement)'][5], standard_frame['tariff(rub/unit_of_measurement)'][6], standard_frame['tariff(rub/unit_of_measurement)'][2], ''],
                    'Объем потребления услуги':[volume_of_consumption_HVS, volume_of_consumption_GVS_heat_carrier, volume_of_consumption_GVS_thermal_energy, volume_of_consumption_EE, ''],
                    'Начислено':[accrual_HVS, accrual_GVS_heat_carrier, accrual_GVS_thermal_energy, accrual_EE, total_accrual]
                    }
        receipt_DF=pd.DataFrame(receipt_data_without_EE_device)
        print(receipt_DF)
    else:
        receipt_data_with_EE_device = {#'Квитанция':[номер лс, адрес, дата, ''],
                    'Вид услуг':['Холодное водоснабжение', 'Горячее водоснабжение теп. носитель', 'Горячее водоснабжение теп. энергия', 'Электроэнергия','Всего'],
                    'Ед. изм': [standard_frame['units_of_measurement'][0], standard_frame['units_of_measurement'][5], standard_frame['units_of_measurement'][6], standard_frame['units_of_measurement'][2], ''],
                    'Тариф':[standard_frame['tariff(rub/unit_of_measurement)'][0], standard_frame['tariff(rub/unit_of_measurement)'][5], standard_frame['tariff(rub/unit_of_measurement)'][6], '4.9 / 2.31', ''],
                    'Объем потребления услуги':[volume_of_consumption_HVS, volume_of_consumption_GVS_heat_carrier, volume_of_consumption_GVS_thermal_energy, volume_of_consumption_EE, ''],
                    'Начислено':[accrual_HVS, accrual_GVS_heat_carrier, accrual_GVS_thermal_energy, accrual_EE, total_accrual]
                    }

        receipt_DF=pd.DataFrame(receipt_data_with_EE_device)
        print(receipt_DF)
