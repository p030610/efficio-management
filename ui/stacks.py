#main class which displays ui
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *

import pymysql
import time

from sqlalchemy import false

from ui.company_detail import Company_detail
from ui.company_list import Company_list
from ui.complete import Complete
from ui.current import Current
from ui.in_progress import In_progress
from ui.lecture import Lecture
from ui.loginpage import Loginpage
from ui.mainwindow import Mainwindow
from ui.new_step1_1 import New_step1_1
from ui.new_step1_2 import New_step1_2
from ui.new_step1_3 import New_step1_3
from ui.new_step1_4 import New_step1_4
from ui.new_step1_5 import New_step1_5
from ui.new_step2_1 import New_step2_1
from ui.new_step2_2 import New_step2_2
from ui.new_step3_1 import New_step3_1
from ui.new_step3_2 import New_step3_2
from ui.new_step3_3 import New_step3_3
from ui.new_step3_4 import New_step3_4
from ui.new_step4_1 import New_step4_1
from ui.new_step4_2 import New_step4_2
from ui.register import Register
from ui.settings import Settings

class Stacks():
    def __init__(self):

        self.company_detail = Company_detail(self)#기업상세
        self.company_list = Company_list(self)#기업 리스트
        self.complete = Complete(self)#완료
        self.current = Current(self)
        self.in_progress = In_progress(self)#진행 중
        self.lecture = Lecture(self)#강의
        self.loginpage = Loginpage(self)#로그인페이지
        self.mainwindow = Mainwindow(self)#대시보드
        self.new_step1_1 = New_step1_1(self)#신규스텝 1-1
        self.new_step1_2 = New_step1_2(self)#신규스텝 1-2
        self.new_step1_3 = New_step1_3(self)#신규스텝 1-3
        self.new_step1_4 = New_step1_4(self)#신규스텝 1-4
        self.new_step1_5 = New_step1_5(self)#신규스텝 1-5

        self.new_step2_1 = New_step2_1(self)#신규스텝 2-1
        self.new_step2_2 = New_step2_2(self)#신규스텝 2-2

        self.new_step3_1 = New_step3_1(self)#신규스텝 3-1
        self.new_step3_2 = New_step3_2(self)#신규스텝 3-2
        self.new_step3_3 = New_step3_3(self)#신규스텝 3-3
        self.new_step3_4 = New_step3_4(self)#신규스텝 3-4

        self.new_step4_1 = New_step4_1(self)#신규스텝 4-1
        self.new_step4_2 = New_step4_2(self)#신규스텝 4-2

        self.registerpage = Register(self)#회원가입페이지
        self.settings = Settings(self)#설정창


        self.loginpage.show()

    def login(self, child, id, pw):

        print(id)
        print(pw)

        self.read_users()
        time.sleep(0.5)
        login_success = False
        for i in self.data : 
            if str(id) == i['username'] and str(pw) == i["password"] : 
                login_success = True
                username = i["name"]
        if login_success == True : 
            self.close_all_windows()
            self.company_list.label_info.setText(id + ":" + username)
            self.complete.label_info.setText(id + ":" + username)
            self.current.label_info.setText(id + ":" + username)
            self.in_progress.label_info.setText(id + ":" + username)
            self.lecture.label_info.setText(id + ":" + username)
            self.mainwindow.label_info.setText(id + ":" + username)
            self.new_step1_1.label_info.setText(id + ":" + username)
            self.new_step1_2.label_info.setText(id + ":" + username)
            self.new_step1_3.label_info.setText(id + ":" + username)
            self.new_step1_4.label_info.setText(id + ":" + username)
            self.new_step1_5.label_info.setText(id + ":" + username)
            self.new_step2_1.label_info.setText(id + ":" + username)
            self.new_step2_2.label_info.setText(id + ":" + username)
            self.new_step3_1.label_info.setText(id + ":" + username)
            self.new_step3_2.label_info.setText(id + ":" + username)
            self.new_step3_3.label_info.setText(id + ":" + username)
            self.new_step3_4.label_info.setText(id + ":" + username)
            self.new_step4_1.label_info.setText(id + ":" + username)
            self.new_step4_2.label_info.setText(id + ":" + username)
            self.mainwindow.show()
            QMessageBox.information(child,'알림 ','성공적으로 로그인 되었습니다')
        else : 
            QMessageBox.warning(child,'알림 ','계정정보가 존재하지 않습니다')

    def register(self) :
        self.close_all_windows()
        self.registerpage.show()

    def find_id(self):
        self.close_all_windows()
        self.find_id.show()

    def find_pw(self):
        self.close_all_windows()
        self.find_pw.show()

    def goto_home(self):
        self.close_all_windows()
        self.mainwindow.show()
    def new_clicked(self) : 
        self.close_all_windows()
        self.new_step1_1.show()
    def in_progress_clicked(self) : 
        self.close_all_windows()
        self.in_progress.show()
    def complete_clicked(self) : 
        self.close_all_windows()
        self.complete.show()
    def current_clicked(self) : 
        self.close_all_windows()
        self.current.show()
    def lecture_clicked(self) : 
        self.close_all_windows()
        self.lecture.show()
    def settings_clicked(self) : 
        self.close_all_windows()
        self.settings.show()
    def read_users(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='COLTm1911a1@',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        # SQL문 실행
        sql = "SELECT * FROM users"
        cursors.execute(sql)

        # data fetch
        self.data = cursors.fetchall()

        # connection 닫기
        self.connection.close()

    def close_all_windows(self) : 

        self.company_detail.close()
        self.company_list.close()
        self.complete.close()
        self.current.close()
        self.in_progress.close()
        self.lecture.close()
        self.loginpage.close()
        self.mainwindow.close()
        self.new_step1_1.close()
        self.new_step1_2.close()
        self.new_step1_3.close()
        self.new_step1_4.close()
        self.new_step1_5.close()
        self.new_step2_1.close()
        self.new_step2_2.close()
        self.new_step3_1.close()
        self.new_step3_2.close()
        self.new_step3_3.close()
        self.new_step3_4.close()
        self.new_step4_1.close()
        self.new_step4_2.close()
        self.registerpage.close()
        self.settings.close()

    def move_to_register_page(self) : 
        self.close_all_windows()
        self.registerpage.show()

    def register_confirmed(self) : 
        self.close_all_windows()
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='COLTm1911a1@',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "insert into users (name, phone, username, password, position, level, authority) values ('" + self.registerpage.line_name.text() + "','" + self.registerpage.line_phone.text() +   "','" + self.registerpage.line_id.text() + "','" + self.registerpage.line_pw.text() + "','" + self.registerpage.line_position.text() + "','" + self.registerpage.line_level.text() + "', 1);"
        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        QMessageBox.information(self.registerpage,'알림 ','성공적으로 회원가입 되었습니다')

        self.close_all_windows()

        self.loginpage.show()

    def inspect_id(self) : 
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='COLTm1911a1@',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from users"
        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        for i in self.data : 
            
            if i["username"] == self.registerpage.line_id.text(): 
                self.registerpage.id_is_unique = False
                QMessageBox.warning(self.registerpage,'경고','존재하는 아이디입니다')
                break
            else : 
                self.registerpage.id_is_unique = True
                QMessageBox.warning(self.registerpage,'알림','유효한 아이디입니다')