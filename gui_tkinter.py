from tkinter import *
import datetime as dt
import calculations_with_gui as cl
from prototype_with_gui import *
from connections import *
import re
import tkinter.filedialog as fd
import os

request_date=dt.date.today()

#создание главных фрейма и окна
def main_window():
    global main_frame, window
    window = Tk()
    window.title("Показания счётчиков онлайн")
    window.geometry('800x650')

    main_frame = Frame(window)
    main_frame.pack(expand=True)

#лист авторизации
def authorization():
    frame_w=Frame(main_frame, padx = 100, pady = 50) 
    frame_w.pack(expand = True) 

    welcome_text = Label(frame_w, text='Добро пожаловать!', font = ('Arial', 30)) 
    welcome_text.grid()

    frame_big=Frame(main_frame)
    frame_big.pack(expand=True)

    frame_LS=Frame(frame_big)  
    frame_LS.pack(expand=True) 

    LS_text = Label(frame_LS, text='Номер лицевого счета : ', font = ('Arial', 10))
    LS_text.grid()

    #ввод личного счета и пароля
    frame_LS_i = Frame(frame_big) 
    frame_LS_i.pack(expand=True) 

    input_LS = Entry(frame_LS_i)
    input_LS.grid()
    input_LS.focus()

    frame_pass = Frame(frame_big)  
    frame_pass.pack(expand=True) 

    password_text = Label(frame_pass, text = 'Пароль : ', font = ('Arial', 10))
    password_text.grid()

    frame_pass_i = Frame(frame_big)
    frame_pass_i.pack(expand=True) 

    input_password = Entry(frame_pass_i)
    input_password.grid()

    #запуск алгоритма аторизации
    def executing():
        validation_LS(input_LS)
        authorization_validate(input_LS, input_password)

    frame_b_0 = Frame(main_frame)  
    frame_b_0.pack(expand=True)  
 
    input_buttion_0 = Button(frame_b_0,text = 'Ввести', command = executing, height = 5, width = 20)
    input_buttion_0.grid()


