import pandas as pd

tariff_data={'service':['HVS', 'GVS', 'EE','EE_daytime', 'EE_night','GVS_heat_carrier', 'GVS_thermal_energy' ],
             'tariff(rub/unit_of_measurement)':[35.78, 158.98, 4.28, 4.9, 2.31, 35.78, 998.69],
             'standard':[4.85, 4.01, 164, '-', '-', 4.01, 0.05349],
             'units_of_measurement':['m^3', 'm^3', 'kW/h','kW/h', 'kW/h','m^3','Gcal']
             }
standard_frame=pd.DataFrame(tariff_data)
#print(standard_frame)

#начисления за ХВС без счётчика
def HVS_without_device(number_LS, request_date, number_of_residents):
    volume_of_consumption=number_of_residents*standard_frame['standard'][0]
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][0] #accrual - начисление
    #добавить внос начисления в базу 

#начисления за ГВС Теплоноситель без счетчика
def GVS_heat_carrier_without_device(number_LS, request_date, number_of_residents):
    global volume_of_consumption_GVS_heat_carrier
    volume_of_consumption_GVS_heat_carrier =number_of_residents*standard_frame['tariff(rub/unit_of_measurement)'][1]
    accrual=volume_of_consumption_GVS_heat_carrier*standard_frame['standard'][1] #accrual - начисление
    #добавить внос начисления в базу 

#начисления за ГВС Тепловая энергия
def GVS_thermal_energy(number_LS, request_date, number_of_residents, volume_of_consumption_GVS_heat_carrier):
    volume_of_consumption=volume_of_consumption_GVS_heat_carrier*standard_frame['standard'][6]
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][6] #accrual - начисление
    #добавить внос начисления в базу 

#начисления за Электроэнергию без счетчика
def EE_without_device(number_LS, request_date, number_of_residents):
    volume_of_consumption=number_of_residents*standard_frame['standard'][2]
    accrual=volume_of_consumption*standard_frame['tariff(rub/unit_of_measurement)'][2] #accrual - начисление
    #добавить внос начисления в базу 