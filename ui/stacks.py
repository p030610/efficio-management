#main class which displays ui
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *

import datetime

import pymysql
import time
from ftplib import FTP
import pandas as pd

from ui.item_new import Step_2_1, Step_2_2, Step_3_1, Step_3_2, Step_3_3, Step_3_4

from ui.company_detail import Company_detail
from ui.company_list import Company_list
from ui.complete import Complete
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
from ui.notice import Notice
from ui.settings_2 import Settings_2
from ui.in_progress_2 import In_progress_2

class Stacks():
    def __init__(self):

        self.layout_list_2_1 = []
        self.layout_list_2_2 = []
        self.layout_list_3_1 = []
        self.layout_list_3_2 = []
        self.layout_list_3_3 = []
        self.layout_list_3_4 = []

        self.company_detail = Company_detail(self)#기업상세
        self.company_list = Company_list(self)#기업 리스트
        self.complete = Complete(self)#완료
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
        self.notice = Notice(self)#알림창
        self.in_progress_2 = In_progress_2(self)
        self.settings_2 = Settings_2(self)

        self.loginpage.show()

    def login(self, child, id, pw):

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
            self.login_info_id = id

            self.get_notices()

            self.mainwindow.show()
            QMessageBox.information(child,'알림 ','성공적으로 로그인 되었습니다')

            self.refresh_mainwindow_tables()

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
        self.refresh_mainwindow_tables()

    def goto_home(self):
        self.close_all_windows()
        self.mainwindow.show()
    def new_clicked(self) : 
        self.close_all_windows()
        self.new_step1_1.show()
    def in_progress_clicked(self) : 
        self.close_all_windows()
        self.load_in_progress_1()
        self.in_progress.show()
    def complete_clicked(self) : 
        self.close_all_windows()
        self.complete.show()
    def company_list_clicked(self) : 
        self.close_all_windows()
        self.company_list.show()
    def lecture_clicked(self) : 
        self.close_all_windows()
        self.lecture.show()
    def settings_clicked(self) : 
        self.close_all_windows()
        self.settings.show()
    def read_users(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
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
        self.settings_2.close()
        self.in_progress_2.close()

    def move_to_register_page(self) : 
        self.close_all_windows()
        self.registerpage.show()

    def register_confirmed(self) : 
        self.close_all_windows()
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        print(self.registerpage.line_name.text())

        sql = "insert into users (name, phone, username, password, position, level, authority) values ('" + self.registerpage.line_name.text() + "','" + self.registerpage.line_phone.text() +   "','" + self.registerpage.line_id.text() + "','" + self.registerpage.line_pw.text() + "','" + self.registerpage.line_position.text() + "','" + self.registerpage.line_level.text() + "', '1');"
        cursors.execute(sql)

        self.connection.commit()


        QMessageBox.information(self.registerpage,'알림 ','성공적으로 회원가입 되었습니다')

        self.close_all_windows()

        self.loginpage.show()

        self.connection.close()


    def inspect_id(self) : 
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
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

    def get_table_company_list(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from company order by name desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_company_list.setColumnCount(6)

        self.mainwindow.table_company_list.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            self.mainwindow.table_company_list.setItem(index, 0, QTableWidgetItem(str(i["name"])))
            self.mainwindow.table_company_list.setItem(index, 1, QTableWidgetItem(str(i["represent"])))
            self.mainwindow.table_company_list.setItem(index, 2, QTableWidgetItem(str(i["phone"])))
            self.mainwindow.table_company_list.setItem(index, 3, QTableWidgetItem(str(i["left_money"])))
            self.mainwindow.table_company_list.setItem(index, 4, QTableWidgetItem(str(i["memo"])))
            self.mainwindow.table_company_list.setItem(index, 5, QTableWidgetItem(str(i["id"])))
            index += 1

    def get_table_deadline_align(self) : #기본 서비스단위로 재설계 필요(마감일 순으로 정렬)

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services order by estimate_publish_date desc"

        sql_company = "select * from company"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_deadline_align.setColumnCount(6)

        self.mainwindow.table_deadline_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    self.mainwindow.table_deadline_align.setItem(index, 0, QTableWidgetItem(str(i["deadline"])))
                    self.mainwindow.table_deadline_align.setItem(index, 1, QTableWidgetItem(str(j["name"])))#기업명
                    self.mainwindow.table_deadline_align.setItem(index, 2, QTableWidgetItem(str(i["name"])))#서비스명
                    self.mainwindow.table_deadline_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))
                    self.mainwindow.table_deadline_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))
                    self.mainwindow.table_deadline_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
                    index += 1

    def get_table_estimate_align(self) : #서비스단위로 재설계 필요(견적서 발행일자대로 정렬)

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services order by estimate_publish_date desc"

        sql_company = "select * from company"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_estimate_align.setColumnCount(6)

        self.mainwindow.table_estimate_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    self.mainwindow.table_estimate_align.setItem(index, 0, QTableWidgetItem(str(i["deadline"])))
                    self.mainwindow.table_estimate_align.setItem(index, 1, QTableWidgetItem(str(j["name"])))#기업명
                    self.mainwindow.table_estimate_align.setItem(index, 2, QTableWidgetItem(str(j["represent"])))
                    self.mainwindow.table_estimate_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))#남은 수량??
                    self.mainwindow.table_estimate_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))#전체 수량??
                    self.mainwindow.table_estimate_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
                    index += 1

    def mainwindow_search_1(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from company where name = '" + self.mainwindow.line_search_1.text() + "' or represent = '" + self.mainwindow.line_search_1.text() + "' or phone = '" + self.mainwindow.line_search_1.text() + "' or left_money = '" + self.mainwindow.line_search_1.text() + "' or memo = '" + self.mainwindow.line_search_1.text() + "' order by name desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_company_list.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            self.mainwindow.table_company_list.setItem(index, 0, QTableWidgetItem(str(i["name"])))
            self.mainwindow.table_company_list.setItem(index, 1, QTableWidgetItem(str(i["represent"])))
            self.mainwindow.table_company_list.setItem(index, 2, QTableWidgetItem(str(i["phone"])))
            self.mainwindow.table_company_list.setItem(index, 3, QTableWidgetItem(str(i["left_money"])))
            self.mainwindow.table_company_list.setItem(index, 4, QTableWidgetItem(str(i["memo"])))
            self.mainwindow.table_company_list.setItem(index, 5, QTableWidgetItem(str(i["id"])))
            index += 1

    def mainwindow_search_2(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services  where  name = '" + self.mainwindow.line_search_2.text() + "' or stock_left = '" + self.mainwindow.line_search_2.text() + "' or entire_stock = '" + self.mainwindow.line_search_2.text() + "' order by deadline desc"

        sql_company = "select * from company"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_deadline_align.setColumnCount(6)

        self.mainwindow.table_deadline_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    self.mainwindow.table_deadline_align.setItem(index, 0, QTableWidgetItem(str(i["deadline"])))
                    self.mainwindow.table_deadline_align.setItem(index, 1, QTableWidgetItem(str(j["name"])))#기업명
                    self.mainwindow.table_deadline_align.setItem(index, 2, QTableWidgetItem(str(i["name"])))#서비스명
                    self.mainwindow.table_deadline_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))
                    self.mainwindow.table_deadline_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))
                    self.mainwindow.table_deadline_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
                    index += 1

    def mainwindow_search_3(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services where name = '" + self.mainwindow.line_search_2.text() + "' order by estimate_publish_date  desc"

        sql_company = "select * from company"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_estimate_align.setColumnCount(6)

        self.mainwindow.table_estimate_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    self.mainwindow.table_estimate_align.setItem(index, 0, QTableWidgetItem(str(i["deadline"])))
                    self.mainwindow.table_estimate_align.setItem(index, 1, QTableWidgetItem(str(j["name"])))#기업명
                    self.mainwindow.table_estimate_align.setItem(index, 2, QTableWidgetItem(str(i["name"])))#서비스명
                    self.mainwindow.table_estimate_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))
                    self.mainwindow.table_estimate_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))
                    self.mainwindow.table_estimate_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
                    index += 1

    def refresh_mainwindow_tables(self) : 
        self.get_table_company_list()
        self.get_table_estimate_align()
        self.get_table_deadline_align()

    def mainwindow_table_1_clicked(self) : 
        row = self.mainwindow.table_company_list.currentRow()

        self.open_company_detail_page(self.mainwindow.table_company_list.item(row, 5).text())

    def mainwindow_table_2_clicked(self) : 
        row = self.mainwindow.table_deadline_align.currentRow()

        self.open_company_detail_page(self.mainwindow.table_deadline_align.item(row, 5).text())

    def mainwindow_table_3_clicked(self) : 
        row = self.mainwindow.table_estimate_align.currentRow()

        self.open_company_detail_page(self.mainwindow.table_estimate_align.item(row, 5).text())


    def open_company_detail_page(self, id) : 

        self.current_company_detail_page = id

        self.close_all_windows()

        self.company_detail.show()

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from company where id = '" + id + "'"

        sql_service = "select * from services where company_id = '" + id + "'"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        cursors.execute(sql_service)

        self.data_service = cursors.fetchall()

        self.connection.close()

        self.company_detail.line_edit_content_down_1_1.setText(str(self.data[0]["name"]))
        self.company_detail.line_edit_content_down_1_2.setText(str(self.data[0]["represent"]))
        self.company_detail.line_edit_content_down_1_3.setText(str(self.data[0]["phone"]))
        self.company_detail.line_edit_content_down_1_4.setText(str(self.data[0]["damdangja"]))
        self.company_detail.line_edit_content_down_1_5.setText(str(self.data[0]["damdangja_phone"]))
        self.company_detail.line_edit_content_down_2_1.setText(str(self.data[0]["advance_money"]))
        self.company_detail.line_edit_content_down_2_2.setText(str(self.data[0]["left_money"]))
        self.company_detail.line_edit_content_down_2_3.setText(str(self.data[0]["deadline_date"]))
        self.company_detail.line_edit_content_down_2_4.setPlainText(str(self.data[0]["memo"]))

        self.company_detail.table.setColumnCount(10)
        self.company_detail.table.setHorizontalHeaderLabels(["서비스명","가이드 전달","가이드 회신","업무 실행날짜","남은 건수","진행 건수","중간보고","마감날짜","완료 보고"])
        self.company_detail.table.setRowCount(len(self.data_service))

        index = 0

        for i in self.data_service : 
            self.company_detail.table.setItem(index, 0, QTableWidgetItem(str(i["name"])))
            self.company_detail.table.setItem(index, 1, QTableWidgetItem(str(i["guide_send"])))
            self.company_detail.table.setItem(index, 2, QTableWidgetItem(str(i["guide_receive"])))
            self.company_detail.table.setItem(index, 3, QTableWidgetItem(str(i["work_commit_date"])))
            self.company_detail.table.setItem(index, 4, QTableWidgetItem(str(i["left_works"])))
            self.company_detail.table.setItem(index, 5, QTableWidgetItem(str(i["did_works"])))
            self.company_detail.table.setItem(index, 6, QTableWidgetItem(str(i["interim_report"])))
            self.company_detail.table.setItem(index, 7, QTableWidgetItem(str(i["deadline"])))
            self.company_detail.table.setItem(index, 8, QTableWidgetItem(str(i["complete_report"])))
            self.company_detail.table.setItem(index, 9, QTableWidgetItem('-'))
            index += 1
    def get_notices(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from notice where username = '" + self.login_info_id + "' and manage = '미확인'"

        cursors.execute(sql)

        self.notice_data = cursors.fetchall()

        self.mainwindow.label_notice.setText(str(len(self.notice_data)) + "개의 알림")

        self.connection.close()

        self.notice.table.setRowCount(len(self.notice_data))

        index = 0

        for notice in self.notice_data : 
            self.notice.table.setItem(index, 0, QTableWidgetItem(str(notice["company_name"])))
            self.notice.table.setItem(index, 1, QTableWidgetItem(str(notice["damdangja"])))
            self.notice.table.setItem(index, 2, QTableWidgetItem(str(notice["notice_type"])))
            self.notice.table.setItem(index, 3, QTableWidgetItem(str(notice["notice_date"])))
            self.notice.table.setItem(index, 4, QTableWidgetItem(str(notice["deadline_date"])))
            self.notice.table.setItem(index, 5, QTableWidgetItem(str(notice["manage"])))
            index += 1
    def open_notice(self) : 
        self.notice.show()

    def open_login(self) : 
        self.close_all_windows()
        self.loginpage.show()

    def notice_read(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "update notice set manage = '읽음' where username = '" + self.login_info_id + "'"

        cursors.execute(sql)

        self.connection.commit()

        self.connection.close()


        QMessageBox.information(self.notice,'알림 ','성공적으로 읽음처리 되었습니다')

        self.get_notices()

    def save_company_detail(self) :

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "update company set name = '" + self.company_detail.line_edit_content_down_1_1.text() + "', represent = '" + self.company_detail.line_edit_content_down_1_2.text() + "', phone = '" + self.company_detail.line_edit_content_down_1_3.text() + "', damdangja = '" + self.company_detail.line_edit_content_down_1_4.text() + "', damdangja_phone = '" + self.company_detail.line_edit_content_down_1_5.text() + "', advance_money = '" + self.company_detail.line_edit_content_down_2_1.text() + "', left_money = '" + self.company_detail.line_edit_content_down_2_2.text() + "', deadline_date = '" + self.company_detail.line_edit_content_down_2_3.text() + "', memo = '" + self.company_detail.line_edit_content_down_2_4.toPlainText() + "'  where id = '" + self.current_company_detail_page + "'"

        cursors.execute(sql)

        self.connection.commit()

        self.connection.close()

        QMessageBox.information(self.notice,'알림 ','성공적으로 회사정보가 저장 되었습니다')

        self.close_all_windows()

        self.mainwindow.show()
    
    def upload_file(self) : 
        ftp = FTP('')
        ftp.login('아이디', '비번')

    def download_file(self) :
        ftp = FTP('')
        ftp.login('아이디', '비번')

    def load_in_progress_1(self) : 
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services where status = '진행중' order by deadline desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        sql_company = "select * from company"

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.in_progress.table.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    self.in_progress.table.setItem(index, 0, QTableWidgetItem(str(j["name"])))#기업명
                    self.in_progress.table.setItem(index, 1, QTableWidgetItem(str(i["name"])))#서비스명
                    self.in_progress.table.setItem(index, 2, QTableWidgetItem(str(i["left_works"])))
                    self.in_progress.table.setItem(index, 3, QTableWidgetItem(str(i["did_works"])))
                    self.in_progress.table.setItem(index, 4, QTableWidgetItem(str(i["deadline"])))
                    time_gap = datetime.datetime.strptime(str(i["deadline"]),"%Y-%m-%d %H:%M:%S") - datetime.datetime.today()
                    self.in_progress.table.setItem(index, 5, QTableWidgetItem(str(time_gap).replace("days","일")))#남은기한
                    self.in_progress.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                    index += 1

    def load_in_progress_2(self) : 
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services where status = '진행중' order by estimate_publish_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        sql_company = "select * from company"

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.in_progress_2.table.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    self.in_progress_2.table.setItem(index, 0, QTableWidgetItem(str(j["name"])))#기업명
                    self.in_progress_2.table.setItem(index, 1, QTableWidgetItem(str(j["represent"])))#대표자명
                    self.in_progress_2.table.setItem(index, 2, QTableWidgetItem(str(j["phone"])))
                    self.in_progress_2.table.setItem(index, 3, QTableWidgetItem(str(i["estimate_publish_date"])))
                    self.in_progress_2.table.setItem(index, 4, QTableWidgetItem(str(j["advance_money"])))
                    self.in_progress_2.table.setItem(index, 5, QTableWidgetItem(str(j["left_money"])))
                    self.in_progress_2.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                    index += 1


    def in_progress_search(self) : 
        pass

    def fill_table_in_progress_1(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services order by deadline desc"

        cursors.execute(sql)

        self.data_service = cursors.fetchall()

        self.connection.close()

    def fill_table_in_progress_2(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services order by interim_repost desc"

        cursors.execute(sql)

        self.data_service = cursors.fetchall()

        self.connection.close()

    def open_settings_1(self) : 
        self.close_all_windows()
        self.settings.show()

    def open_settings_2(self) : 
        self.close_all_windows()
        self.settings_2.show()

    def open_in_progress_2(self) : 
        self.close_all_windows()
        self.load_in_progress_2()
        self.in_progress_2.show()

    def open_in_progress_1(self) : 
        self.close_all_windows()
        self.load_in_progress_1()
        self.in_progress.show()

    def create_new_company(self) : 
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "insert into company (name, represent, phone, left_money, memo, deadline_date, notice_date, advance_money, damdangja, damdangja_phone, business_num, medium_money) values ('" + self.new_step1_1.input_company_name.text() + "','" + self.new_step1_1.input_represent.text() +   "','" + self.new_step1_1.input_represent_phone.text() + "','0','없음','" + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "', '" + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "','0', '" + self.new_step1_1.input_damdangja.text() + "','" + self.new_step1_1.input_damdangja_phone.text() + "','" + self.new_step1_1.input_business_num.text() + "','0');"
        cursors.execute(sql)

        self.connection.commit()

        QMessageBox.information(self.registerpage,'알림 ','신규 회사 정보가 저장되었습니다')

        self.connection.close()

    def open_new_step_1_2(self) : 
        self.close_all_windows()
        self.new_step1_2.show()

        self.new_step_1_2_row_count = 0

        self.new_step1_2.table_estimate.setColumnCount(6)
        self.new_step1_2.table_estimate.setRowCount(self.new_step_1_2_row_count)
        self.new_step1_2.table_estimate.setHorizontalHeaderLabels(["품목","사양","단가","수량","공급가액","비고"])

        self.new_step1_2.table_estimate.setColumnWidth(0,int(self.new_step1_2.table_estimate.width()/6))
        self.new_step1_2.table_estimate.setColumnWidth(1,int(self.new_step1_2.table_estimate.width()/6))
        self.new_step1_2.table_estimate.setColumnWidth(2,int(self.new_step1_2.table_estimate.width()/6))
        self.new_step1_2.table_estimate.setColumnWidth(3,int(self.new_step1_2.table_estimate.width()/6))
        self.new_step1_2.table_estimate.setColumnWidth(4,int(self.new_step1_2.table_estimate.width()/6))
        self.new_step1_2.table_estimate.setColumnWidth(5,int(self.new_step1_2.table_estimate.width()/6))

    def add_table_row_new_step_1_2(self) : 

        self.new_step_1_2_row_count += 1
        self.new_step1_2.table_estimate.setRowCount(self.new_step_1_2_row_count)

    def save_table_new_step_1_2(self) : 

        number_of_rows = self.new_step1_2.table_estimate.rowCount()
        number_of_columns = self.new_step1_2.table_estimate.columnCount()

        #견적서 상세정보 저장 버퍼
        self.estimate_detail = pd.DataFrame(columns=["품목", "사양", "단가", "수량", "공급가액", "비고", "가이드발송여부", "가이드수신여부", "실행여부", "중간보고여부", "업무완료여부", "최종보고여부"], index=range(number_of_rows))

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                self.estimate_detail.iloc[i, j] = self.new_step1_2.table_estimate.item(i, j).text()

        for i in range(number_of_rows):
            for j in range(number_of_columns + 1, number_of_columns + 6):
                self.estimate_detail.iloc[i, j] = 0

        for i in range(number_of_rows):
            self.estimate_detail.iloc[i, 6] = 1

        print(self.estimate_detail)

        QMessageBox.information(self.new_step1_2,'알림 ','성공적으로 견적서 정보가 저장되었습니다')

        self.load_new_step_2_1()

    def open_new_step_1_3(self) : 
        self.close_all_windows()
        self.new_step1_3.show()

        self.new_step_1_3_row_count = 0

        self.new_step1_3.table_estimate.setColumnCount(6)
        self.new_step1_3.table_estimate.setRowCount(self.new_step_1_2_row_count)
        self.new_step1_3.table_estimate.setHorizontalHeaderLabels(["품목","사양","단가","수량","공급가액","비고"])

        self.new_step1_3.table_estimate.setColumnWidth(0,int(self.new_step1_3.table_estimate.width()/6))
        self.new_step1_3.table_estimate.setColumnWidth(1,int(self.new_step1_3.table_estimate.width()/6))
        self.new_step1_3.table_estimate.setColumnWidth(2,int(self.new_step1_3.table_estimate.width()/6))
        self.new_step1_3.table_estimate.setColumnWidth(3,int(self.new_step1_3.table_estimate.width()/6))
        self.new_step1_3.table_estimate.setColumnWidth(4,int(self.new_step1_3.table_estimate.width()/6))
        self.new_step1_3.table_estimate.setColumnWidth(5,int(self.new_step1_3.table_estimate.width()/6))

    def save_new_step_1_3(self) : 
        pass

    def open_new_step_1_4(self) : 
        self.close_all_windows()
        self.new_step1_4.show()

    def save_new_step_1_4(self) : 
        pass

    def open_new_step_1_5(self) : 
        self.close_all_windows()
        self.new_step1_5.show()

    def download_excel_new_step_1_5(self) : 
        pass

    def save_new_step_1_5(self) :
        pass

    def open_new_step_2_1(self) : 
        self.close_all_windows()
        
        self.new_step2_1.show()

    def refresh_new_step_2_1(self) : 
        for i in self.layout_list_2_1 : 
            i.deleteLater()
            i.setParent(None)

    def load_new_step_2_1(self) : 

        self.new_step2_1.content_right.addLayout(self.new_step2_1.layout_content_right_button)

        self.new_step2_1.layout_content_right_button.addWidget(self.new_step2_1.button_previous)
        self.new_step2_1.layout_content_right_button.addWidget(self.new_step2_1.button_save)
        self.new_step2_1.layout_content_right_button.addWidget(self.new_step2_1.button_next)

        self.new_step2_2.content_right.addLayout(self.new_step2_2.layout_content_right_button)

        self.new_step2_2.layout_content_right_button.addWidget(self.new_step2_2.button_previous)
        self.new_step2_2.layout_content_right_button.addWidget(self.new_step2_2.button_save)
        self.new_step2_2.layout_content_right_button.addWidget(self.new_step2_2.button_next)

        self.new_step3_1.content_right.addLayout(self.new_step3_1.layout_content_right_button)

        self.new_step3_1.layout_content_right_button.addWidget(self.new_step3_1.button_previous)
        self.new_step3_1.layout_content_right_button.addWidget(self.new_step3_1.button_save)
        self.new_step3_1.layout_content_right_button.addWidget(self.new_step3_1.button_next)

        self.new_step3_2.content_right.addLayout(self.new_step3_2.layout_content_right_button)

        self.new_step3_2.layout_content_right_button.addWidget(self.new_step3_2.button_previous)
        self.new_step3_2.layout_content_right_button.addWidget(self.new_step3_2.button_save)
        self.new_step3_2.layout_content_right_button.addWidget(self.new_step3_2.button_next)

        self.new_step3_3.content_right.addLayout(self.new_step3_3.layout_content_right_button)

        self.new_step3_3.layout_content_right_button.addWidget(self.new_step3_3.button_previous)
        self.new_step3_3.layout_content_right_button.addWidget(self.new_step3_3.button_save)
        self.new_step3_3.layout_content_right_button.addWidget(self.new_step3_3.button_next)




        self.new_step3_4.content_right.addLayout(self.new_step3_4.layout_content_right_button)

        self.new_step3_4.layout_content_right_button.addWidget(self.new_step3_4.button_previous)
        self.new_step3_4.layout_content_right_button.addWidget(self.new_step3_4.button_save)
        self.new_step3_4.layout_content_right_button.addWidget(self.new_step3_4.button_next)

        print(self.estimate_detail)

        self.layout_list_2_1 = []

        index = 1

        df_index = 0

        for name, row in self.estimate_detail.iterrows() : 
            if row[6] == 1 : 

                new_step_2_1_item = Step_2_1(index, df_index, row[0], self)

                self.layout_list_2_1.append(new_step_2_1_item)

                index += 1
            df_index += 1

        for widget in self.layout_list_2_1 : 
            self.new_step2_1.content_right.addWidget(widget)

        

    def save_new_step_2_1(self) : 
        pass

    def open_new_step_2_2(self) : 
        self.close_all_windows()
        # try : 
        #     self.refresh_new_step_2_2()
        # except : 
        #     pass
        # self.load_new_step_2_2()
        self.new_step2_2.show()

    # def refresh_new_step_2_2(self) : 
    #     for i in self.layout_list_2_2 : 
    #         i.deleteLater()
    #         i.setParent(None)

    # def load_new_step_2_2(self) : 

    #     print(self.estimate_detail)

    #     self.layout_list_2_2 = []

    #     index = 1

    #     df_index = 0

    #     for name, row in self.estimate_detail.iterrows() : 
    #         if row[7] == 1 : 

    #             new_step_2_2_item = Step_2_2(index, df_index, row[0], self)

    #             self.layout_list_2_2.append(new_step_2_2_item)

    #             index += 1
    #         df_index += 1

    #     for widget in self.layout_list_2_2 : 
    #         self.new_step2_2.content_right.addWidget(widget)

    #     self.new_step2_2.content_right.addLayout(self.new_step2_2.layout_content_right_button)

    #     self.new_step2_2.layout_content_right_button.addWidget(self.new_step2_2.button_previous)
    #     self.new_step2_2.layout_content_right_button.addWidget(self.new_step2_2.button_save)
    #     self.new_step2_2.layout_content_right_button.addWidget(self.new_step2_2.button_next)

    def save_new_step_2_2(self) : 
        pass

    def open_new_step_3_1(self) : 
        self.close_all_windows()
        # try : 
        #     self.refresh_new_step_3_1()
        # except : 
        #     pass
        # self.load_new_step_3_1()
        self.new_step3_1.show()

    # def refresh_new_step_3_1(self) : 
    #     for i in self.layout_list_3_1 : 
    #         i.deleteLater()
    #         i.setParent(None)

    # def load_new_step_3_1(self) : 

    #     print(self.estimate_detail)

    #     self.layout_list_3_1 = []

    #     index = 1

    #     df_index = 0

    #     for name, row in self.estimate_detail.iterrows() : 
    #         if row[8] == 1 : 

    #             new_step_3_1_item = Step_3_1(index, df_index, row[0], self)

    #             self.layout_list_3_1.append(new_step_3_1_item)

    #             index += 1
    #         df_index += 1

    #     for layout in self.layout_list_3_1 : 
    #         self.new_step3_1.content_right.addWidget(layout)

    #     self.new_step3_1.content_right.addLayout(self.new_step3_1.layout_content_right_button)

    #     self.new_step3_1.layout_content_right_button.addWidget(self.new_step3_1.button_previous)
    #     self.new_step3_1.layout_content_right_button.addWidget(self.new_step3_1.button_save)
    #     self.new_step3_1.layout_content_right_button.addWidget(self.new_step3_1.button_next)

    # def save_new_step_3_1(self) : 
    #     pass

    def open_new_step_3_2(self) : 
        self.close_all_windows()
        # try : 
        #     self.refresh_new_step_3_2()
        # except : 
        #     pass
        # self.load_new_step_3_2()
        self.new_step3_2.show()

    # def refresh_new_step_3_2(self) : 
    #     for i in self.layout_list_3_2 : 
    #         i.deleteLater()
    #         i.setParent(None)


    # def load_new_step_3_2(self) : 

    #     self.layout_list_3_2 = []

    #     index = 1

    #     df_index = 0

    #     for name, row in self.estimate_detail.iterrows() : 
    #         if row[9] == 1 : 

    #             new_step_3_2_item = Step_3_2(index, df_index, row[0], self)

    #             self.layout_list_3_2.append(new_step_3_2_item)

    #             index += 1
    #         df_index += 1

    #     for layout in self.layout_list_3_2 : 
    #         self.new_step3_2.content_right.addWidget(layout)

    #     self.new_step3_2.content_right.addLayout(self.new_step3_2.layout_content_right_button)

    #     self.new_step3_2.layout_content_right_button.addWidget(self.new_step3_2.button_previous)
    #     self.new_step3_2.layout_content_right_button.addWidget(self.new_step3_2.button_save)
    #     self.new_step3_2.layout_content_right_button.addWidget(self.new_step3_2.button_next)


    def save_new_step_3_2(self) : 
        pass

    def open_new_step_3_3(self) : 
        self.close_all_windows()
        # try : 
        #     self.refresh_new_step_3_3()
        # except : 
        #     pass
        # self.load_new_step_3_3()
        self.new_step3_3.show()

    # def refresh_new_step_3_3(self) : 
    #     for i in self.layout_list_3_3 : 
    #         i.deleteLater()
    #         i.setParent(None)

    # def load_new_step_3_3(self) : 

    #     self.layout_list_3_3 = []

    #     index = 1

    #     df_index = 0

    #     for name, row in self.estimate_detail.iterrows() : 
    #         if row[10] == 1 : 

    #             new_step_3_3_item = Step_3_3(index, df_index, row[0], self)

    #             self.layout_list_3_3.append(new_step_3_3_item)

    #             index += 1
    #         df_index += 1

    #     for layout in self.layout_list_3_3 : 
    #         self.new_step3_3.content_right.addWidget(layout)

    #     self.new_step3_3.content_right.addLayout(self.new_step3_3.layout_content_right_button)

    #     self.new_step3_3.layout_content_right_button.addWidget(self.new_step3_3.button_previous)
    #     self.new_step3_3.layout_content_right_button.addWidget(self.new_step3_3.button_save)
    #     self.new_step3_3.layout_content_right_button.addWidget(self.new_step3_3.button_next)


    # def save_new_step_3_3(self) : 
    #     pass

    def open_new_step_3_4(self) : 
        self.close_all_windows()
        # try : 
        #     self.refresh_new_step_3_4()
        # except : 
        #     pass
        # self.load_new_step_3_4()
        self.new_step3_4.show()

    # def refresh_new_step_3_4(self) : 
    #     for i in self.layout_list_3_4 : 
    #         i.deleteLater()
    #         i.setParent(None)

    # def load_new_step_3_4(self) : 

    #     self.layout_list_3_4 = []

    #     index = 1

    #     df_index = 0

    #     for name, row in self.estimate_detail.iterrows() : 
    #         if row[11] == 1 : 

    #             new_step_3_4_item = Step_3_4(index, df_index, row[0], self)

    #             self.layout_list_3_4.append(new_step_3_4_item)

    #             index += 1
    #         df_index += 1

    #     for layout in self.layout_list_3_4 : 
    #         self.new_step3_4.content_right.addWidget(layout)

    #     self.new_step3_4.content_right.addLayout(self.new_step3_4.layout_content_right_button)

    #     self.new_step3_4.layout_content_right_button.addWidget(self.new_step3_4.button_previous)
    #     self.new_step3_4.layout_content_right_button.addWidget(self.new_step3_4.button_save)
    #     self.new_step3_4.layout_content_right_button.addWidget(self.new_step3_4.button_next)

    # def save_new_step_3_4(self) : 
    #     pass

    def open_new_step_4_1(self) : 
        self.close_all_windows()
        self.new_step4_1.show()

    def save_new_step_4_1(self) : 
        pass

    def open_new_step_4_2(self) : 
        self.close_all_windows()
        self.new_step4_2.show()

    def save_new_step_4_2(self) : 
        pass

    #견적서 세부사항 이동

    def move_to_guide_receive(self, text, index, button) : #2-1 2-2
        button._close_widget()

        self.estimate_detail.iloc[index, 7] = 1
        self.estimate_detail.iloc[index, 6] = 0

        new_step_2_2_item = Step_2_2(index, index, text, self)

        self.new_step2_2.content_right.addWidget(new_step_2_2_item)

    def move_to_run(self, text, index, button) : #2-2 3-1
        button._close_widget()

        new_step_3_1_item = Step_3_1(index, index, text, self)

        self.new_step3_1.content_right.addWidget(new_step_3_1_item)

        self.estimate_detail.iloc[index, 8] = 1
        self.estimate_detail.iloc[index, 7] = 0

    def move_to_midterm(self, text, index, button) : #3-1 3-2
        button._close_widget()

        new_step_3_2_item = Step_3_2(index, index, text, self)

        self.new_step3_2.content_right.addWidget(new_step_3_2_item)

        self.estimate_detail.iloc[index, 9] = 1
        self.estimate_detail.iloc[index, 8] = 0

    def move_to_complete(self, text, index, button) : #3-2 3-3
        button._close_widget()

        new_step_3_3_item = Step_3_3(index, index, text, self)

        self.new_step3_3.content_right.addWidget(new_step_3_3_item)

        self.estimate_detail.iloc[index, 10] = 1
        self.estimate_detail.iloc[index, 9] = 0

    def move_to_final(self, text, index, button) : #3-3 3-4
        button._close_widget()

        new_step_3_4_item = Step_3_4(index, index, text, self)

        self.new_step3_4.content_right.addWidget(new_step_3_4_item)

        self.estimate_detail.iloc[index, 11] = 1
        self.estimate_detail.iloc[index, 10] = 0

    def stay_final(self, text, index, button) : #3-4 ~
        pass

    
    # def load_lecture(self) : 