#создание первой страницы
def first_page():
    frame_w = Frame(main_frame)  
    frame_w.pack(expand = True, padx = 100, pady = 50) 

    welcome_text = Label(frame_w, text='Заполните данные: ', font = ('Arial', 30)) 
    welcome_text.grid()

    #статус кол-ва проживающих
    big_frame_residents = Frame(main_frame)
    big_frame_residents.pack(expand = True, pady = 5)

    frame_residents=Frame(big_frame_residents)  
    frame_residents.grid(row = 1, column = 1)

    condition_of_residents_text1 = Label(frame_residents, text='Количество проживающих менялось?', font = ('Arial', 10))
    condition_of_residents_text1.grid(row = 1, column = 1)
    condition_of_residents_text2 = Label(frame_residents, text='(Если заполняете впервые - введие ДА) ', font = ('Arial', 8))
    condition_of_residents_text2.grid(row = 2, column = 1)

    condition_of_residents_input = IntVar()
    condition_of_residents_input.set(1)

    frame_residents_b = Frame(big_frame_residents)  
    frame_residents_b.grid(row = 1, column = 2)

    yes_condition_of_residents = Radiobutton(frame_residents_b, text = 'ДА', value = 1,variable = condition_of_residents_input)
    yes_condition_of_residents.grid(row = 1, column = 1)
    no_condition_of_residents = Radiobutton(frame_residents_b, text = 'НЕТ', value = 2,variable = condition_of_residents_input)
    no_condition_of_residents.grid(row = 1, column = 2)

    #наличие ХВС
    big_frame_HVS = Frame(main_frame)
    big_frame_HVS.pack(expand = True, pady = 5)
    
    frame_HVS_d = Frame(big_frame_HVS)  
    frame_HVS_d.grid(row = 1, column = 1)
    
    HVS_device_text = Label(frame_HVS_d, text = 'Есть ли у вас прибор учета ХВС?(введите ДА или НЕТ)',  font = ('Arial', 10) )
    HVS_device_text.grid()

    HVS_device_input = IntVar()
    HVS_device_input.set(1)

    frame_HVS_d_b = Frame(big_frame_HVS)  
    frame_HVS_d_b.grid(row = 1, column = 2)

    yes_HVS_device = Radiobutton(frame_HVS_d_b, text = 'ДА', value = 1,variable=HVS_device_input)
    yes_HVS_device.grid(row = 1, column = 1)
    no_HVS_device = Radiobutton(frame_HVS_d_b, text = 'НЕТ', value = 2,variable=HVS_device_input)
    no_HVS_device.grid(row = 1, column = 2)

    #наличие ГВС
    big_frame_GVS = Frame(main_frame)
    big_frame_GVS.pack(expand = True, pady = 5)

    frame_GVS_d = Frame(big_frame_GVS)  
    frame_GVS_d.grid(row = 1, column = 1)

    GVS_device_text = Label(frame_GVS_d, text = 'Есть ли у вас прибор учета ГВС?(введите ДА или НЕТ)',  font = ('Arial', 10) )
    GVS_device_text.grid()

    GVS_device_input = IntVar()
    GVS_device_input.set(1)

    frame_GVS_d_b = Frame(big_frame_GVS)  
    frame_GVS_d_b.grid(row = 1, column = 2)

    yes_GVS_device = Radiobutton(frame_GVS_d_b, text = 'ДА', value = 1,variable=GVS_device_input)
    yes_GVS_device.grid(row = 1, column = 1)
    no_GVS_device = Radiobutton(frame_GVS_d_b, text = 'НЕТ', value = 2,variable=GVS_device_input)
    no_GVS_device.grid(row = 1, column = 2)

    #наличие ЭЭ
    big_frame_EE = Frame(main_frame)
    big_frame_EE.pack(expand = True, pady = 5)

    frame_EE_d = Frame(big_frame_EE)  
    frame_EE_d.grid(row = 1, column = 1)
    
    EE_device_text = Label(frame_EE_d, text = 'Есть ли у вас прибор учета ЭЭ?(введите ДА или НЕТ)',  font = ('Arial', 10) )
    EE_device_text.grid()

    EE_device_input = IntVar()
    EE_device_input.set(1)

    frame_EE_d_b = Frame(big_frame_EE)  
    frame_EE_d_b.grid(row = 1, column = 2)   

    yes_EE_device = Radiobutton(frame_EE_d_b, text = 'ДА', value = 1,variable=EE_device_input)
    yes_EE_device.grid(row = 1, column = 1)
    no_EE_device = Radiobutton(frame_EE_d_b, text = 'НЕТ', value = 2,variable=EE_device_input)
    no_EE_device.grid(row = 1, column = 2)

    #обработка ввода
    def Input_process():
        global condition_of_residents, HVS_device, GVS_device, EE_device
        database_record(number_LS,request_date)
        condition_of_residents = int(condition_of_residents_input.get())
        HVS_device = int(HVS_device_input.get())
        GVS_device = int(GVS_device_input.get())
        EE_device = int(EE_device_input.get())
        for widget in main_frame.winfo_children():
            widget.destroy()
        second_page()
    
    frame_b_1 = Frame(main_frame)  
    frame_b_1.pack(expand = True)

    input_buttion = Button(frame_b_1,text = 'Ввести', command = Input_process, height = 5, width = 20)
    input_buttion.grid()
#---------------------------------------------------------------------------------------------------------------
#проверка ввода номера лс
def validation_LS(input_LS):
    string=input_LS.get()
    pattern = r'\d{6}' #шесть чисел
    match = re.fullmatch(pattern, str(string))
    if not match:
        frame_error_0 = Frame(main_frame)
        frame_error_0.pack(expand=True)

        error_label = Label(frame_error_0, text = 'НЕКОРРЕКТНЫЙ НОМЕР ЛИЦЕВОГО СЧЕТА',  font = ('Arial', 10), fg = 'red')
        error_label.grid()
        input_LS.delete(0, END)

#проверка ввода показаний
def validation_indications(string_to_valid):
    string=string_to_valid.get()
    pattern = r'[1-9]\d{0,}' #первый не ноль, а после любое кол-во чисел
    match = re.fullmatch(pattern, str(string))
    if not match:
        frame_error_1 = Frame(main_frame)
        frame_error_1.pack(expand=True)

        error_label = Label(frame_error_1, text = 'НЕКОРРЕКТНЫЕ ДАННЫЕ',  font = ('Arial', 10), fg = 'red')
        error_label.grid()
        string_to_valid.delete(0, END)

