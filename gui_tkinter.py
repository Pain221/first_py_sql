from tkinter import *
from tkinter import messagebox
import datetime as dt
import calculations_with_gui as cl
from prototype_with_gui import *
from connections import *
import re
import tkinter.filedialog as fd
import os

request_date=dt.date.today()

#создание фрейма и окна
def main_window():
    global frame, window
    window=Tk()
    window.title("Показания счётчиков онлайн")
    window.geometry('800x650')

    frame=Frame(window, padx=100, pady=100) #контейнер 
    frame.pack(expand=True) #включена возможность заполнения


#лист авторизации
def authorization():
    welcome_text = Label(frame, text='Добро пожаловать!', font = ('Arial', 30)) 
    welcome_text.grid(row = 3, column = 1)

    LS_text = Label(frame, text='Номер лицевого счета : ', font = ('Arial', 10))
    LS_text.grid(row = 4, column = 1)

    #ввод личного счета
    input_LS = Entry(frame)
    input_LS.grid(row = 4, column = 2)
    input_LS.focus()

    password_text = Label(frame, text='Пароль : ', font = ('Arial', 10))
    password_text.grid(row = 5, column = 1)

    input_password = Entry(frame)
    input_password.grid(row = 5, column = 2)

    def executing():
        validation_LS(input_LS)
        authorization_validate(input_LS, input_password)

 
    input_buttion_0 = Button(frame,text = 'Ввести', command = executing, height = 5, width = 20)
    input_buttion_0.grid(row = 6, column = 1)


#создание первой страницы
def first_page():
    welcome_text = Label(frame, text='Заполните данные: ', font = ('Arial', 30)) 
    welcome_text.grid(row = 3, column = 1)

    #статус кол-ва проживающих
    condition_of_residents_text1 = Label(frame, text='Количество проживающих менялось?', font = ('Arial', 10))
    condition_of_residents_text1.grid(row = 5, column = 1)
    condition_of_residents_text2 = Label(frame, text='(Если заполняете впервые - введие ДА) ', font = ('Arial', 8))
    condition_of_residents_text2.grid(row = 6, column = 1)

    condition_of_residents_input = IntVar()
    condition_of_residents_input.set(1)

    yes_condition_of_residents = Radiobutton(frame, text = 'ДА', value = 1,variable=condition_of_residents_input)
    yes_condition_of_residents.grid(row = 5, column = 2)
    no_condition_of_residents = Radiobutton(frame, text = 'НЕТ', value = 2,variable=condition_of_residents_input)
    no_condition_of_residents.grid(row = 5, column = 3)

    #наличие ХВС
    HVS_device_text = Label(frame, text='Есть ли у вас прибор учета ХВС?(введите ДА или НЕТ)',  font = ('Arial', 10) )
    HVS_device_text.grid(row = 7, column = 1)

    HVS_device_input = IntVar()
    HVS_device_input.set(1)

    yes_HVS_device = Radiobutton(frame, text = 'ДА', value = 1,variable=HVS_device_input)
    yes_HVS_device.grid(row = 7, column = 2)
    no_HVS_device = Radiobutton(frame, text = 'НЕТ', value = 2,variable=HVS_device_input)
    no_HVS_device.grid(row = 7, column = 3)

    #наличие ГВС
    GVS_device_text = Label(frame, text = 'Есть ли у вас прибор учета ГВС?(введите ДА или НЕТ)',  font = ('Arial', 10) )
    GVS_device_text.grid(row = 8, column = 1)

    GVS_device_input = IntVar()
    GVS_device_input.set(1)

    yes_GVS_device = Radiobutton(frame, text = 'ДА', value = 1,variable=GVS_device_input)
    yes_GVS_device.grid(row = 8, column = 2)
    no_GVS_device = Radiobutton(frame, text = 'НЕТ', value = 2,variable=GVS_device_input)
    no_GVS_device.grid(row = 8, column = 3)


    #наличие ЭЭ
    EE_device_text = Label(frame, text = 'Есть ли у вас прибор учета ЭЭ?(введите ДА или НЕТ)',  font = ('Arial', 10) )
    EE_device_text.grid(row=9, column=1)

    EE_device_input = IntVar()
    EE_device_input.set(1)

    yes_EE_device = Radiobutton(frame, text = 'ДА', value = 1,variable=EE_device_input)
    yes_EE_device.grid(row = 9, column = 2)
    no_EE_device = Radiobutton(frame, text = 'НЕТ', value = 2,variable=EE_device_input)
    no_EE_device.grid(row = 9, column = 3)

    #обработка ввода
    def Input_process():
        global condition_of_residents, HVS_device, GVS_device, EE_device
        database_record(number_LS,request_date)
        condition_of_residents = int(condition_of_residents_input.get())
        HVS_device = int(HVS_device_input.get())
        GVS_device = int(GVS_device_input.get())
        EE_device = int(EE_device_input.get())
        messagebox.showinfo('ТЕСТ', f"{number_LS, HVS_device, GVS_device, EE_device, condition_of_residents} ") #ПОСЛЕ ТЕСТОВ УДАЛИТЬ 
        for widget in frame.winfo_children():
            widget.destroy()
        second_page()
    
    input_buttion = Button(frame,text = 'Ввести', command = Input_process, height = 5, width = 20)
    input_buttion.grid(row = 10, column = 1)


