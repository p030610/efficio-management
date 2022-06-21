from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


import datetime

class New_step1_3(QWidget):
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

        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)

        self.webView.setFixedHeight(700)

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

        self.label_content_right_1_1 = QLabel("1. [기업명] 견적서를 발송했나요?")
        self.label_content_right_1_2 = QLabel("2. [기업명] 견적서를 최종 검토가 완료되었을까요?")

        self.label_content_right_2_1 = QLabel("3. [기업명] 세금계산서 여부")
        self.label_content_right_2_2 = QLabel("4. [기업명] 세금계산서 발행 날짜")

        self.button_content_right_1_1_o = QPushButton("O")
        self.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_1_1_o.clicked.connect(self.parent.new_step_1_3_1_o_clicked)
        self.button_content_right_1_1_x = QPushButton("X")
        self.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_1_1_x.clicked.connect(self.parent.new_step_1_3_1_x_clicked)

        self.button_content_right_1_2_o = QPushButton("O")
        self.button_content_right_1_2_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_1_2_o.clicked.connect(self.parent.new_step_1_3_2_o_clicked)
        self.button_content_right_1_2_x = QPushButton("X")
        self.button_content_right_1_2_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_1_2_x.clicked.connect(self.parent.new_step_1_3_2_x_clicked)

        self.button_content_right_2_1_o = QPushButton("O")
        self.button_content_right_2_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_2_1_o.clicked.connect(self.parent.new_step_1_3_3_o_clicked)
        self.button_content_right_2_1_x = QPushButton("X")
        self.button_content_right_2_1_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_2_1_x.clicked.connect(self.parent.new_step_1_3_3_x_clicked)

        self.button_content_right_2_2_calendar = QPushButton("입력한 날짜 저장")
        self.button_content_right_2_2_calendar.setStyleSheet('QPushButton {background-color: yellow;}')
        self.button_content_right_1_1_o.clicked.connect(self.parent.new_step_1_3_4_calendar_clicked)

        self.label_content_right_2_2_calendar = QLineEdit()
        self.label_content_right_2_2_calendar.setPlaceholderText("yyyy-mm-dd")

        button_previous = QPushButton("이전")
        button_previous.clicked.connect(self.parent.open_new_step_1_2)
        button_save = QPushButton("저장")
        button_save.clicked.connect(self.parent.save_new_step_1_3)
        button_next = QPushButton("다음")
        button_next.clicked.connect(self.parent.open_new_step_1_4)

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

        content_right.setContentsMargins(0,150,0,150)

        content_right.addWidget(label_content_right_1)
        content_right.addLayout(layout_content_right_1_1)
        content_right.addLayout(layout_content_right_1_2)
        content_right.addWidget(label_content_right_2)
        content_right.addLayout(layout_content_right_2_1)
        content_right.addLayout(layout_content_right_2_2)
        content_right.addLayout(layout_content_right_button)

        layout_content_right_button.addWidget(button_previous)
        layout_content_right_button.addWidget(button_save)
        layout_content_right_button.addWidget(button_next)

        layout_content_right_1_1.addWidget(self.label_content_right_1_1)
        layout_content_right_1_1.addWidget(self.button_content_right_1_1_o)
        layout_content_right_1_1.addWidget(self.button_content_right_1_1_x)

        layout_content_right_1_2.addWidget(self.label_content_right_1_2)
        layout_content_right_1_2.addWidget(self.button_content_right_1_2_o)
        layout_content_right_1_2.addWidget(self.button_content_right_1_2_x)

        layout_content_right_2_1.addWidget(self.label_content_right_2_1)
        layout_content_right_2_1.addWidget(self.button_content_right_2_1_o)
        layout_content_right_2_1.addWidget(self.button_content_right_2_1_x)

        layout_content_right_2_2.addWidget(self.label_content_right_2_2)
        layout_content_right_2_2.addWidget(self.button_content_right_2_2_calendar)
        layout_content_right_2_2.addWidget(self.label_content_right_2_2_calendar)

        content_xlsx.addWidget(self.webView)

        self.setLayout(self.mainwindow)