#авторизация
def authorization_validate(input_LS, input_password):
    string=int(input_LS.get())
    try:
        cursor.execute("""SELECT * FROM Users WHERE number_ls='%s';""",(int(input_LS.get()),)) 
        datas = cursor.fetchall()
        user_data_DF = pd.DataFrame(datas)
        number_LS_DB = user_data_DF[0][0]
    except:
        frame_error_2 = Frame(main_frame)
        frame_error_2.pack(expand = True)

        error_label = Label(frame_error_2, text = 'НЕКОРРЕКТНЫЙ НОМЕР ЛС',  font = ('Arial', 10), fg = 'red')
        error_label.grid()
        input_LS.delete(0, END)

    if string != number_LS_DB:
        frame_error_3 = Frame(main_frame)
        frame_error_3.pack(expand = True)

        error_label = Label(frame_error_3, text = 'НЕКОРРЕКТНЫЙ НОМЕР ЛС',  font = ('Arial', 10), fg = 'red')
        error_label.grid()
        input_LS.delete(0, END)
    else:
        string_2 = str(input_password.get())
        password_DB = user_data_DF[1][0]
        if string_2 != password_DB:
            frame_error_4 = Frame(main_frame)
            frame_error_4.pack(expand = True)

            error_label = Label(frame_error_4, text = 'НЕВЕРНЫЙ ПАРОЛЬ',  font = ('Arial', 10), fg = 'red')
            error_label.grid()
            input_password.delete(0, END)
        else:
            global number_LS
            number_LS = int(input_LS.get())
            for widget in main_frame.winfo_children():
                widget.destroy()
            first_page()
