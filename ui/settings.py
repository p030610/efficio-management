#담당자 이름 가지고있는 기업 표에 출력
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime

class Settings(QWidget):
    def __init__(self,parent) : 
        super().__init__()
        self.parent = parent
        self.initUI()

        self.settings_split = False
        self.in_progress_split = False

    def initUI(self):
        self.setWindowTitle("에피치오 업무 관리 프로그램")
        self.move(150,50)
        self.setFixedSize(1200,800)
        self.mainwindow = QVBoxLayout()
        self.dock_top = QHBoxLayout()
        self.content = QHBoxLayout()
        dock_right = QVBoxLayout()
        dock_left = QVBoxLayout()
        self.content_left = QVBoxLayout()
        content_right = QVBoxLayout()
        content_right_top = QHBoxLayout()
        search_layout_1 = QHBoxLayout()

        self.layout_info = QHBoxLayout()

        self.line_search_1 = QLineEdit()
        self.line_search_1.setPlaceholderText("검색")
        button_search_1 = QPushButton("검색")
        button_search_1.clicked.connect(self.parent.in_progress_search)

        button_efficio = QPushButton("efficio")
        button_efficio.clicked.connect(self.parent.goto_home)

        self.label_notice = QPushButton("알림 없음")
        self.label_notice.setStyleSheet("background-color: yellow")
        self.label_notice.clicked.connect(self.parent.open_notice)
        self.label_datetime = QLabel(datetime.datetime.today().strftime("%Y년 %m월 %d일")) 

        self.label_info = QLabel("ID:담당자명")
        self.label_datetime = QLabel(datetime.datetime.today().strftime("%Y년 %m월 %d일")) 
        self.table_label = QLabel("-사용자 목록")

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["이름", "아이디", "부서", "직급", "권한", "가입일", "최종 수정 날짜", '내역 다운'])

        self.table.setColumnWidth(0,int(self.table.width()/8))
        self.table.setColumnWidth(1,int(self.table.width()/8))
        self.table.setColumnWidth(2,int(self.table.width()/8))
        self.table.setColumnWidth(3,int(self.table.width()/8))
        self.table.setColumnWidth(4,int(self.table.width()/8))
        self.table.setColumnWidth(5,int(self.table.width()/8))
        self.table.setColumnWidth(6,int(self.table.width()/8))
        self.table.setColumnWidth(7,int(self.table.width()/8))

        button_new = QPushButton("-신규")
        button_new.clicked.connect(self.parent.new_clicked)
        button_new.setFont(QFont('맑은 고딕', 16))
        button_in_progress = QPushButton("-진행 중")#드롭다운 버튼
        button_in_progress.clicked.connect(self.split_in_progress)
        button_in_progress.setFont(QFont('맑은 고딕', 16))

        button_complete = QPushButton("-완료")
        button_complete.setFont(QFont('맑은 고딕', 16))
        button_complete.clicked.connect(self.parent.complete_clicked)
        button_current = QPushButton("-기업 리스트")
        button_current.setFont(QFont('맑은 고딕', 16))
        
        button_lecture = QPushButton("-강의")
        button_lecture.setFont(QFont('맑은 고딕', 16))
        button_lecture.clicked.connect(self.parent.lecture_clicked)
        button_settings = QPushButton("-설정")
        button_settings.clicked.connect(self.split_settings)
        button_settings.setFont(QFont('맑은 고딕', 16))

        
        self.button_settings_1 = QPushButton("-사용자 목록")
        self.button_settings_1.setContentsMargins(50,0,0,0)
        self.button_settings_1.clicked.connect(self.parent.open_settings_1)

        self.button_settings_2 = QPushButton("-운영진 설정")
        self.button_settings_2.setContentsMargins(50,0,0,0)
        self.button_settings_2.clicked.connect(self.parent.open_settings_2)

        self.button_in_progress_1 = QPushButton("-서비스 마감 순")
        self.button_in_progress_1.setContentsMargins(50,0,0,0)
        self.button_in_progress_1.clicked.connect(self.parent.open_in_progress_1)

        self.button_in_progress_2 = QPushButton("-견적서 시작 순")
        self.button_in_progress_2.setContentsMargins(50,0,0,0)
        self.button_in_progress_2.clicked.connect(self.parent.open_in_progress_2)
        
        frame_1 = QFrame()
        frame_1.setFrameShape(QFrame.Shape.Panel)

        frame_2 = QFrame()
        frame_2.setFrameShape(QFrame.Shape.Panel)

        frame_3 = QFrame()
        frame_3.setFrameShape(QFrame.Shape.Panel)

        frame_1.setLayout(self.content_left)
        frame_2.setLayout(self.dock_top)
        frame_3.setLayout(content_right)

        self.content.addWidget(frame_1)
        self.content.addWidget(frame_3)
        content_right.addLayout(content_right_top)
        content_right_top.addWidget(self.table_label)
        content_right_top.addLayout(search_layout_1)
        search_layout_1.setContentsMargins(600,0,0,0)
        content_right.addWidget(self.table)

        search_layout_1.addWidget(self.line_search_1)
        search_layout_1.addWidget(button_search_1)

        self.content_left.setContentsMargins(50,0,50,0)

        self.content_left.addWidget(button_new, 0)
        self.content_left.addWidget(button_in_progress, 1)
        self.content_left.addWidget(button_complete, 2)
        self.content_left.addWidget(button_current, 3)
        self.content_left.addWidget(button_lecture, 4)
        self.content_left.addWidget(button_settings, 5)

        dock_right.addLayout(self.layout_info)
        self.layout_info.addWidget(self.label_notice)
        self.layout_info.addWidget(self.label_info)
        dock_right.addWidget(self.label_datetime)
        dock_right.setContentsMargins(100,0,0,0)
        self.mainwindow.addWidget(frame_2)
        self.mainwindow.addLayout(self.content)
        self.mainwindow.setStretchFactor(self.content, 5)
        self.dock_top.addLayout(dock_left)
        self.dock_top.addLayout(dock_right)
        dock_left.addWidget(button_efficio)
        dock_left.setContentsMargins(0,0,400,0)
        dock_right.setContentsMargins(400,0,0,0)

        self.setLayout(self.mainwindow)

    def split_in_progress(self) : 
        if self.in_progress_split == False : 
            self.button_in_progress_1 = QPushButton("-서비스 마감 순")
            self.button_in_progress_1.setContentsMargins(50,0,0,0)
            self.button_in_progress_1.clicked.connect(self.parent.open_in_progress_1)

            self.button_in_progress_2 = QPushButton("-견적서 시작 순")
            self.button_in_progress_2.setContentsMargins(50,0,0,0)
            self.button_in_progress_2.clicked.connect(self.parent.open_in_progress_2)

            self.content_left.insertWidget(2, self.button_in_progress_1,alignment=Qt.AlignmentFlag.AlignRight)
            self.content_left.insertWidget(3, self.button_in_progress_2,alignment=Qt.AlignmentFlag.AlignRight)

            self.in_progress_split = True
        else : 
            self.button_in_progress_1.deleteLater()
            self.button_in_progress_2.deleteLater()

            self.in_progress_split = False
    def split_settings(self) : 
        if self.settings_split == False : 

            self.button_settings_1 = QPushButton("-사용자 목록")
            self.button_settings_1.setContentsMargins(50,0,0,0)
            self.button_settings_1.clicked.connect(self.parent.open_settings_1)

            self.button_settings_2 = QPushButton("-운영진 설정")
            self.button_settings_2.setContentsMargins(50,0,0,0)
            self.button_settings_2.clicked.connect(self.parent.open_settings_2)

            self.settings_split = True
            self.content_left.addWidget(self.button_settings_1,alignment=Qt.AlignmentFlag.AlignRight)
            self.content_left.addWidget(self.button_settings_2,alignment=Qt.AlignmentFlag.AlignRight)
        else : 
            self.button_settings_1.deleteLater()
            self.button_settings_2.deleteLater()
            self.settings_split = False

