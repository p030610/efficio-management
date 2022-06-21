from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import datetime

class New_step1_4(QWidget):
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
        content_xlsx = QHBoxLayout()
        content_right = QVBoxLayout()
        layout_content_right_button = QHBoxLayout()

        layout_content_right_1_1 = QHBoxLayout()
        layout_content_right_1_2 = QHBoxLayout()
        layout_content_right_2_1 = QHBoxLayout()
        layout_content_right_2_2 = QHBoxLayout()

        self.layout_info = QHBoxLayout()

        self.money_info = QVBoxLayout()

        self.money_1 = QHBoxLayout()
        self.money_2 = QHBoxLayout()
        self.money_3 = QHBoxLayout()

        self.money_info.addLayout(self.money_1)
        self.money_info.addLayout(self.money_2)
        self.money_info.addLayout(self.money_3)

        label_money_1 = QLabel("선금")
        label_money_2 = QLabel("중도금")
        label_money_3 = QLabel("잔금")

        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)

        self.webView.setFixedHeight(700)

        self.input_money_1_1 = QLineEdit()
        self.input_money_1_1.setPlaceholderText("%")
        self.input_money_1_2 = QLineEdit()
        self.input_money_1_2.setPlaceholderText("원")
        self.input_money_1_3 = QLineEdit()
        self.input_money_1_3.setPlaceholderText("yyyy-mm-dd")

        self.input_money_2_1 = QLineEdit()
        self.input_money_2_1.setPlaceholderText("%")
        self.input_money_2_2 = QLineEdit()
        self.input_money_2_2.setPlaceholderText("원")
        self.input_money_2_3 = QLineEdit()
        self.input_money_2_3.setPlaceholderText("yyyy-mm-dd")

        self.input_money_3_1 = QLineEdit()
        self.input_money_3_1.setPlaceholderText("%")
        self.input_money_3_2 = QLineEdit()
        self.input_money_3_2.setPlaceholderText("원")
        self.input_money_3_3 = QLineEdit()
        self.input_money_3_3.setPlaceholderText("yyyy-mm-dd")

        self.money_1.addWidget(label_money_1)
        self.money_1.addWidget(self.input_money_1_1)
        self.money_1.addWidget(self.input_money_1_2)
        self.money_1.addWidget(self.input_money_1_3)

        self.money_2.addWidget(label_money_2)
        self.money_2.addWidget(self.input_money_2_1)
        self.money_2.addWidget(self.input_money_2_2)
        self.money_2.addWidget(self.input_money_2_3)

        self.money_3.addWidget(label_money_3)
        self.money_3.addWidget(self.input_money_3_1)
        self.money_3.addWidget(self.input_money_3_2)
        self.money_3.addWidget(self.input_money_3_3)

        self.table_estimate = QTableWidget()

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

        label_content_right_1 = QLabel("[견적서]")
        label_content_right_2 = QLabel("[세금 계산서]")

        self.label_content_right_1_1 = QLabel("1. 입금 확인")
        self.label_content_right_1_2 = QLabel("2. 입금 내역")

        self.button_content_right_1_1_o = QPushButton("O")
        self.button_content_right_1_1_o.clicked.connect(self.parent.new_step_1_4_1_o_clicked)
        self.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_1_1_x = QPushButton("X")
        self.button_content_right_1_1_x.clicked.connect(self.parent.new_step_1_4_1_x_clicked)
        self.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: yellow;}')

        button_previous = QPushButton("이전")
        button_previous.clicked.connect(self.parent.open_new_step_1_3)
        button_save = QPushButton("저장")
        button_save.clicked.connect(self.parent.save_new_step_1_4)
        button_next = QPushButton("다음")
        button_next.clicked.connect(self.parent.open_new_step_1_5)

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

        self.content.addLayout(content_xlsx)
        self.content.addLayout(content_right)

        content_right.addLayout(layout_content_right_1_1)
        content_right.addLayout(layout_content_right_1_2)

        content_right.addLayout(layout_content_right_2_1)
        content_right.addLayout(layout_content_right_2_2)
        content_right.addLayout(layout_content_right_button)

        content_right.setContentsMargins(0,150,0,150)

        layout_content_right_button.addWidget(button_previous)
        layout_content_right_button.addWidget(button_save)
        layout_content_right_button.addWidget(button_next)

        layout_content_right_1_1.addWidget(self.label_content_right_1_1)
        layout_content_right_1_1.addWidget(self.button_content_right_1_1_o)
        layout_content_right_1_1.addWidget(self.button_content_right_1_1_x)

        layout_content_right_1_2.addWidget(self.label_content_right_1_2)

        layout_content_right_2_1.addLayout(self.money_info)

        content_xlsx.addWidget(self.webView)

        self.setLayout(self.mainwindow)