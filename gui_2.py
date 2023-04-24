from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Показания счётчиков онлайн")
window.geometry('800x650')

frame=Frame(window, padx=100, pady=100) #контейнер 
frame.pack(expand=True) #включена возможность заполнения

#создание первого фрейма
def first_frame():
    welcome_text=Label(frame, text='Добро пожаловать!', font=('Arial', 30)) 
    welcome_text.grid(row=3, column=1)

    LS_text=Label(frame, text='Номер лицевого счета : ', font=('Arial', 10))
    LS_text.grid(row=4, column=1)

    input_LS=Entry(frame)
    input_LS.grid(row=4, column=2)
    input_LS.focus()

    condition_of_residents_text1=Label(frame, text='Количество проживающих менялось?', font=('Arial', 10))
    condition_of_residents_text1.grid(row=5, column=1)
    condition_of_residents_text2=Label(frame, text='(Введите ДА или НЕТ, если заполняете впервые - введие ДА) ', font=('Arial', 8))
    condition_of_residents_text2.grid(row=6, column=1)

    input_condition_of_residents=Entry(frame)
    input_condition_of_residents.grid(row=5, column=2)

    HVS_device_text=Label(frame, text='Есть ли у вас прибор учета ХВС?(введите ДА или НЕТ)',  font=('Arial', 10) )
    HVS_device_text.grid(row=7, column=1)

    input_HVS_device=Entry(frame)
    input_HVS_device.grid(row=7, column=2)

    GVS_device_text=Label(frame, text='Есть ли у вас прибор учета ГВС?(введите ДА или НЕТ)',  font=('Arial', 10) )
    GVS_device_text.grid(row=8, column=1)

    input_GVS_device=Entry(frame)
    input_GVS_device.grid(row=8, column=2)

    EE_device_text=Label(frame, text='Есть ли у вас прибор учета ЭЭ?(введите ДА или НЕТ)',  font=('Arial', 10) )
    EE_device_text.grid(row=9, column=1)

    input_EE_device=Entry(frame)
    input_EE_device.grid(row=9, column=2)

    #обработка ввода
    def Input_process():
        global number_LS,condition_of_residents, HVS_device, GVS_device, EE_device
        number_LS=int(input_LS.get())
        condition_of_residents=str(input_condition_of_residents.get())
        HVS_device=str(input_HVS_device.get())
        GVS_device=str(input_GVS_device.get())
        EE_device=str(input_EE_device.get())
        messagebox.showinfo('ТЕСТ', f"{number_LS, HVS_device, GVS_device, EE_device, condition_of_residents} ") #ПОСЛЕ ТЕСТОВ УДАЛИТЬ 
        for widget in frame.winfo_children():
            widget.destroy()
        second_frame()
        

    input_buttion=Button(frame,text='Ввести', command=Input_process)
    input_buttion.grid(row=10, column=1)

def second_frame():
    welcome_text_1=Label(frame, text='Сбор показаний', font=('Arial', 30)) 
    welcome_text_1.grid(row=3, column=1)

    def Collecting_data():
        if HVS_device == "ДА":
            indications_HVS_text=Label(frame, text='Введите показания ХВС: ', font=('Arial', 10))
            indications_HVS_text.grid(row=4, column=1)

            input_incications_HVS=Entry(frame)
            input_incications_HVS.grid(row=4, column=2)

        if GVS_device == "ДА":
            indications_GVS_text=Label(frame, text='Введите показания ХВС: ', font=('Arial', 10))
            indications_GVS_text.grid(row=5, column=1)

            input_incications_GVS=Entry(frame)
            input_incications_GVS.grid(row=5, column=2)
        
        if EE_device == "ДА":
            indications_EE_text=Label(frame, text='Введите показания ХВС: ', font=('Arial', 10))
            indications_EE_text.grid(row=6, column=1)

            input_incications_EE=Entry(frame)
            input_incications_EE.grid(row=6, column=2)
        
        if condition_of_residents == "ДА":
            number_of_residents_text=Label(frame, text='Введите показания ХВС: ', font=('Arial', 10))
            number_of_residents_text.grid(row=7, column=1)

            input_number_of_residents=Entry(frame)
            input_number_of_residents.grid(row=7, column=2)
        
        #if condition_of_residents == "НЕТ":

        Collecting_data()
        

first_frame()

window.mainloop()


