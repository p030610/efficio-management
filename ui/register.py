from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import datetime

from pkg_resources import register_loader_type

class Register(QWidget):
    def __init__(self,parent) : 
        super().__init__()
        self.parent = parent
        self.initUI()
        self.id_is_unique = False


    def initUI(self):
        
        
        self.setWindowTitle("에피치오 업무 관리 프로그램")
        self.move(100, 100)
        self.setFixedSize(1280, 800)

        mainlayout = QVBoxLayout()
        upper_dock = QHBoxLayout()
        content = QHBoxLayout()
        content_left = QVBoxLayout()
        content_right = QVBoxLayout()
        dock_right = QVBoxLayout()
        register_layout = QVBoxLayout()
        register_button_layout = QHBoxLayout()
        layout_id = QHBoxLayout()

        button_id = QPushButton("중복확인")

        button_id.clicked.connect(self.parent.inspect_id)

        button_efficio = QLabel("에피치오")

        label_info = QLabel("ID:담당자명")
        label_datetime = QLabel(datetime.datetime.today().strftime("%Y년 %m월 %d일")) 

        label_register = QLabel("-회원가입")

        self.line_name = QLineEdit()
        self.line_name.setPlaceholderText("이름")

        self.line_phone = QLineEdit()
        self.line_phone.setPlaceholderText("연락처")

        self.line_id = QLineEdit()
        self.line_id.setPlaceholderText("id")

        self.line_pw = QLineEdit()
        self.line_pw.setPlaceholderText("pw")

        self.line_pw_confirm = QLineEdit()
        self.line_pw_confirm.setPlaceholderText("pw확인")

        self.line_position = QLineEdit()
        self.line_position.setPlaceholderText("부서")

        self.line_level = QLineEdit()
        self.line_level.setPlaceholderText("직급")

        button_register = QPushButton("가입 완료")
        button_cancel = QPushButton("취소")

        label_register2 = QLabel("-회원가입")


        dock_right.addWidget(label_info)
        dock_right.addWidget(label_datetime)
        dock_right.setContentsMargins(400,0,0,0)

        upper_dock.addWidget(button_efficio)

        upper_dock.addLayout(dock_right)
        button_efficio.resize(80,50)
        upper_dock.setStretchFactor(dock_right, -1)

        content.addLayout(content_left)
        content.addLayout(content_right)

        content_left.addWidget(label_register)

        content_left.setContentsMargins(0,0,0,250)

        # content_left.

        content_right.addWidget(label_register2)
        content_right.addLayout(register_layout)

        content_right.setContentsMargins(300,0,300,0)

        content.setContentsMargins(0,100,0,300)

        register_layout.addWidget(self.line_name)
        register_layout.addWidget(self.line_phone)
        register_layout.addLayout(layout_id)
        
        layout_id.addWidget(self.line_id)
        layout_id.addWidget(button_id)

        register_layout.addWidget(self.line_pw)
        register_layout.addWidget(self.line_pw_confirm)
        register_layout.addWidget(self.line_position)
        register_layout.addWidget(self.line_level)

        register_layout.addLayout(register_button_layout)

        register_button_layout.addWidget(button_register)
        register_button_layout.addWidget(button_cancel)

        mainlayout.addLayout(upper_dock)
        mainlayout.addLayout(content)

        self.setLayout(mainlayout)

        button_register.clicked.connect(self.register)

    def register(self) :
        if self.id_is_unique == True : 
            if self.line_name.text() != "" and self.line_id.text() != "" and self.line_pw.text() != "" and self.line_phone.text() != "" and self.line_position.text() != "" and self.line_level.text() != "" and self.line_pw.text() == self.line_pw_confirm.text(): 

                self.parent.register_confirmed()

            else : 
                QMessageBox.warning(self,'경고','계정정보를 다시 확인해주세요')
        else : 
            QMessageBox.warning(self,'경고','중복확인을 해주세요')
