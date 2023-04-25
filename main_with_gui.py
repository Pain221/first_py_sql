import connections as cn
import gui_tkinter as gui
import calculations_with_gui as cl

#коннект и курсор
cn.connection_open()

#запуск интерфейса, сбор и внесение показаний в базу
gui.first_page()

cn.connection_close()

