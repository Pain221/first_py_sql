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


#создает в базе запись с номером ЛС и датой
def database_record(number_LS,request_date):
    cursor.execute("""INSERT INTO Customers (number_ls, indications_date) VALUES (%s, %s);""",(number_LS, request_date))

#определяет какие показания собирать
def Collecting_data():
    if HVS_device == "ДА":
        Collecting_HVS(number_LS, request_date)
    if GVS_device == "ДА":
        Collecting_GVS(number_LS, request_date)
    if EE_device == "ДА":
        Collecting_EE(number_LS, request_date)
    if condition_of_residents == "ДА":
        Collecting_number_of_residents(number_LS, request_date)
    if condition_of_residents == "НЕТ":
        Number_residents(number_LS)

#собирает показания ХВС
def Collecting_HVS(number_LS, request_date):
    try:
        indications_HVS=int(input('Введите показания ХВС: '))
        cursor.execute("""UPDATE Customers SET indications_hvs=%s WHERE number_LS=%s and indications_date=%s;""",(indications_HVS, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#собирает показания ГВС
def Collecting_GVS(number_LS, request_date):
    try:
        indications_GVS=int(input('Введите показания ХВС: '))
        cursor.execute("""UPDATE Customers SET indications_gvs=%s WHERE number_LS=%s and indications_date=%s;""",(indications_GVS, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#Cобирает показания ЭЭ
def Collecting_EE(number_LS, request_date):
    try:
        indications_EE=int(input('Введите показания ХВС: '))
        cursor.execute("""UPDATE Customers SET indications_ee=%s WHERE number_LS=%s and indications_date=%s;""",(indications_EE, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#собирает количество жильцов
def Collecting_number_of_residents(number_LS, request_date):
    try:
        number_of_residents=int(input('Введите количество проживающих: '))
        cursor.execute("""UPDATE Customers SET number_of_residents=%s WHERE number_LS=%s and indications_date=%s;""",(number_of_residents, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#вытаскивание количества жильцов из базы
def Number_residents(number_LS):
    try:
        cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' LIMIT 1 ;""",(number_LS,)) #СОРТИРОВКУ ДОБАВИТЬ
        datas=cursor.fetchall()
        last_record_DF=pd.DataFrame(datas)
        number_of_residents=last_record_DF[5][0]
        print(number_of_residents) #УБРАТЬ ПОСЛЕ ПРОВЕРКИ
    except Exception:
        conn.rollback()
        print('ошибка!')

Request_data()
Collecting_data()

cursor.close()
conn.close()