#----------------------------------------------
#проверка ввода номера лс
def validation_LS(input_LS):
    string=input_LS.get()
    pattern = r'\d{6}' #шесть чисел
    match = re.fullmatch(pattern, str(string))
    if not match:
        error_label = Label(frame, text = 'НЕКОРРЕКТНЫЙ НОМЕР ЛИЦЕВОГО СЧЕТА',  font = ('Arial', 10), fg='red')
        error_label.grid(row = 11, column = 1)
        input_LS.delete(0, END)

#проверка ввода показаний
def validation_indications(string_to_valid):
    string=string_to_valid.get()
    pattern = r'[1-9]\d{0,}' #первый не ноль, а после любое кол-во чисел
    match = re.fullmatch(pattern, str(string))
    if not match:
        error_label = Label(frame, text = 'НЕКОРРЕКТНЫЕ ДАННЫЕ',  font = ('Arial', 10), fg='red')
        error_label.grid(row = 11, column = 1)
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
        error_label = Label(frame, text = 'НЕКОРРЕКТНЫЙ НОМЕР ЛС',  font = ('Arial', 10), fg='red')
        error_label.grid(row = 7, column = 1)
        input_LS.delete(0, END)

    if string != number_LS_DB:
        error_label = Label(frame, text = 'НЕКОРРЕКТНЫЙ НОМЕР ЛС',  font = ('Arial', 10), fg='red')
        error_label.grid(row = 7, column = 1)
        input_LS.delete(0, END)
    else:
        string_2=str(input_password.get())
        password_DB = user_data_DF[1][0]
        if string_2 != password_DB:
            error_label = Label(frame, text = 'НЕВЕРНЫЙ ПАРОЛЬ',  font = ('Arial', 10), fg='red')
            error_label.grid(row = 7, column = 1)
            input_password.delete(0, END)
        else:
            global number_LS
            number_LS=int(input_LS.get())
            for widget in frame.winfo_children():
                widget.destroy()
            first_page()
