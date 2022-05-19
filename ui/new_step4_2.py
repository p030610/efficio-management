from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import datetime

class New_step4_2(QWidget):
    def __init__(self,parent) : 
        super().__init__()
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.setWindowTitle("에피치오 업무 관리 프로그램")
        self.move(150,50)
        self.setFixedSize(1200,800)
        self.mainwindow = QVBoxLayout()
        self.dock_top = QHBoxLayout()
        self.content = QHBoxLayout()
        dock_right = QVBoxLayout()
        dock_left = QVBoxLayout()
        dock_button = QHBoxLayout()

        table_layout_1 = QVBoxLayout()
        table_layout_2 = QVBoxLayout()
        table_layout_3 = QVBoxLayout()

        label_company_list = QLabel("-기업 리스트")
        label_deadline_align = QLabel("-마감일 순")
        label_estimate_align = QLabel("-견적서 발행 순")

        table_company_list = QTableWidget()
        table_deadline_align = QTableWidget()
        table_estimate_align = QTableWidget()

        button_efficio = QPushButton("에피치오 홈")
        button_efficio.clicked.connect(self.parent.goto_home)

        self.label_info = QLabel("ID:담당자명")
        self.label_datetime = QLabel(datetime.datetime.today().strftime("%Y년 %m월 %d일")) 

        button_new = QPushButton("신규")
        button_new.clicked.connect(self.parent.new_clicked)
        button_in_progress = QPushButton("진행 중")
        button_in_progress.clicked.connect(self.parent.in_progress_clicked)
        button_complete = QPushButton("완료")
        button_complete.clicked.connect(self.parent.complete_clicked)
        button_current = QPushButton("현황")
        button_current.clicked.connect(self.parent.current_clicked)
        button_lecture = QPushButton("강의")
        button_lecture.clicked.connect(self.parent.lecture_clicked)
        button_settings = QPushButton("설정")
        button_settings.clicked.connect(self.parent.settings_clicked)

        dock_right.addWidget(self.label_info)
        dock_right.addWidget(self.label_datetime)
        dock_right.setContentsMargins(100,0,0,0)
        self.mainwindow.addLayout(self.dock_top)
        self.mainwindow.addLayout(self.content)
        self.mainwindow.setStretchFactor(self.content, 5)
        self.dock_top.addLayout(dock_left)
        self.dock_top.addLayout(dock_button)
        self.dock_top.addLayout(dock_right)
        dock_left.addWidget(button_efficio)
        dock_button.addWidget(button_new)
        dock_button.setContentsMargins(200,0,0,0)
        dock_button.addWidget(button_in_progress)
        dock_button.addWidget(button_complete)
        dock_button.addWidget(button_current)
        dock_button.addWidget(button_lecture)
        dock_button.addWidget(button_settings)
        self.content.addLayout(table_layout_1)
        self.content.addLayout(table_layout_2)
        self.content.addLayout(table_layout_3)

        table_layout_1.addWidget(label_company_list)
        table_layout_1.addWidget(table_company_list)
        table_layout_2.addWidget(label_deadline_align)
        table_layout_2.addWidget(table_deadline_align)
        table_layout_3.addWidget(label_estimate_align)
        table_layout_3.addWidget(table_estimate_align)

        self.setLayout(self.mainwindow)

