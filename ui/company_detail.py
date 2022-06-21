# 5/27피드백
# 서비스 내역이 페이지 3분의 2 차지, 상세정보는 왼쪽에 폭의 3분의 1 형태로 기입
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime

class Company_detail(QWidget):
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
        self.content = QVBoxLayout()
        self.content_up = QHBoxLayout()
        self.content_down = QHBoxLayout()
        content_down_1 = QVBoxLayout()
        content_down_2 = QVBoxLayout()
        dock_right = QVBoxLayout()
        dock_left = QVBoxLayout()
        dock_button = QHBoxLayout()
        table_layout = QVBoxLayout()
        content_down_1_sublayout = QHBoxLayout()
        content_down_2_sublayout= QHBoxLayout()

        self.layout_info = QHBoxLayout()

        label_table = QLabel("서비스 내역")

        self.table = QTableWidget()
        

        
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

        # button_content_modify = QPushButton("수정")
        # button_content_modify.clicked.connect()
        button_content_save = QPushButton("저장")
        button_content_save.clicked.connect(self.parent.save_company_detail)

        label_content = QLabel("(기업명)상세정보")

        label_content_down_1_1 = QLabel("기업명")
        label_content_down_1_2 = QLabel("대표자명")
        label_content_down_1_3 = QLabel("연락처")
        label_content_down_1_4 = QLabel("담당자명")
        label_content_down_1_5 = QLabel("(담당자)연락처")
        label_content_down_1_6 = QLabel("사업자등록증")

        self.line_edit_content_down_1_1 = QLineEdit()
        self.line_edit_content_down_1_2 = QLineEdit()
        self.line_edit_content_down_1_3 = QLineEdit()
        self.line_edit_content_down_1_4 = QLineEdit()
        self.line_edit_content_down_1_5 = QLineEdit()

        button_content_down_1_1 = QPushButton("보기")
        button_content_down_1_2 = QPushButton("파일 업로드")
        button_content_down_1_3 = QPushButton("파일 다운로드")

        label_content_down_2_1 = QLabel("선금")
        label_content_down_2_2 = QLabel("잔금")
        label_content_down_2_3 = QLabel("마감 예정일")
        label_content_down_2_4 = QLabel("특이사항")
        label_content_down_2_5 = QLabel("소상공인확인서")

        self.line_edit_content_down_2_1 = QLineEdit()
        self.line_edit_content_down_2_2 = QLineEdit()
        self.line_edit_content_down_2_3 = QLineEdit()
        self.line_edit_content_down_2_4 = QPlainTextEdit()

        button_content_down_2_1 = QPushButton("보기")
        button_content_down_2_2 = QPushButton("파일 업로드")
        button_content_down_2_3 = QPushButton("파일 다운로드")

        table_layout.addWidget(label_table)
        table_layout.addWidget(self.table)

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

        self.content_up.addWidget(label_content)
        # self.content_up.addWidget(button_content_modify)
        self.content_up.addWidget(button_content_save)
        self.content_up.setContentsMargins(0,0,700,0)

        self.content.addLayout(self.content_up)#기업명 상세정보 수정 저장
        self.content.addLayout(self.content_down)
        self.content_down.addLayout(content_down_1)#좌측 column
        
        self.content_down.addLayout(content_down_2)#우측 column
        self.content_down.addLayout(table_layout)

        self.content_down.setContentsMargins(50,0,50,0)

        content_down_1.addWidget(label_content_down_1_1)
        content_down_1.addWidget(self.line_edit_content_down_1_1)#기업명
        content_down_1.addWidget(label_content_down_1_2)
        content_down_1.addWidget(self.line_edit_content_down_1_2)#대표자명
        content_down_1.addWidget(label_content_down_1_3)
        content_down_1.addWidget(self.line_edit_content_down_1_3)#연락처
        content_down_1.addWidget(label_content_down_1_4)
        content_down_1.addWidget(self.line_edit_content_down_1_4)#담당자명
        content_down_1.addWidget(label_content_down_1_5)
        content_down_1.addWidget(self.line_edit_content_down_1_5)#담당자 연락처
        content_down_1.addLayout(content_down_1_sublayout)#사업자등록증(보기)
        content_down_1_sublayout.addWidget(label_content_down_1_6)
        content_down_1_sublayout.addWidget(button_content_down_1_1)
        content_down_1.addWidget(button_content_down_1_2)
        content_down_1.addWidget(button_content_down_1_3)

        content_down_1_sublayout.setContentsMargins(0,370,0,0)

        content_down_2.addWidget(label_content_down_2_1)#선금
        content_down_2.addWidget(self.line_edit_content_down_2_1)
        content_down_2.addWidget(label_content_down_2_2)#잔금
        content_down_2.addWidget(self.line_edit_content_down_2_2)
        content_down_2.addWidget(label_content_down_2_3)#마감 예정일
        content_down_2.addWidget(self.line_edit_content_down_2_3)
        content_down_2.addWidget(label_content_down_2_4)#특이사항
        content_down_2.addWidget(self.line_edit_content_down_2_4)
        content_down_2.addLayout(content_down_2_sublayout)#소상공인확인서(보기)
        content_down_2_sublayout.addWidget(label_content_down_2_5)
        content_down_2_sublayout.addWidget(button_content_down_2_1)
        content_down_2.addWidget(button_content_down_2_2)
        content_down_2.addWidget(button_content_down_2_3)

        self.setLayout(self.mainwindow)