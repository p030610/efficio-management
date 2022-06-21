from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import datetime

class Mainwindow(QWidget):
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

        self.table_layout_1 = QVBoxLayout()
        self.table_layout_2 = QVBoxLayout()
        self.table_layout_3 = QVBoxLayout()

        search_layout_1 = QHBoxLayout()
        search_layout_2 = QHBoxLayout()
        search_layout_3 = QHBoxLayout()
        
        self.layout_info = QHBoxLayout()

        label_company_list = QLabel("-기업 리스트")
        label_deadline_align = QLabel("-마감일 순")
        label_estimate_align = QLabel("-견적서 발행 순")

        self.table_company_list = QTableWidget()
        self.table_deadline_align = QTableWidget()
        self.table_estimate_align = QTableWidget()

        button_efficio = QPushButton("에피치오 홈")
        button_efficio.clicked.connect(self.parent.goto_home)

        self.label_info = QLabel("ID:담당자명")
        self.label_notice = QPushButton("알림 없음")
        self.label_notice.setStyleSheet("background-color: yellow")
        self.label_notice.clicked.connect(self.parent.open_notice)
        self.label_datetime = QLabel(datetime.datetime.today().strftime("%Y년 %m월 %d일")) 

        button_new = QPushButton("신규")
        button_new.clicked.connect(self.parent.new_clicked)
        button_in_progress = QPushButton("진행 중")
        button_in_progress.clicked.connect(self.parent.in_progress_clicked)
        button_complete = QPushButton("완료")
        button_complete.clicked.connect(self.parent.complete_clicked)
        button_current = QPushButton("기업 리스트")
        button_current.clicked.connect(self.parent.company_list_clicked)
        button_lecture = QPushButton("강의")
        button_lecture.clicked.connect(self.parent.lecture_clicked)
        button_settings = QPushButton("설정")
        button_settings.clicked.connect(self.parent.settings_clicked)

        self.line_search_1 = QLineEdit()
        self.line_search_1.setPlaceholderText("검색")
        button_search_1 = QPushButton("검색")
        button_search_1.clicked.connect(self.parent.mainwindow_search_1)

        self.line_search_2 = QLineEdit()
        self.line_search_2.setPlaceholderText("검색")
        button_search_2 = QPushButton("검색")
        button_search_2.clicked.connect(self.parent.mainwindow_search_2)

        self.line_search_3 = QLineEdit()
        self.line_search_3.setPlaceholderText("검색")
        button_search_3 = QPushButton("검색")
        button_search_3.clicked.connect(self.parent.mainwindow_search_3)

        self.table_company_list.clicked.connect(self.parent.mainwindow_table_1_clicked)
        self.table_deadline_align.clicked.connect(self.parent.mainwindow_table_2_clicked)
        self.table_estimate_align.clicked.connect(self.parent.mainwindow_table_3_clicked)

        self.table_company_list.setColumnCount(6)

        self.table_deadline_align.setColumnCount(6)

        self.table_estimate_align.setColumnCount(6)

        self.table_company_list.setHorizontalHeaderLabels(["기업명","대표자명","연락처","잔금","비고", "고유번호"])
        self.table_deadline_align.setHorizontalHeaderLabels(["마감일","기업명","서비스명","남은수량","전체수량", "고유번호"])
        self.table_estimate_align.setHorizontalHeaderLabels(["마감일","기업명","대표자명","남은수량","전체수량", "고유번호"])

        search_layout_1.addWidget(self.line_search_1)
        search_layout_1.addWidget(button_search_1)

        search_layout_2.addWidget(self.line_search_2)
        search_layout_2.addWidget(button_search_2)

        search_layout_3.addWidget(self.line_search_3)
        search_layout_3.addWidget(button_search_3)
        
        dock_right.addLayout(self.layout_info)
        self.layout_info.addWidget(self.label_notice)
        self.layout_info.addWidget(self.label_info)
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
        self.content.addLayout(self.table_layout_1)
        self.content.addLayout(self.table_layout_2)
        self.content.addLayout(self.table_layout_3)

        self.table_layout_1.addWidget(label_company_list)
        self.table_layout_1.addLayout(search_layout_1)
        self.table_layout_1.addWidget(self.table_company_list)
        self.table_layout_2.addWidget(label_deadline_align)
        self.table_layout_2.addLayout(search_layout_2)
        self.table_layout_2.addWidget(self.table_deadline_align)
        self.table_layout_3.addWidget(label_estimate_align)
        self.table_layout_3.addLayout(search_layout_3)
        self.table_layout_3.addWidget(self.table_estimate_align)

        self.setLayout(self.mainwindow)


