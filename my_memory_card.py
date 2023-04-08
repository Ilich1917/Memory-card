#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout
from random import shuffle, randint
class Question():
    def __init__(self, question_text, right_ansewer, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.right_ansewer = right_ansewer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#скрываем группу воросов,показываем группу результатов
def show_result():
    ansewer_group.hide()
    result_box.show()
    button.setText('Следующий вопрос')
def show_question():
    result_box.hide()
    ansewer_group.show()
    button.setText('Ответить') 
def click_ok():
    if button.text() == 'Ответить':
        check_ansewer()
    else:
        next_question()
def ask(q:Question):
    shuffle(ansewers)
    ansewers[0].setText(q.right_ansewer)
    ansewers[1].setText(q.wrong1)
    ansewers[2].setText(q.wrong2)
    ansewers[3].setText(q.wrong3)
    question.setText(q.question_text)
    right_ansewer.setText(q.right_ansewer)
    show_question()
def check_ansewer():
    if ansewers[0].isChecked():
        result_text.setText('Правильно')
        show_result()
        main_win.score += 1
    else:
        result_text.setText('Неравильно')
        show_result()
    print('Всего вопросов', main_win.total)
    print('Общий счёт', main_win.score)
    print('Рейтинг', main_win.score/main_win.total * 100)
def next_question():
    main_win.total += 1
    cur_question = randint(0, len(question_list)-1 ) 
    q=question_list[cur_question]
    ask(q)
#подписка к кнопке 


app = QApplication([])

main_win = QWidget()
main_win.total = 0
main_win.score = 0
question = QLabel('Вопрос')
button = QPushButton('Ответить')
ansewer_group = QGroupBox('Варианты ответов')
vline = QVBoxLayout()

main_win.setLayout(vline) #создание направляющей
main_win.resize(400, 300) #размер окна
main_win.setWindowTitle('Memory Card') #название окна
ansewer1 = QRadioButton('Вариант 1')
ansewer2 = QRadioButton('Вариант 2')
ansewer3 = QRadioButton('Вариант 3')
ansewer4 = QRadioButton('Вариант 4')
ansewers = [ansewer1, ansewer2, ansewer3, ansewer4]

v1 = QVBoxLayout()
v1.addWidget(ansewer1)
v1.addWidget(ansewer2)
v2 = QVBoxLayout()
v2.addWidget(ansewer3)
v2.addWidget(ansewer4)
h = QHBoxLayout()
h.addLayout(v1)
h.addLayout(v2)
ansewer_group.setLayout(h)
result_box = QGroupBox('Результат:')
result_text = QLabel('Правильно/неправильно')
right_ansewer = QLabel('Верный ответ')
v3 = QVBoxLayout()
v3.addWidget(result_text)
v3.addWidget(right_ansewer)
result_box.setLayout(v3)


#привязываем главные направляющие(вопрос, две группы)
vline.addWidget(question, alignment = Qt.AlignCenter)
vline.addWidget(ansewer_group)
vline.addWidget(result_box)
vline.addWidget(button)
#спрятать группу с вариантами ответов
result_box.hide()

button.clicked.connect(click_ok)
question1 = Question('Кто не обитает в озере?','Щука', 'Язь', 'Рак','Карась')
question2 = Question('Излюбленный трофей рыбаков ', 'Сазан', 'Пелядь', 'Чебак','Пескарь')
question3 = Question('Легенда гачи', 'Билли Херингтон','Марк Вульф','Дядя Богдан','Вэн Даркхом')
question4 = Question('Где любит собираться крупная рыба в водоёме днём?', 'Омут', 'Мелководие', 'Возле берега', 'Возле камышей')
question5 = Question('Запрещённый вид ловли рыбы', 'Паук', 'Удочка', 'Закидушка','Спиннинг')
question6 = Question('Какая река впадает в бассейн Северного ледовитого океана?', 'Обь', 'Иртыш', 'Волга', 'Енисей')
question7 = Question('С помощью чего ловят рыбу на мелководии?', 'Острога','Удочка', 'Копьё', 'Спиннинг')
question8 = Question('Какое дно для обитания предпочитает рыба судак?', 'Песчаное','Илистое','Каменное','Глинястое')
question9 = Question('Who is the boy next door?', 'Van','uncle Bogdan','Billy','Steve')
question10 = Question('The last soviet union OBT', 'T-90','T-80','T-72б3','Gvozdika')
question_list=[question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
main_win.curquestion = - 1
next_question()
main_win.show()
app.exec_()

