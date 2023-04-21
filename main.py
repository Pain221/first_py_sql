import prototype as pt
import calculations as cl
import connections as cn

#коннект и курсор
cn.connection_open()

#сбор показаний и занесение в базу
pt.activation()

#выполнение вычислений
cl.activate_calculations()

#закрытие коннекта и курсора
cn.connection_close()

