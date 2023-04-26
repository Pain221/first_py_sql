import connections as cn
import gui_tkinter as gui


#коннект и курсор
cn.connection_open()

#вся работа
gui.manage()

#закрытие коннекта и курсора
cn.connection_close()

