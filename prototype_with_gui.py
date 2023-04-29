import psycopg2 as pc2
import pandas as pd

conn=pc2.connect("dbname=*** user=*** password=*** port=***")
cursor=conn.cursor()

#внесение в базу показаний ХВС
def Collecting_HVS(number_LS, request_date, indications_HVS):
    try:
        cursor.execute("""UPDATE Customers SET indications_hvs=%s WHERE number_LS=%s and indications_date=%s;""",(indications_HVS, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#внесение в базу показаний ГВС
def Collecting_GVS(number_LS, request_date, indications_GVS):
    try:
        cursor.execute("""UPDATE Customers SET indications_gvs=%s WHERE number_LS=%s and indications_date=%s;""",(indications_GVS, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#внесение в базу показаний ЭЭ
def Collecting_EE(number_LS, request_date, indications_EE_daytime, indications_EE_night):
    try:
        cursor.execute("""UPDATE Customers SET indications_ee_daytime=%s WHERE number_LS=%s and indications_date=%s;""",(indications_EE_daytime, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
        cursor.execute("""UPDATE Customers SET indications_ee_night=%s WHERE number_LS=%s and indications_date=%s;""",(indications_EE_night, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#внесение в базу кол-ва жильцов
def Collecting_number_of_residents(number_LS, request_date, number_of_residents):
    try:
        cursor.execute("""UPDATE Customers SET number_of_residents=%s WHERE number_LS=%s and indications_date=%s;""",(number_of_residents, number_LS, request_date))
        conn.commit()
        print('Показания внесены!')
    except Exception:
        conn.rollback()
        print('ошибка!')

#создает в базе запись с номером ЛС и датой
def database_record(number_LS,request_date):
    cursor.execute("""INSERT INTO Customers (number_ls, indications_date) VALUES (%s, %s);""",(number_LS, request_date))

#вытаскивание количества жильцов из базы и занесение в новую строку
def Number_residents(number_LS, request_date):
    global number_of_residents
    try:
        cursor.execute("""SELECT * FROM Customers WHERE number_ls='%s' ORDER BY indications_date DESC LIMIT 1 OFFSET 1;""",(number_LS,)) 
        datas=cursor.fetchall()
        last_record_DF=pd.DataFrame(datas)
        number_of_residents=last_record_DF[5][0]
        cursor.execute("""UPDATE Customers SET number_of_residents=%s WHERE number_LS=%s and indications_date=%s;""",(int(number_of_residents), number_LS, request_date))
        conn.commit()
        print('Число жильцов внесено!')
    except Exception as e:
        conn.rollback()
        print('ошибка!')
        print(e)

