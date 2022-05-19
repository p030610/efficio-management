from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import datetime

class Loginpage(QWidget):

    def __init__(self,parent) : 
        super().__init__()
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.setWindowTitle("에피치오 업무 관리 프로그램")
        self.move(100, 100)
        self.setFixedSize(640, 480)

        mainlayout = QVBoxLayout()
        upper_dock = QHBoxLayout()
        content = QVBoxLayout()
        button_layout = QHBoxLayout()
        dock_right = QVBoxLayout()

        button_efficio = QLabel("에피치오")
        # button_efficio.clicked.connect(self.parent.goto_home)

        button_login = QPushButton("로그인")
        button_register = QPushButton("회원가입")
        button_register.clicked.connect(self.parent.register)

        button_find_id = QPushButton("아이디찾기")
        button_find_pw = QPushButton("비밀번호찾기")
        button_find_id.clicked.connect(self.parent.find_id)
        button_find_pw.clicked.connect(self.parent.find_pw)

        label_info = QLabel("ID:담당자명")
        label_datetime = QLabel(datetime.datetime.today().strftime("%Y년 %m월 %d일")) 


        self.input_id = QLineEdit()
        self.input_pw = QLineEdit()
        self.input_id.setPlaceholderText("아이디")
        self.input_pw.setPlaceholderText("비밀번호")

        dock_right.addWidget(label_info)
        dock_right.addWidget(label_datetime)
        mainlayout.addLayout(upper_dock)
        mainlayout.addLayout(content)
        content.addWidget(self.input_id)
        content.addWidget(self.input_pw)
        content.addLayout(button_layout)
        content.setStretchFactor(button_layout,5)
        mainlayout.setStretchFactor(content, 5)
        upper_dock.addWidget(button_efficio)

        upper_dock.addLayout(dock_right)
        button_efficio.resize(80,50)
        upper_dock.setStretchFactor(dock_right, -1)
        button_layout.addWidget(button_login)
        button_layout.addWidget(button_find_id)
        button_layout.addWidget(button_find_pw)
        button_layout.addWidget(button_register)
        content.setContentsMargins(100,50,100,200)

        button_login.clicked.connect(lambda : self.parent.login(self,self.input_id.text(),self.input_pw.text()))

        self.setLayout(mainlayout)
    

