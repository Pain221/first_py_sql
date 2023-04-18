import psycopg2
import datetime

conn=psycopg2.connect("dbname=komunalka user=postgres password=123")
cursor=conn.cursor()

#Запрос данных, GVS - горячая вода, HVS - холодная, EE - электроэнергия
def Request_data():  
    global HVS_device, GVS_device, EE_device, number_LS, request_date
    number_LS=int(input('Введите ваш номер лицевого счета: '))
    number_of_residents=input('введите количество проживающих в помещении')
    request_date=datetime.date.today()
    HVS_device=input('есть ли у вас прибор учета ХВС?(введите ДА или НЕТ)')
    GVS_device=input('есть ли у вас прибор учета ГВС?(введите ДА или НЕТ)')
    EE_device=input('есть ли у вас прибор учета ЭЭ?(введите ДА или НЕТ)')
    return number_LS,request_date

#сбор показаний счетчиков и занесение в базу
def Collecting_data():
    try:
        if HVS_device=='ДА' and GVS_device=='ДА' and EE_device=='ДА':
            indications_HVS=int(input('введите показания ХВС'))
            indications_GVS=int(input('введите показания ГВС'))
            indications_EE=int(input('введите показания ЭЭ'))
            cursor.execute("""INSERT INTO Customers(number_ls, indications_date, indications_hvs, indications_gvs, indications_ee) 
            VALUES (%s, %s, %s, %s, %s);""", (number_LS, request_date, indications_HVS, indications_GVS, indications_EE))
            conn.commit()
            print('Показания внесены!')
    except Exception:
        conn.rollback()
        sys.exc_info()
        print('ошибка!')
        

request_list=Request_data()
Collecting_data()