#---------------------------------------------
#создание второй страницы
def second_page():
    welcome_text_1 = Label(frame, text = 'Сбор показаний', font = ('Arial', 30)) 
    welcome_text_1.grid(row = 3, column = 1)

    if HVS_device == 1:
        indications_HVS_text = Label(frame, text = 'Введите показания ХВС: ', font=('Arial', 10))
        indications_HVS_text.grid(row = 4, column = 1)

        input_incications_HVS = Entry(frame)
        input_incications_HVS.grid(row = 4, column = 2)

    if GVS_device == 1:
        indications_GVS_text = Label(frame, text = 'Введите показания ГВС: ', font = ('Arial', 10))
        indications_GVS_text.grid(row = 5, column = 1)

        input_incications_GVS = Entry(frame)
        input_incications_GVS.grid(row = 5, column = 2)
        
    if EE_device == 1:
        indications_EE_text = Label(frame, text = 'Введите показания ЭЭ с дневной шкалы: ', font = ('Arial', 10))
        indications_EE_text.grid(row = 6, column = 1)

        input_indications_EE_daytime = Entry(frame)
        input_indications_EE_daytime.grid(row = 6, column = 2)

        indications_EE_text_2 = Label(frame, text = 'Введите показания ЭЭ с ночной шкалы: ', font = ('Arial', 10))
        indications_EE_text_2.grid(row = 7, column = 1)

        input_indications_EE_night = Entry(frame)
        input_indications_EE_night.grid(row = 7, column = 2)

    if condition_of_residents == 1:
        number_of_residents_text=Label(frame, text = 'Введите кол-во жильцов: ', font = ('Arial', 10))
        number_of_residents_text.grid(row = 8, column = 1)

        input_number_of_residents = Entry(frame)
        input_number_of_residents.grid(row = 8, column = 2)
        
    if condition_of_residents == 2:
        Number_residents(number_LS, request_date) #вытаскивает последнее число жильцов и вносит в базу

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
        for widget in frame.winfo_children():
            widget.destroy()
        third_page()

    input_buttion_2 = Button(frame,text = 'Ввести', command = Collecting_data_gui, height = 5, width = 20)
    input_buttion_2.grid(row = 10, column = 1)

#---------------------------------------------------------
#сохранение файла
def save():
    path = fd.askdirectory()
    os.chdir(path)
    path = path + '/receipt.xlsx'
    cl.receipt(EE_device, path)

#--------------------------------------------------------
def third_page():
    welcome_text = Label(frame, text = 'Начисления произведены!', font = ('Arial', 30)) 
    welcome_text.grid(row = 3, column = 1)

    hvs_text = Label(frame, text = 'ХВС: ', font = ('Arial', 10)  )
    hvs_text.grid(row = 4, column = 1)
    hvs_var=Label(frame, text = ("{:8.2f}".format(cl.accrual_HVS) + ' рублей!'), font = ('Arial', 10) )
    hvs_var.grid(row = 4, column = 2)

    gvs_text_1 = Label(frame, text = 'ГВС Теплоноситель: ', font = ('Arial', 10)  )
    gvs_text_1.grid(row = 5, column = 1)
    gvs_var_1 = Label(frame, text = ("{:8.2f}".format(cl.accrual_GVS_heat_carrier) + ' рублей!'), font = ('Arial', 10) )
    gvs_var_1.grid(row = 5, column = 2)

    gvs_text_2 = Label(frame, text = 'ГВС Тепловая энергия: ', font = ('Arial', 10)  )
    gvs_text_2.grid(row = 6, column = 1)
    gvs_var_2 = Label(frame, text = ("{:8.2f}".format(cl.accrual_GVS_thermal_energy) + ' рублей!'), font = ('Arial', 10) )
    gvs_var_2.grid(row = 6, column = 2)

    gvs_text_3 = Label(frame, text = 'ГВС Итого: ', font = ('Arial', 10)  )
    gvs_text_3.grid(row = 7, column = 1)
    gvs_var_3 = Label(frame, text = ("{:8.2f}".format(cl.accrual_GVS) + ' рублей!'), font = ('Arial', 10) )
    gvs_var_3.grid(row = 7, column = 2)

    ee_text = Label(frame, text = 'ЭЭ: ', font = ('Arial', 10)  )
    ee_text.grid(row = 8, column = 1)
    ee_var = Label(frame, text = ("{:8.2f}".format(cl.accrual_EE) + ' рублей!'), font = ('Arial', 10) )
    ee_var.grid(row = 8, column = 2)

    total_text = Label(frame, text = 'Итого: ', font = ('Arial', 10)  )
    total_text.grid(row = 9, column = 1)
    total_var = Label(frame, text = ("{:8.2f}".format(cl.total_accrual) + ' рублей!'), font = ('Arial', 10) )
    total_var.grid(row = 9, column = 2)

    buttion_save = Button(frame,text = 'Сохранить квитанцию', command = save, height = 5, width = 20)
    buttion_save.grid(row = 10, column = 1)

#главная функция для main
def manage():
    main_window()
    authorization()
    window.mainloop()

