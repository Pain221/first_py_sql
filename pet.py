import psycopg2 as pc2
import datetime as dt
import pandas as pd

conn=pc2.connect("dbname=komunalka user=postgres password=123 port=5432")
cursor=conn.cursor()

#Запрос данных, GVS - горячая вода, HVS - холодная, EE - электроэнергия
def Request_data():  
    global HVS_device, GVS_device, EE_device, number_LS, request_date, condition_of_residents
    number_LS=int(input('Введите ваш номер лицевого счета: '))
    condition_of_residents=input('Количество проживающих менялось?(Введите ДА или НЕТ, если заполняете впервые - введие ДА)')
    request_date=dt.date.today()
    HVS_device=input('Есть ли у вас прибор учета ХВС?(введите ДА или НЕТ)')
    GVS_device=input('Есть ли у вас прибор учета ГВС?(введите ДА или НЕТ)')
    EE_device=input('Есть ли у вас прибор учета ЭЭ?(введите ДА или НЕТ)')
    return number_LS,request_date

#сбор показаний счетчиков и занесение в базу
def Collecting_data():
    try:
        if HVS_device=='ДА' and GVS_device=='ДА' and EE_device=='ДА' and condition_of_residents=='ДА':
            indications_HVS=int(input('Введите показания ХВС: '))
            indications_GVS=int(input('Введите показания ГВС: '))
            indications_EE=int(input('Введите показания ЭЭ: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs, indications_gvs, indications_ee, number_of_residents) 
            VALUES (%s, %s, %s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, indications_GVS, indications_EE, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='ДА' and GVS_device=='ДА' and EE_device=='ДА' and condition_of_residents=='НЕТ':
            ndications_HVS=int(input('Введите показания ХВС: '))
            indications_GVS=int(input('Введите показания ГВС: '))
            indications_EE=int(input('Введите показания ЭЭ: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs, indications_gvs, indications_ee) 
            VALUES (%s, %s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, indications_GVS, indications_EE))
            conn.commit()
            print('Показания внесены!')

            #все вариации при изменившемся числе жильцов
        elif HVS_device=='ДА' and GVS_device=='ДА' and EE_device=='НЕТ' and condition_of_residents=='ДА':
            indications_HVS=int(input('Введите показания ХВС: '))
            indications_GVS=int(input('Введите показания ГВС: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs, indications_gvs, number_of_residents) 
            VALUES (%s, %s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, indications_GVS, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='ДА' and GVS_device=='НЕТ' and EE_device=='ДА' and condition_of_residents=='ДА':
            indications_HVS=int(input('Введите показания ХВС: '))
            indications_EE=int(input('Введите показания ЭЭ: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs, indications_ee, number_of_residents) 
            VALUES (%s, %s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, indications_EE, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='ДА' and EE_device=='ДА' and condition_of_residents=='ДА':
            indications_GVS=int(input('Введите показания ГВС: '))
            indications_EE=int(input('Введите показания ЭЭ: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_gvs, indications_ee, number_of_residents) 
            VALUES (%s, %s, %s, %s, %s);""", (number_LS, request_date,  indications_GVS, indications_EE, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='ДА' and GVS_device=='НЕТ' and EE_device=='НЕТ' and condition_of_residents=='ДА':
            indications_HVS=int(input('Введите показания ХВС: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs,  number_of_residents) 
            VALUES (%s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='НЕТ' and EE_device=='ДА' and condition_of_residents=='ДА':
            indications_EE=int(input('Введите показания ЭЭ: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date,  indications_ee, number_of_residents) 
            VALUES (%s, %s, %s, %s);""", (number_LS, request_date,  indications_EE, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='ДА' and EE_device=='НЕТ' and condition_of_residents=='ДА':
            indications_GVS=int(input('Введите показания ГВС: '))
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date,  indications_gvs,  number_of_residents) 
            VALUES (%s, %s, %s, %s);""", (number_LS, request_date,  indications_GVS, number_of_residents))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='НЕТ' and EE_device=='НЕТ' and condition_of_residents=='ДА':
            number_of_residents=int(input('Введите количество проживающих: '))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date,  number_of_residents) 
            VALUES (%s, %s, %s);""", (number_LS, request_date,  number_of_residents))
            conn.commit()
            print('Показания внесены!')

        #ниже непроверенные элифы
        #все вариации при НЕ изменившемся числе жильцов
        elif HVS_device=='ДА' and GVS_device=='ДА' and EE_device=='НЕТ' and condition_of_residents=='НЕТ':
            indications_HVS=int(input('Введите показания ХВС: '))
            indications_GVS=int(input('Введите показания ГВС: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs, indications_gvs) 
            VALUES (%s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, indications_GVS))
            conn.commit()
            print('Показания внесены!')
        elif HVS_device=='ДА' and GVS_device=='НЕТ' and EE_device=='ДА' and condition_of_residents=='НЕТ':
            indications_HVS=int(input('Введите показания ХВС: '))
            indications_EE=int(input('Введите показания ЭЭ: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs,  indications_ee) 
            VALUES (%s, %s, %s, %s);""", (number_LS, request_date, indications_HVS,  indications_EE))
            conn.commit()
            print('Показания внесены!')
        elif HVS_device=='НЕТ' and GVS_device=='ДА' and EE_device=='ДА' and condition_of_residents=='НЕТ':
            indications_GVS=int(input('Введите показания ГВС: '))
            indications_EE=int(input('Введите показания ЭЭ: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date,  indications_gvs, indications_ee) 
            VALUES (%s, %s, %s, %s);""", (number_LS, request_date,  indications_GVS, indications_EE))
            conn.commit()
            print('Показания внесены!')
        elif HVS_device=='ДА' and GVS_device=='НЕТ' and EE_device=='НЕТ' and condition_of_residents=='НЕТ':
            indications_HVS=int(input('Введите показания ХВС: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs) 
            VALUES (%s, %s, %s);""", (number_LS, request_date, indications_HVS))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='НЕТ' and EE_device=='ДА' and condition_of_residents=='НЕТ':
            indications_EE=int(input('Введите показания ЭЭ: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date,  indications_ee) 
            VALUES (%s, %s, %s);""", (number_LS, request_date,  indications_EE))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='ДА' and EE_device=='НЕТ' and condition_of_residents=='НЕТ':
            indications_GVS=int(input('Введите показания ГВС: '))

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_gvs) 
            VALUES (%s, %s, %s);""", (number_LS, request_date, indications_GVS))
            conn.commit()
            print('Показания внесены!')

        elif HVS_device=='НЕТ' and GVS_device=='НЕТ' and EE_device=='НЕТ' and condition_of_residents=='НЕТ':

            #вытаскивание кол-ва жильцов из базы
            request=cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,))
            datas=cursor.fetchall()
            frame=pd.DataFrame(datas)
            number_of_residents=frame[5][0]
            print(number_of_residents)

            cursor.execute("""INSERT INTO Customers(number_ls, indications_date) 
            VALUES (%s, %s);""", (number_LS, request_date))
            conn.commit()
            print('Показания внесены!')
    except Exception:
        conn.rollback()
        #print(sys.exc_info())
        print('ошибка!')
        

Request_data()
Collecting_data()

cursor.close()
conn.close()