#----------------------------------------------------------------------------------------------------------------------------------------
#создание второй страницы
def second_page():
    frame_w = Frame(main_frame, padx = 100, pady = 50) 
    frame_w.pack(expand=True) 

    welcome_text_1 = Label(frame_w, text = 'Сбор показаний', font = ('Arial', 30)) 
    welcome_text_1.grid()

    #запрос показаний хвс
    if HVS_device == 1:
        big_HVS_frame=Frame(main_frame, pady = 5)
        big_HVS_frame.pack(expand = True)

        frame_HVS=Frame(big_HVS_frame)
        frame_HVS.grid(row = 1, column = 1)

        indications_HVS_text = Label(frame_HVS, text = 'Введите показания ХВС: ', font = ('Arial', 10))
        indications_HVS_text.grid()

        frame_HVS_e = Frame(big_HVS_frame)
        frame_HVS_e.grid(row = 1, column = 2)

        input_incications_HVS = Entry(frame_HVS_e)
        input_incications_HVS.grid()

    #запрос показаний гвс
    if GVS_device == 1:
        big_GVS_frame = Frame(main_frame, pady = 5)
        big_GVS_frame.pack(expand = True)

        frame_GVS = Frame(big_GVS_frame)
        frame_GVS.grid(row = 1, column = 1)

        indications_GVS_text = Label(frame_GVS, text = 'Введите показания ГВС: ', font = ('Arial', 10))
        indications_GVS_text.grid()

        frame_GVS_e = Frame(big_GVS_frame)
        frame_GVS_e.grid(row = 1, column = 2)

        input_incications_GVS = Entry(frame_GVS_e)
        input_incications_GVS.grid()
        
    #запрос показаний ЭЭ
    if EE_device == 1:
        big_EE_daytime_frame = Frame(main_frame, pady = 5)
        big_EE_daytime_frame.pack(expand=True)

        frame_EE_daytime = Frame(big_EE_daytime_frame)
        frame_EE_daytime.grid(row = 1, column = 1)

        indications_EE_text = Label(frame_EE_daytime, text = 'Введите показания ЭЭ с дневной шкалы: ', font = ('Arial', 10))
        indications_EE_text.grid()

        frame_EE_daytime_e = Frame(big_EE_daytime_frame)
        frame_EE_daytime_e.grid(row = 1, column = 2)

        input_indications_EE_daytime = Entry(frame_EE_daytime_e)
        input_indications_EE_daytime.grid()

        big_EE_night_frame = Frame(main_frame, pady=5)
        big_EE_night_frame.pack(expand=True)

        frame_EE_night = Frame(big_EE_night_frame)
        frame_EE_night.grid(row = 1, column = 1)

        indications_EE_text_2 = Label(frame_EE_night, text = 'Введите показания ЭЭ с ночной шкалы: ', font = ('Arial', 10))
        indications_EE_text_2.grid()

        frame_EE_night_e = Frame(big_EE_night_frame)
        frame_EE_night_e.grid(row = 1, column = 2)

        input_indications_EE_night = Entry(frame_EE_night_e)
        input_indications_EE_night.grid()

    #запрос кол-ва жильцов
    if condition_of_residents == 1:
        big_residents_frame = Frame(main_frame, pady = 5)
        big_residents_frame.pack(expand = True)

        frame_residents=Frame(big_residents_frame)
        frame_residents.grid(row = 1, column = 1)

        number_of_residents_text = Label(frame_residents, text = 'Введите кол-во жильцов: ', font = ('Arial', 10))
        number_of_residents_text.grid()

        frame_residents_e = Frame(big_residents_frame)
        frame_residents_e.grid(row = 1, column = 2)

        input_number_of_residents = Entry(frame_residents_e)
        input_number_of_residents.grid()
        
    if condition_of_residents == 2:
        Number_residents(number_LS, request_date) #вытаскивает последнее число жильцов и вносит в базу

    #вносит собранные показания в базу данных и запускает вычисления
    def Collecting_data_gui():
        global indications_EE_daytime, indications_EE_night, indications_HVS, indications_GVS, number_of_residents
        if HVS_device == 1:
            validation_indications(input_incications_HVS) 
            indications_HVS = int(input_incications_HVS.get())
            Collecting_HVS(number_LS, request_date, indications_HVS)
        if GVS_device == 1:
            validation_indications(input_incications_GVS) 
            indications_GVS = int(input_incications_GVS.get())
            Collecting_GVS(number_LS, request_date, indications_GVS)
        if EE_device == 1:
            validation_indications(input_indications_EE_daytime) 
            validation_indications(input_indications_EE_night) 
            indications_EE_daytime = int(input_indications_EE_daytime.get())
            indications_EE_night = int(input_indications_EE_night.get())
            Collecting_EE(number_LS, request_date, indications_EE_daytime, indications_EE_night)
        if condition_of_residents == 1:
            validation_indications(input_number_of_residents) 
            number_of_residents = int(input_number_of_residents.get())
            Collecting_number_of_residents(number_LS, request_date, number_of_residents)

        cl.database_record_accrual(number_LS,request_date)
        if HVS_device == 2:
            cl.HVS_without_device(number_of_residents, number_LS, request_date)
        if HVS_device == 1:
            cl.HVS_with_device(number_LS, request_date, indications_HVS)

        if GVS_device==2:
            cl.GVS_heat_carrier_without_device(number_LS, request_date, number_of_residents)
        if GVS_device == 1:
            cl.GVS_heat_carrier_with_device(number_LS, request_date, indications_GVS)
        cl.GVS_thermal_energy(number_LS, request_date,  cl.volume_of_consumption_GVS_heat_carrier)
        cl.Total_GVS(number_LS, request_date, cl.accrual_GVS_thermal_energy, cl.accrual_GVS_heat_carrier)

        if EE_device == 2:
            cl.EE_without_device(number_LS, request_date, number_of_residents)
        if EE_device == 1:
            cl.EE_with_device(number_LS, request_date,indications_EE_daytime, indications_EE_night)

        cl.Total_accrual(number_LS,request_date)
        for widget in main_frame.winfo_children():
            widget.destroy()
        third_page()

    frame_b_2 = Frame(main_frame)  
    frame_b_2.pack(expand=True)

    input_buttion_2 = Button(frame_b_2,text = 'Ввести', command = Collecting_data_gui, height = 5, width = 20)
    input_buttion_2.grid()

#---------------------------------------------------------
#сохранение квитанции в эксель
def save():
    path = fd.askdirectory()
    os.chdir(path)
    path = path + '/receipt.xlsx'
    cl.receipt(EE_device, path)
