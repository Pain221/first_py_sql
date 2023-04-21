from PyQt6 import QtWidgets
import sys 

app=QtWidgets.QApplication(sys.argv) #создание приложения, "sys.argv, чтобы разрешить аргументы командной строки для приложения"

window=QtWidgets.QWidget() #создание окна
window.setWindowTitle("Показания счётчиков онлайн") #заголовок окна
window.resize(800,600) #размеры клиентской области

label=QtWidgets.QLabel("<center> <strong> <h1> Добро пожаловать! </center> </strong> </h1>") #создание надписи, можно использовать html теги и css атрибуты
buttion_Quit=QtWidgets.QPushButton("Выйти") #создание кнопки

vbox=QtWidgets.QVBoxLayout() #вертикальный контейнер, в котором в порядке добавяления появляются элементы

#добавление элементов в контейнер
vbox.addWidget(label)
vbox.addWidget(buttion_Quit)

window.setLayout(vbox) #добавление контейнера в окно

buttion_Quit.clicked.connect(app.quit) #при нажатии кнопки - выход из приложения

window.show()
app.exec() #бесконечный цикл обработки событий в приложении
