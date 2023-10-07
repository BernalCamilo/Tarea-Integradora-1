import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QLabel,QLineEdit
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QSize
from story_controller import StoryController
from PyQt5.QtCore import Qt,QUrl
import PyQt5.QtMultimedia as mm


import textwrap



class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = StoryController()
        self.transitions = self.controller.get_transitions()
        self.ans = ""
        self.vbox = QVBoxLayout()
        self.setGeometry(50, 50, 1200, 1200)
        self.setWindowTitle('PyQt5 App')
        self.showMaximized()
        self.setup_audio()
        self.get_username()

    def restart(self):
        self.controller = StoryController()
        self.refresh_ui()
        self.get_username()




    def setup_audio(self):
        self.player = mm.QMediaPlayer()
        self.player.setMedia(mm.QMediaContent(QUrl.fromLocalFile("./resources/sounds/zombies.mp3")))
        self.player.play()

    def get_username(self):

        self.refresh_ui()


        usernameLabel = QLabel("Nombre de usuario:")
        usernameLabel.setFont(QFont('Arial', 20))

        self.usernameLineEdit = QLineEdit()
        self.usernameLineEdit.setFixedWidth(500)
        self.usernameLineEdit.setFixedHeight(150)


        startButton = QPushButton("Comenzar")

        startButton.clicked.connect(self.initUI)
        startButton.setFixedHeight(150)
        startButton.setFixedWidth(500)


        self.vbox.addWidget(usernameLabel,alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.usernameLineEdit,alignment=Qt.AlignCenter)
        self.vbox.addWidget(startButton,alignment=Qt.AlignCenter)

        self.vbox.setSpacing(0)
        self.setLayout(self.vbox)








    def initUI(self):

        username = self.usernameLineEdit.text()


        if self.controller.validate_username(username):

            self.controller.user_name = username
        
            self.refresh_ui()
            text = self.controller.get_story_state(0)
            text = self.controller.transduce_text(text) 
            label = QLabel(text)
            self.vbox.addWidget(label, alignment=Qt.AlignCenter)
            
            if(self.controller.validate_transitons()):

                self.configure_options()
        else:
            self.get_username()


    def configure_options(self):



        # Transitions
        self.transitions = self.controller.get_transitions()

        if not self.transitions:


            if (self.controller.nfa.accepts(self.ans)):
                label = QLabel('FELICIDADES, HAS SOBREVIVIDO')

                restart = QPushButton("Reiniciar")
                restart.clicked.connect(self.restart)
                restart.setFixedHeight(150)
                restart.setFixedWidth(500)


                close = QPushButton("Cerrar")
                close.clicked.connect(self.close_app)
                close.setFixedHeight(150)
                close.setFixedWidth(500)

                self.vbox.addWidget(label, alignment=Qt.AlignCenter)
                self.vbox.addWidget(restart, alignment=Qt.AlignCenter)
                self.vbox.addWidget(close, alignment=Qt.AlignCenter)
            else:
                label = QLabel('ESTAS MUERTO!!!!')

                restart = QPushButton("Reiniciar")
                restart.clicked.connect(self.restart)
                restart.setFixedHeight(150)
                restart.setFixedWidth(500)


                close = QPushButton("Cerrar")
                close.clicked.connect(self.close_app)
                close.setFixedHeight(150)
                close.setFixedWidth(500)

                self.vbox.addWidget(label, alignment=Qt.AlignCenter)
                self.vbox.addWidget(restart, alignment=Qt.AlignCenter)
                self.vbox.addWidget(close, alignment=Qt.AlignCenter)

    

            
        elif len(self.transitions) == 2:
            states = []
            states_id = []
            for idx, next_state in enumerate(self.transitions):
                states_id.append(next_state)
                states.append(self.controller.get_story_state(next_state))

            self.setup_buttons(states,states_id)

        else:
            states = []
            states_id = []
            for idx, next_state in enumerate(self.transitions):
                states_id.append(next_state)
                states.append(self.controller.get_story_state(next_state))
            
            self.setup_buttons(states,states_id)
        


    def setup_buttons(self,states,states_id):
        

            if len(states) == 2:
                #Resources button 1
                text_bnt1 = states[0]
                text_bnt1 = self.controller.transduce_text(text_bnt1)
                text_bnt1 = textwrap.fill(text_bnt1, 80)

                img1_path = './resources/img/q'+str(states_id[0])+'.png'

                btn1 = QPushButton(text_bnt1, self)
                btn1.setFixedHeight(350)
                btn1.setFixedWidth(980)
                img1 = QIcon(img1_path)  
                btn1.setIcon(img1)
                btn1.setIconSize(QSize(300, 300))
                btn1.clicked.connect(self.option_0)
                self.vbox.addWidget(btn1,alignment=Qt.AlignCenter)

                #Resources button 2
                text_bnt2 = states[1]
                text_bnt2 = self.controller.transduce_text(text_bnt2)

                text_bnt2 = textwrap.fill(text_bnt2, 80)
                img2_path = './resources/img/q'+str(states_id[1])+'.png'
                btn2 = QPushButton(text_bnt2,self)
                btn2.setFixedHeight(350)

                btn2.setFixedWidth(980)

                img2 = QIcon(img2_path)  
                btn2.setIcon(img2)
                btn2.setIconSize(QSize(300, 300))
                btn2.clicked.connect(self.option_1)
                self.vbox.addWidget(btn2,alignment=Qt.AlignCenter)
            else:
                text_bnt1 = states[0]
                text_bnt1 = self.controller.transduce_text(text_bnt1)
                text_bnt1 = textwrap.fill(text_bnt1, 80)

                img1_path = './resources/img/q'+str(states_id[0])+'.png'

                btn1 = QPushButton(text_bnt1, self)
                btn1.setFixedHeight(350)
                btn1.setFixedWidth(980)

                img1 = QIcon(img1_path)  
                btn1.setIcon(img1)
                btn1.setIconSize(QSize(300, 300))
                btn1.clicked.connect(self.option_0)
                self.vbox.addWidget(btn1,alignment=Qt.AlignCenter)


    def refresh_ui(self):
        for i in reversed(range(self.vbox.count())): 
            self.vbox.itemAt(i).widget().setParent(None)

    def option_0(self):
        
        self.refresh_ui()
        next_state = self.transitions[0]
        self.ans = self.ans + str(0)
        self.controller.current_position = next_state
        self.configure_options()

    def option_1(self):
        self.refresh_ui()
        next_state = self.transitions[1]
        self.ans = self.ans + str(1)
        self.controller.current_position = next_state
        self.configure_options()
   
    def close_app(self):
        QApplication.close()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())