#--------------------------------------------------------
#создание третьей страницы(вывод всех начислений)
def third_page():
    frame_w = Frame(main_frame, padx = 100, pady = 50) 
    frame_w.pack(expand=True) 

    welcome_text = Label(frame_w, text = 'Начисления произведены!', font = ('Arial', 30)) 
    welcome_text.grid()

    big_frame_hvs = Frame(main_frame, pady = 5)
    big_frame_hvs.pack(expand=True)

    frame_hvs = Frame(big_frame_hvs)
    frame_hvs.grid(row = 1, column = 1)

    hvs_text = Label(frame_hvs, text = 'ХВС: ', font = ('Arial', 10)  )
    hvs_text.grid()

    frame_hvs_v = Frame(big_frame_hvs)
    frame_hvs_v.grid(row = 1, column = 2)

    hvs_var = Label(frame_hvs_v, text = ("{:8.2f}".format(cl.accrual_HVS) + ' рублей!'), font = ('Arial', 10) )
    hvs_var.grid()

    big_frame_gvs_1 = Frame(main_frame, pady = 5)
    big_frame_gvs_1.pack(expand = True)

    frame_gvs_1 = Frame(big_frame_gvs_1)
    frame_gvs_1.grid(row = 1, column = 1)

    gvs_text_1 = Label(frame_gvs_1, text = 'ГВС Теплоноситель: ', font = ('Arial', 10)  )
    gvs_text_1.grid()

    frame_gvs_1_v = Frame(big_frame_gvs_1)
    frame_gvs_1_v.grid(row = 1, column = 2)

    gvs_var_1 = Label(frame_gvs_1_v, text = ("{:8.2f}".format(cl.accrual_GVS_heat_carrier) + ' рублей!'), font = ('Arial', 10) )
    gvs_var_1.grid()

    big_frame_gvs_2 = Frame (main_frame, pady = 5)
    big_frame_gvs_2.pack(expand = True)

    frame_gvs_2=Frame(big_frame_gvs_2)
    frame_gvs_2.grid(row = 1, column = 1)

    gvs_text_2 = Label(frame_gvs_2, text = 'ГВС Тепловая энергия: ', font = ('Arial', 10)  )
    gvs_text_2.grid()

    frame_gvs_2_v = Frame(big_frame_gvs_2)
    frame_gvs_2_v.grid(row = 1, column = 2)

    gvs_var_2 = Label(frame_gvs_2_v, text = ("{:8.2f}".format(cl.accrual_GVS_thermal_energy) + ' рублей!'), font = ('Arial', 10) )
    gvs_var_2.grid()

    big_frame_gvs_3 = Frame (main_frame, pady = 5)
    big_frame_gvs_3.pack(expand=True)

    frame_gvs_3 = Frame(big_frame_gvs_3)
    frame_gvs_3.grid(row = 1, column = 1)

    gvs_text_3 = Label(frame_gvs_3, text = 'ГВС Итого: ', font = ('Arial', 10)  )
    gvs_text_3.grid()

    frame_gvs_3_v = Frame(big_frame_gvs_3)
    frame_gvs_3_v.grid(row = 1, column = 2)

    gvs_var_3 = Label(frame_gvs_3_v, text = ("{:8.2f}".format(cl.accrual_GVS) + ' рублей!'), font = ('Arial', 10) )
    gvs_var_3.grid()

    big_frame_ee = Frame (main_frame, pady = 5)
    big_frame_ee.pack(expand=True)

    frame_ee = Frame(big_frame_ee)
    frame_ee.grid(row = 1, column = 1)

    ee_text = Label(frame_ee, text = 'ЭЭ: ', font = ('Arial', 10)  )
    ee_text.grid()

    frame_ee_v = Frame(big_frame_ee)
    frame_ee_v.grid(row = 1, column = 2)

    ee_var = Label(frame_ee_v, text = ("{:8.2f}".format(cl.accrual_EE) + ' рублей!'), font = ('Arial', 10) )
    ee_var.grid()

    big_frame_total = Frame (main_frame, pady = 5)
    big_frame_total.pack(expand=True)

    frame_total=Frame(big_frame_total)
    frame_total.grid(row = 1, column = 1)

    total_text = Label(frame_total, text = 'Итого: ', font = ('Arial', 10)  )
    total_text.grid()

    frame_total_v = Frame(big_frame_total)
    frame_total_v.grid(row = 1, column = 2)

    total_var = Label(frame_total_v, text = ("{:8.2f}".format(cl.total_accrual) + ' рублей!'), font = ('Arial', 10) )
    total_var.grid()

    frame_b_3 = Frame(main_frame)
    frame_b_3.pack(expand=True)

    #кнопка для сохранения квитанции
    buttion_save = Button(frame_b_3,text = 'Сохранить квитанцию', command = save, height = 5, width = 20)
    buttion_save.grid()

#главная функция для main
def manage():
    main_window()
    authorization()
    window.mainloop()
