#main class which displays ui
from os.path import abspath
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5 import QAxContainer


import shutil
import win32com
import win32com.client

import datetime
import openpyxl
from openpyxl import load_workbook

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
        self.refresh_mainwindow_tables()
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
        self.load_complete()
        self.complete.show()
    def company_list_clicked(self) : 
        self.close_all_windows()
        self.load_company_list()
        self.company_list.show()
    def lecture_clicked(self) : 
        self.close_all_windows()
        self.lecture.show()
    def settings_clicked(self) : 
        self.close_all_windows()
        self.settings.show()
    def read_users(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

    def in_progress_1_table_clicked(self) : 
        row = self.in_progress.table.currentRow()

        col = self.in_progress.table.currentColumn()

        if col == 1 : 
            pass
            #서비스 중도 오픈
        elif col ==  0: 
            self.open_company_detail_page(self.in_progress.table.item(row, 7).text())

    def in_progress_2_table_clicked(self) : 
        row = self.in_progress_2.table.currentRow()

        self.open_company_detail_page(self.in_progress_2.table.item(row, 7).text())
    
    def complete_table_clicked(self) : 
        row = self.complete.table.currentRow()

        self.open_company_detail_page(self.complete.table.item(row, 7).text())

    def company_list_table_clicked(self) : 
        row = self.company_list.table.currentRow()

        col = self.company_list.table.currentColumn()

        if col == 4 : 
            pass
            #서비스 중도 오픈
        elif col == 1 : 
            self.open_company_detail_page(self.company_list.table.item(row, 8).text())

    def open_company_detail_page(self, id) : 

        self.current_company_detail_page = id

        self.close_all_windows()

        self.company_detail.show()

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from notice where username = '" + self.login_info_id + "' and manage = '미확인'"

        cursors.execute(sql)

        self.notice_data = cursors.fetchall()

        self.mainwindow.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.in_progress.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.in_progress_2.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.complete.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.settings.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.settings_2.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.company_list.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.lecture.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.mainwindow.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.company_detail.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step1_1.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step1_2.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step1_3.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step1_4.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step1_5.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step2_1.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step2_2.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step3_1.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step3_2.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step3_3.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step3_4.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step4_1.label_notice.setText(str(len(self.notice_data)) + "개의 알림")
        self.new_step4_2.label_notice.setText(str(len(self.notice_data)) + "개의 알림")

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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
                    time_gap = datetime.datetime.strptime(str(i["deadline"]),"%Y-%m-%d") - datetime.datetime.today()
                    self.in_progress.table.setItem(index, 5, QTableWidgetItem(str(time_gap).replace("days","일")))#남은기한
                    self.in_progress.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                    self.in_progress.table.setItem(index, 7, QTableWidgetItem(str(j["id"])))
                    index += 1

    def load_in_progress_2(self) : 
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
                    self.in_progress_2.table.setItem(index, 7, QTableWidgetItem(str(j["id"])))
                    index += 1

    def load_complete(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                            user='efficio',
                            password='efficio-password',
                            database='efficio_manage',
                            cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services where status = '완료' order by estimate_publish_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        sql_company = "select * from company"

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.complete.table.setRowCount(len(self.data))

        index = 0

        
        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    # "No", "구분", "기업명", "대표자명", "연락처", "날짜", "특이사항", "고유번호"
                    self.complete.table.setItem(index, 0, QTableWidgetItem(str(index + 1)))#기업명
                    self.complete.table.setItem(index, 1, QTableWidgetItem(str(j["type"])))#대표자명
                    self.complete.table.setItem(index, 2, QTableWidgetItem(str(j["name"])))
                    self.complete.table.setItem(index, 3, QTableWidgetItem(str(j["represent"])))
                    self.complete.table.setItem(index, 4, QTableWidgetItem(str(j["phone"])))
                    self.complete.table.setItem(index, 5, QTableWidgetItem(str(i["complete_report"])))
                    self.complete.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                    self.complete.table.setItem(index, 7, QTableWidgetItem(str(j["id"])))
                    index += 1

    def load_company_list(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                            user='efficio',
                            password='efficio-password',
                            database='efficio_manage',
                            cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql_company = "select * from company"

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.company_list.table.setRowCount(len(self.data_company))

        index = 0

        for j in self.data_company : 
            # "No","기업명", "대표자명", "연락처", "진행 상황", "잔액", "잔금 여부", "특이 사항"
            self.company_list.table.setItem(index, 0, QTableWidgetItem(str(index + 1)))
            self.company_list.table.setItem(index, 1, QTableWidgetItem(str(j["name"])))
            self.company_list.table.setItem(index, 2, QTableWidgetItem(str(j["represent"])))
            self.company_list.table.setItem(index, 3, QTableWidgetItem(str(j["phone"])))
            self.company_list.table.setItem(index, 4, QTableWidgetItem(str(j["status"])))
            self.company_list.table.setItem(index, 5, QTableWidgetItem(str(j["left_money"])))
            if str(j["left_money"]) != "0" : 
                money_left_yn = "있음"
            else : 
                money_left_yn = "없음"
            self.company_list.table.setItem(index, 6, QTableWidgetItem(str(money_left_yn)))
            self.company_list.table.setItem(index, 7, QTableWidgetItem(str(j["memo"])))
            self.company_list.table.setItem(index, 8, QTableWidgetItem(str(j["id"])))
            index += 1

    def in_progress_search(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
                    if str(self.in_progress.line_search_1.text()) in str(j["name"]) or self.in_progress.line_search_1.text() in str(i["name"]) or self.in_progress.line_search_1.text() in str(j["memo"]) :

                        self.in_progress.table.setItem(index, 0, QTableWidgetItem(str(j["name"])))#기업명
                        self.in_progress.table.setItem(index, 1, QTableWidgetItem(str(i["name"])))#서비스명
                        self.in_progress.table.setItem(index, 2, QTableWidgetItem(str(i["left_works"])))
                        self.in_progress.table.setItem(index, 3, QTableWidgetItem(str(i["did_works"])))
                        self.in_progress.table.setItem(index, 4, QTableWidgetItem(str(i["deadline"])))
                        time_gap = datetime.datetime.strptime(str(i["deadline"]),"%Y-%m-%d") - datetime.datetime.today()
                        self.in_progress.table.setItem(index, 5, QTableWidgetItem(str(time_gap).replace("days","일")))#남은기한
                        self.in_progress.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                        self.in_progress.table.setItem(index, 7, QTableWidgetItem(str(j["id"])))
                        index += 1

        self.in_progress.table.setRowCount(index)

        if index == 0 : 
            QMessageBox.information(self.in_progress,'알림 ','검색결과가 없습니다')
        else : 
            QMessageBox.information(self.in_progress,'알림 ','검색 완료')

    def in_progress_2_search(self) : 
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
                    if str(self.in_progress_2.line_search_1.text()) in str(j["name"]) or self.in_progress_2.line_search_1.text() in str(i["name"]) or self.in_progress_2.line_search_1.text() in str(j["memo"]) :
                        self.in_progress_2.table.setItem(index, 0, QTableWidgetItem(str(j["name"])))#기업명
                        self.in_progress_2.table.setItem(index, 1, QTableWidgetItem(str(j["represent"])))#대표자명
                        self.in_progress_2.table.setItem(index, 2, QTableWidgetItem(str(j["phone"])))
                        self.in_progress_2.table.setItem(index, 3, QTableWidgetItem(str(i["estimate_publish_date"])))
                        self.in_progress_2.table.setItem(index, 4, QTableWidgetItem(str(j["advance_money"])))
                        self.in_progress_2.table.setItem(index, 5, QTableWidgetItem(str(j["left_money"])))
                        self.in_progress_2.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                        self.in_progress_2.table.setItem(index, 7, QTableWidgetItem(str(j["id"])))
                        index += 1
        self.in_progress_2.table.setRowCount(index)

    def complete_search(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                            user='efficio',
                            password='efficio-password',
                            database='efficio_manage',
                            cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services where status = '완료' order by estimate_publish_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        sql_company = "select * from company"

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.complete.table.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            for j in self.data_company : 
                if i["company_id"] == j["id"] : 
                    if str(self.complete.line_search_1.text()) in str(j["name"]) or self.complete.line_search_1.text() in str(j["memo"]) or self.complete.line_search_1.text() in str(j["phone"]) :
                        # "No", "구분", "기업명", "대표자명", "연락처", "날짜", "특이사항", "고유번호"
                        self.complete.table.setItem(index, 0, QTableWidgetItem(str(index + 1)))#기업명
                        self.complete.table.setItem(index, 1, QTableWidgetItem(str(j["type"])))#대표자명
                        self.complete.table.setItem(index, 2, QTableWidgetItem(str(j["name"])))
                        self.complete.table.setItem(index, 3, QTableWidgetItem(str(j["represent"])))
                        self.complete.table.setItem(index, 4, QTableWidgetItem(str(j["phone"])))
                        self.complete.table.setItem(index, 5, QTableWidgetItem(str(i["complete_report"])))
                        self.complete.table.setItem(index, 6, QTableWidgetItem(str(j["memo"])))
                        self.complete.table.setItem(index, 7, QTableWidgetItem(str(j["id"])))
                        index += 1


        self.complete.table.setRowCount(index)

        if index == 0 : 
            QMessageBox.information(self.complete,'알림 ','검색결과가 없습니다')
        else : 
            QMessageBox.information(self.complete,'알림 ','검색 완료')
            

    def company_list_search(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                            user='efficio',
                            password='efficio-password',
                            database='efficio_manage',
                            cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql_company = "select * from company"

        cursors.execute(sql_company)

        self.data_company = cursors.fetchall()

        self.connection.close()

        self.company_list.table.setRowCount(len(self.data_company))

        index = 0

        for j in self.data_company : 
            if str(self.company_list.line_search_1.text()) in str(j["name"]) or self.company_list.line_search_1.text() in str(j["memo"]) or self.company_list.line_search_1.text() in str(j["phone"]) :
                # "No","기업명", "대표자명", "연락처", "진행 상황", "잔액", "잔금 여부", "특이 사항"
                self.company_list.table.setItem(index, 0, QTableWidgetItem(str(index + 1)))
                self.company_list.table.setItem(index, 1, QTableWidgetItem(str(j["name"])))
                self.company_list.table.setItem(index, 2, QTableWidgetItem(str(j["represent"])))
                self.company_list.table.setItem(index, 3, QTableWidgetItem(str(j["phone"])))
                self.company_list.table.setItem(index, 4, QTableWidgetItem(str(j["status"])))
                self.company_list.table.setItem(index, 5, QTableWidgetItem(str(j["left_money"])))
                if str(j["left_money"]) != "0" : 
                    money_left_yn = "있음"
                else : 
                    money_left_yn = "없음"
                self.company_list.table.setItem(index, 6, QTableWidgetItem(str(money_left_yn)))
                self.company_list.table.setItem(index, 7, QTableWidgetItem(str(j["memo"])))
                self.company_list.table.setItem(index, 8, QTableWidgetItem(str(j["id"])))
                index += 1


        self.company_list.table.setRowCount(index)

        if index == 0 : 
            QMessageBox.information(self.company_list,'알림 ','검색결과가 없습니다')
        else : 
            QMessageBox.information(self.company_list,'알림 ','검색 완료')
            
        

    def fill_table_in_progress_1(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from services order by deadline desc"

        cursors.execute(sql)

        self.data_service = cursors.fetchall()

        self.connection.close()

    def fill_table_in_progress_2(self) : 

        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
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
        if self.new_step1_1.input_consult_date.text() == "" or self.new_step1_1.input_dantok.text() == "" or self.new_step1_1.input_company_name.text() == "" or  self.new_step1_1.input_business_num.text() == "" or self.new_step1_1.input_represent.text() == "" or self.new_step1_1.input_represent_phone.text() == "" or self.new_step1_1.input_damdangja.text() == "" or self.new_step1_1.input_damdangja_phone.text() == "": 
            QMessageBox.information(self.new_step1_1,'알림 ','누락된 정보가 있습니다.')
        else : 
                
            self.connection = pymysql.connect(host='34.72.92.140',
                                user='efficio',
                                password='efficio-password',
                                database='efficio_manage',
                                cursorclass=pymysql.cursors.DictCursor)

            cursors = self.connection.cursor()

            sql_get_company = "select * from company where name like '%" + self.new_step1_1.input_company_name.text() + "%'"

            cursors.execute(sql_get_company)

            company_data = cursors.fetchall()

            if len(company_data) > 0 : 
                self.company_name = self.new_step1_1.input_company_name.text() + "(" + str(len(company_data) + 1) + ")"
                sql = "insert into company (name, represent, phone, left_money, memo, deadline_date, notice_date, advance_money, damdangja, damdangja_phone, business_num, medium_money, consult_date) values ('" + self.new_step1_1.input_company_name.text() + "(" + str(len(company_data) + 1) + ")" + "','" + self.new_step1_1.input_represent.text() +   "','" + self.new_step1_1.input_represent_phone.text() + "','0','없음','" + datetime.datetime.today().strftime("%Y-%m-%d") + "', '" + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "','0', '" + self.new_step1_1.input_damdangja.text() + "','" + self.new_step1_1.input_damdangja_phone.text() + "','" + self.new_step1_1.input_business_num.text() + "','0', '" + self.new_step1_1.input_consult_date.text() + "');"
            else :
                self.company_name = self.new_step1_1.input_company_name.text()
                sql = "insert into company (name, represent, phone, left_money, memo, deadline_date, notice_date, advance_money, damdangja, damdangja_phone, business_num, medium_money, consult_date) values ('" + self.new_step1_1.input_company_name.text() + "','" + self.new_step1_1.input_represent.text() +   "','" + self.new_step1_1.input_represent_phone.text() + "','0','없음','" + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "', '" + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "','0', '" + self.new_step1_1.input_damdangja.text() + "','" + self.new_step1_1.input_damdangja_phone.text() + "','" + self.new_step1_1.input_business_num.text() + "','0', '" + self.new_step1_1.input_consult_date.text() + "');"

            cursors.execute(sql)

            self.connection.commit()

            QMessageBox.information(self.registerpage,'알림 ','신규 회사 정보가 저장되었습니다')

            self.connection.close()

            #버퍼 저장

            self.company_represent = self.new_step1_1.input_represent.text()

            self.company_phone = self.new_step1_1.input_represent_phone.text()

            self.company_damdangja = self.new_step1_1.input_damdangja.text()

            self.company_damdangja_phone = self.new_step1_1.input_damdangja_phone.text()

            self.company_business_num = self.new_step1_1.input_business_num.text()

            self.new_step1_3.label_content_right_1_1.setText("1. [" + self.company_name + "] 견적서를 발송했나요?")
            self.new_step1_3.label_content_right_1_2.setText("2. [" + self.company_name + "] 견적서를 최종 검토가 완료되었을까요?")
            self.new_step1_3.label_content_right_2_1.setText("3. [" + self.company_name + "] 세금계산서 여부")
            self.new_step1_3.label_content_right_2_2.setText("4. [" + self.company_name + "] 세금계산서 발행 날짜")

            self.estimate_company_detail = pd.DataFrame(columns=["상담날짜", "단톡여부", "기업명", "사업자등록번호", "대표자", "대표자 연락처", "담당자", "담당자 연락처", "견적서 발송여부", "견적서 최종검토여부", "세금계산서 여부", "세금계산서 발행날짜", "입금확인", "선금", "중도금", "잔금", "선금날짜", "중도금날짜", "잔금날짜", "거래처시트작성여부", "거래처시트 더블체크", "잔금입금여부", "선금내역", "중도금내역", "잔금내역", "최종완료여부"], index=range(1))

            self.estimate_company_detail.iloc[0, 0] = self.new_step1_1.input_consult_date.text()#상담날짜
            self.estimate_company_detail.iloc[0, 1] = self.new_step1_1.input_dantok.text()#단톡여부
            self.estimate_company_detail.iloc[0, 2] = self.company_name#기업명
            self.estimate_company_detail.iloc[0, 3] = self.new_step1_1.input_business_num.text()#사업자등록번호
            self.estimate_company_detail.iloc[0, 4] = self.new_step1_1.input_represent.text()#대표자
            self.estimate_company_detail.iloc[0, 5] = self.new_step1_1.input_represent_phone.text()#대표자 연락처
            self.estimate_company_detail.iloc[0, 6] = self.new_step1_1.input_damdangja.text()#담당자
            self.estimate_company_detail.iloc[0, 7] = self.new_step1_1.input_damdangja_phone.text()#담당자 연락처
            self.estimate_company_detail.iloc[0, 8] = 0 #견적서 발송여부
            self.estimate_company_detail.iloc[0, 9] = 0 #견적서 최종검토여부
            self.estimate_company_detail.iloc[0, 10] = 0 #세금계산서 여부
            self.estimate_company_detail.iloc[0, 11] = "2001-01-01"#세금계산서 발행일
            self.estimate_company_detail.iloc[0, 12] = 0 #입금확인
            self.estimate_company_detail.iloc[0, 13] = 0 #선금
            self.estimate_company_detail.iloc[0, 14] = 0 #중도금
            self.estimate_company_detail.iloc[0, 15] = 0 #잔금
            self.estimate_company_detail.iloc[0, 16] = "2001-01-01" #선금날짜
            self.estimate_company_detail.iloc[0, 17] = "2001-01-01" #중도금날짜
            self.estimate_company_detail.iloc[0, 18] = "2001-01-01" #잔금날짜
            self.estimate_company_detail.iloc[0, 19] = 0 #거래처시트작성여부
            self.estimate_company_detail.iloc[0, 20] = 0 #거래처시트 더블체크
            self.estimate_company_detail.iloc[0, 21] = 0 #잔금입금여부
            self.estimate_company_detail.iloc[0, 22] = 0 #선금내역
            self.estimate_company_detail.iloc[0, 23] = 0 #중도금내역
            self.estimate_company_detail.iloc[0, 24] = 0 #잔금내역
            self.estimate_company_detail.iloc[0, 25] = 0 #최종완료여부

    def open_new_step_1_2(self) : 
        self.step1_2_saved = False
        if self.new_step1_1.input_consult_date.text() == "" or self.new_step1_1.input_dantok.text() == "" or self.new_step1_1.input_company_name.text() == "" or  self.new_step1_1.input_business_num.text() == "" or self.new_step1_1.input_represent.text() == "" or self.new_step1_1.input_represent_phone.text() == "" or self.new_step1_1.input_damdangja.text() == "" or self.new_step1_1.input_damdangja_phone.text() == "": 
            QMessageBox.information(self.new_step1_1,'알림 ','누락된 정보가 있습니다.')
        else : 
            self.close_all_windows()
            self.new_step1_2.show()

            self.new_step_1_2_row_count = 0

            self.new_step1_2.table_estimate.setColumnCount(6)
            self.new_step1_2.table_estimate.setRowCount(self.new_step_1_2_row_count)
            self.new_step1_2.table_estimate.setHorizontalHeaderLabels(["품목","사양","단가(숫자만)","수량(숫자만)","공급가액(숫자만)","비고"])

            self.new_step1_2.table_estimate.setColumnWidth(0,int(self.new_step1_2.table_estimate.width()/6))
            self.new_step1_2.table_estimate.setColumnWidth(1,int(self.new_step1_2.table_estimate.width()/6))
            self.new_step1_2.table_estimate.setColumnWidth(2,int(self.new_step1_2.table_estimate.width()/6))
            self.new_step1_2.table_estimate.setColumnWidth(3,int(self.new_step1_2.table_estimate.width()/6))
            self.new_step1_2.table_estimate.setColumnWidth(4,int(self.new_step1_2.table_estimate.width()/6))
            self.new_step1_2.table_estimate.setColumnWidth(5,int(self.new_step1_2.table_estimate.width()/6))

    def add_table_row_new_step_1_2(self) : 

        self.new_step_1_2_row_count += 1
        self.new_step1_2.table_estimate.setRowCount(self.new_step_1_2_row_count)

        self.new_step1_2.table_estimate.setItem(self.new_step_1_2_row_count - 1, 5, QTableWidgetItem("없음"))


    def convert_estimate_pdf(self) : 
        try :
            shutil.copyfile("./template/견적서 원본파일/견적서템플릿.xlsx", "./견적서/" + self.company_name + "_견적서.xlsx")

            wb = load_workbook("./견적서/" + self.company_name + "_견적서.xlsx")
            sheet = wb.active

            sheet['C3'] = self.company_name
            sheet["C2"] = datetime.datetime.today().strftime("%Y.%m.%d")
            
            sheet.insert_rows(8, len(self.estimate_detail.index))

            wb.save("./견적서/" + self.company_name + "_견적서.xlsx")

            index = 0
            price_sum = 0

            for name, row in self.estimate_detail.iterrows() : 
                # "품목", "사양", "단가", "수량", "공급가액", "비고", "가이드발송여부", "가이드수신여부", "실행여부", "중간보고여부", "업무완료여부", "최종보고여부", "가이드발송일", "가이드수신일", "실행일", "중간보고일", "업무완료일", "최종보고일"
                sheet["A" + str(index + 8)] = row[0]
                sheet["B" + str(index + 8)] = row[1]
                sheet["C" + str(index + 8)] = row[2]
                sheet["D" + str(index + 8)] = row[3]
                sheet["E" + str(index + 8)] = row[4]
                sheet["F" + str(index + 8)] = row[5]
                index += 1
                price_sum += int(row[4])

            sheet["B" + str(index + 11)] = str(price_sum) + "원"

            wb.save("./견적서/" + self.company_name + "_견적서.xlsx")

            excel = win32com.client.dynamic.Dispatch("Excel.Application")

            wb = excel.Workbooks.Open(abspath("./견적서/" + self.company_name + "_견적서.xlsx"))

            ws_data = wb.Worksheets("Sheet1")
            ws_data.Select()

            pdf_path = abspath("./견적서/" + self.company_name + "_견적서.pdf")

            wb.ActiveSheet.ExportAsFixedFormat(0, pdf_path)
            wb.Close(False)
            excel.Quit()
            QMessageBox.information(self.new_step1_2,'알림 ','견적서 변환 성공.')

            time.sleep(1)

            self.new_step1_3.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step1_4.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step1_5.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step2_1.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step2_2.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step3_1.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step3_2.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step3_3.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step3_4.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step4_1.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
            self.new_step4_2.webView.load(QUrl(str(abspath('./견적서/' + self.company_name + '_견적서.pdf')).replace("%5C","/").replace("\\", "/")))
        except : 
            QMessageBox.information(self.new_step1_2,'알림 ','견적서 변환 과정에서 오류가 발생했습니다.')


    def save_table_new_step_1_2(self) : 

        self.step1_2_saved = True

        number_of_rows = self.new_step1_2.table_estimate.rowCount()
        number_of_columns = self.new_step1_2.table_estimate.columnCount()

        #견적서 상세정보 저장 버퍼
        self.estimate_detail = pd.DataFrame(columns=["품목", "사양", "단가", "수량", "공급가액", "비고", "가이드발송여부", "가이드수신여부", "실행여부", "중간보고여부", "업무완료여부", "최종보고여부", "가이드발송일", "가이드수신일", "실행일", "중간보고일", "업무완료일", "최종보고일"], index=range(number_of_rows))

        try : 
            for i in range(number_of_rows):
                for j in range(number_of_columns):
                    self.estimate_detail.iloc[i, j] = self.new_step1_2.table_estimate.item(i, j).text()
        

            for i in range(number_of_rows):
                for j in range(number_of_columns + 1, number_of_columns + 6):
                    self.estimate_detail.iloc[i, j] = 0

            for i in range(number_of_rows):
                self.estimate_detail.iloc[i, 6] = 1

            for i in range(number_of_rows):
                for j in range(12, 18):
                    self.estimate_detail.iloc[i, j] = "2001-01-01"

            print(self.estimate_detail)

            QMessageBox.information(self.new_step1_2,'알림 ','성공적으로 견적서 정보가 저장되었습니다')

            self.load_new_step_2_1()

        except AttributeError: 
            QMessageBox.information(self.new_step1_2,'알림 ','세부사항 정보를 입력해주세요')

    def open_new_step_1_3(self) : 
        if self.step1_2_saved ==  True : 
            self.close_all_windows()
            self.new_step1_3.show()

        else : 
            QMessageBox.information(self.new_step1_2,'알림 ','세부사항 정보를 입력&저장 해주세요')

    def new_step_1_3_1_o_clicked(self) : 
        self.new_step1_3.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: blue;}')
        self.new_step1_3.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,8] = 1

    def new_step_1_3_1_x_clicked(self) : 
        self.new_step1_3.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: red;}')
        self.new_step1_3.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,8] = 0

    def new_step_1_3_2_o_clicked(self) : 
        self.new_step1_3.button_content_right_1_2_o.setStyleSheet('QPushButton {background-color: blue;}')
        self.new_step1_3.button_content_right_1_2_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,9] = 1

    def new_step_1_3_2_x_clicked(self) : 
        self.new_step1_3.button_content_right_1_2_x.setStyleSheet('QPushButton {background-color: red;}')
        self.new_step1_3.button_content_right_1_2_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,9] = 0
    
    def new_step_1_3_3_o_clicked(self) : 
        self.new_step1_3.button_content_right_2_1_o.setStyleSheet('QPushButton {background-color: blue;}')
        self.new_step1_3.button_content_right_2_1_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,10] = 1

    def new_step_1_3_3_x_clicked(self) : 
        self.new_step1_3.button_content_right_2_1_x.setStyleSheet('QPushButton {background-color: red;}')
        self.new_step1_3.button_content_right_2_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,10] = 0

    def new_step_1_3_4_calendar_clicked(self) : 
        self.estimate_company_detail.iloc[0,11] = self.new_step1_3.label_content_right_2_2_calendar.text()

    def open_new_step_1_4(self) : 
        self.close_all_windows()
        self.new_step1_4.show()

        self.close_all_windows()
        self.new_step1_4.show()


    def new_step_1_4_1_o_clicked(self) : 
        self.new_step1_4.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: blue;}')
        self.new_step1_4.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,12] = 1

    def new_step_1_4_1_x_clicked(self) : 
        self.new_step1_4.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: red;}')
        self.new_step1_4.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,12] = 0

    def open_new_step_1_5(self) : 
        self.close_all_windows()
        self.new_step1_5.show()

    def new_step_1_5_1_o_clicked(self) : 
        self.new_step1_5.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: blue;}')
        self.new_step1_5.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,19] = 1

    def new_step_1_5_1_x_clicked(self) : 
        self.new_step1_5.button_content_right_1_1_x.setStyleSheet('QPushButton {background-color: red;}')
        self.new_step1_5.button_content_right_1_1_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,19] = 0

    def new_step_1_5_2_o_clicked(self) : 
        self.new_step1_5.button_content_right_1_2_o.setStyleSheet('QPushButton {background-color: blue;}')
        self.new_step1_5.button_content_right_1_2_x.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,20] = 1

    def new_step_1_5_2_x_clicked(self) : 
        self.new_step1_5.button_content_right_1_2_x.setStyleSheet('QPushButton {background-color: red;}')
        self.new_step1_5.button_content_right_1_2_o.setStyleSheet('QPushButton {background-color: yellow;}')
        self.estimate_company_detail.iloc[0,20] = 0

    def download_excel_new_step_1_5(self) : 
        pass

    def open_new_step_2_1(self) : 
        self.close_all_windows()
        
        self.new_step2_1.show()

    def upload_company_service_detail(self) : 
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql_company = "update company set consult_date = '" + str(self.estimate_company_detail.iloc[0, 0]) + "', dantok = '" + str(self.estimate_company_detail.iloc[0, 1]) + "', estimate_send = '" + str(self.estimate_company_detail.iloc[0, 8]) + "', estimate_confirm = '" + str(self.estimate_company_detail.iloc[0, 9]) + "', tax_yn = '" + str(self.estimate_company_detail.iloc[0, 10]) + "', tax_date = '" + str(self.estimate_company_detail.iloc[0, 11]) + "', deposit_yn = '" + str(self.estimate_company_detail.iloc[0, 12]) + "', advance_money = '" + str(self.estimate_company_detail.iloc[0, 13]) + "', medium_money = '" + str(self.estimate_company_detail.iloc[0, 14]) + "', left_money = '" + str(self.estimate_company_detail.iloc[0, 15]) + "', advance_money_date = '" + str(self.estimate_company_detail.iloc[0, 16]) + "', medium_money_date = '" + str(self.estimate_company_detail.iloc[0, 17]) + "', left_money_date = '" + str(self.estimate_company_detail.iloc[0, 18]) + "', sheet_yn = '" + str(self.estimate_company_detail.iloc[0, 19]) + "', double_check = '" + str(self.estimate_company_detail.iloc[0, 20]) + "', left_money_deposit_yn = '" + str(self.estimate_company_detail.iloc[0, 21]) + "', final_complete = '" + str(self.estimate_company_detail.iloc[0, 25]) + "', final_complete_date = '" + str(datetime.datetime.today().strftime("%Y-%m-%d")) + "' where name = '" + self.company_name + "'"
        cursors.execute(sql_company)

        self.connection.commit()

        sql_get_company = "select * from company where name = '" + self.company_name + "';"
        cursors.execute(sql_get_company)

        company_data = cursors.fetchall()

        print(str(company_data[0]["service_saved"]))

        if str(company_data[0]["service_saved"]) == "0" or company_data[0]["service_saved"] == 0 or company_data[0]["service_saved"] == "0": 

            for name, row in self.estimate_detail.iterrows() : 

                sql_service = "insert into services (company_id, name, content, price, amount, price_2, memo, is_guide_send, is_guide_receive, is_work_commit, is_interim_report, is_work_complete, is_complete_report, guide_send, guide_receive, work_commit_date, interim_report, work_complete, complete_report) values ('" + str(company_data[0]["id"]) + "','" + str(row[0]) + "','" + str(row[1]) +   "','" + str(row[2]) + "','" + str(row[3]) + "','" + str(row[4]) + "','" + str(row[5]) + "','" + str(row[6]) + "','" + str(row[7]) + "','" + str(row[8]) + "','" + str(row[9]) + "','" + str(row[10]) + "','" + str(row[11]) + "','" + str(row[12]) + "','" + str(row[13]) + "','" + str(row[14]) + "','" + str(row[15]) + "','" + str(row[16]) + "','" + str(row[17]) + "');"
                cursors.execute(sql_service)
                self.connection.commit()
        else : 
            for name, row in self.estimate_detail.iterrows() : 

                sql_service = "update services set is_guide_send = '" + str(row[6]) + "', is_guide_receive = '" + str(row[7]) + "', is_work_commit = '" + str(row[8]) + "', is_interim_report = '" + str(row[9]) + "', is_work_complete = '" + str(row[10]) + "', is_complete_report = '" + str(row[11]) + "', guide_send = '" + str(row[12]) + "', guide_receive = '" + str(row[13]) + "', work_commit_date = '" + str(row[14]) + "', interim_report = '" + str(row[15]) + "', work_complete = '" + str(row[16]) + "', complete_report = '" + str(row[17]) + "' where name = '" + str(row[0]) + "' and content = '" + str(row[1]) + "'"
                cursors.execute(sql_service)
                self.connection.commit()

        sql_company = "update company set service_saved = 1 where name = '" + self.company_name + "';"
        cursors.execute(sql_service)
        self.connection.commit()

        QMessageBox.information(self.registerpage,'알림 ','회사&서비스 정보가 저장되었습니다')

        self.connection.close()

    def save_new_service(self) : 
        self.connection = pymysql.connect(host='34.72.92.140',
                             user='efficio',
                             password='efficio-password',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        get_company_sql = "select * from company"

        cursors.execute(get_company_sql)

        # data fetch
        self.data = cursors.fetchall()

        for i in self.data : 
            if i["name"] == self.company_name and i["phone"] == self.company_phone and i["business_num"] == self.company_business_num and i["damdangja"] == self.company_damdangja : 
                company_id = i["id"]


        for name, row in self.estimate_detail.iterrows() : 

            if row[6] == 1 : 
                step = 1
            elif row[7] == 1 : 
                step = 2
            elif row[8] == 1 : 
                step = 3
            elif row[9] == 1 : 
                step = 4
            elif row[10] == 1 : 
                step = 5
            elif row[11] == 1 : 
                step = 6
            else : 
                step = 1
            
            if str(row[12]) == 'nan' : 
                guide_send = '2000-01-01'
            else : 
                guide_send = row[12]

            if str(row[13]) == 'nan' : 
                guide_receive = '2000-01-01'
            else : 
                guide_receive = row[13]

            if str(row[14]) == 'nan' : 
                work_commit_date = '2000-01-01'
            else : 
                work_commit_date = row[14]

            if str(row[15]) == 'nan' : 
                interim_report = '2000-01-01'
            else : 
                interim_report = row[15]

            if str(row[16]) == 'nan' : 
                work_complete = '2000-01-01'
            else : 
                work_complete = row[16]

            if str(row[17]) == 'nan' : 
                complete_report = '2000-01-01'
            else : 
                complete_report = row[17]

            sql = "insert into services (company_id, name, content, price, amount, price_2, memo, step, status, guide_send, guide_receive, work_commit_date, interim_report, work_complete, complete_report) values ('" + str(company_id) + "','" + str(row[0]) +   "','" + str(row[1]) + "','" + str(row[2]) + "','" + str(row[3]) + "','" + str(row[4]) + "', '" + str(row[5]) + "','" + str(step) + "', '진행중','" + str(guide_send) + "','" + str(guide_receive) + "','" + str(work_commit_date) + "','" + str(interim_report) + "','" + str(work_complete) + "','" + str(complete_report) + "');"
            cursors.execute(sql)

            self.connection.commit()

        QMessageBox.information(self.registerpage,'알림 ','진행중인 서비스 정보가 저장되었습니다')

        self.connection.close()
    

    #초기화 개념의 함수

    def load_new_step_2_1(self) : 

        #이전, 저장, 다음 버튼 생성

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


        index = 0

        df_index = 0

        for i in self.layout_list_2_1 : 
            i.hide()

        self.layout_list_2_1 = []
        

        for name, row in self.estimate_detail.iterrows() : 
            if row[6] == 1 : 

                new_step_2_1_item = Step_2_1(index, df_index, row[0], self)

                self.layout_list_2_1.append(new_step_2_1_item)

                index += 1
            df_index += 1

        for widget in self.layout_list_2_1 : 
            self.new_step2_1.content_right.addWidget(widget)

    def open_new_step_2_2(self) : 
        self.close_all_windows()
        self.new_step2_2.show()

    def open_new_step_3_1(self) : 
        self.close_all_windows()
        self.new_step3_1.show()

    def open_new_step_3_2(self) : 
        self.close_all_windows()
        self.new_step3_2.show()

    def open_new_step_3_3(self) : 
        self.close_all_windows()
        self.new_step3_3.show()

    def open_new_step_3_4(self) : 
        self.close_all_windows()
        self.new_step3_4.show()

    def open_new_step_4_1(self) : 
        self.close_all_windows()
        self.new_step4_1.show()

    def open_new_step_4_2(self) : 
        self.close_all_windows()
        self.new_step4_2.show()

    def save_new_step_1_3(self) : 
        self.upload_company_service_detail()
    
    def save_new_step_1_4(self) : 
        self.estimate_company_detail.iloc[0,13] = self.new_step1_4.input_money_1_2.text()
        self.estimate_company_detail.iloc[0,14] = self.new_step1_4.input_money_2_2.text()
        self.estimate_company_detail.iloc[0,15] = self.new_step1_4.input_money_3_2.text()
        self.estimate_company_detail.iloc[0,16] = self.new_step1_4.input_money_1_3.text()
        self.estimate_company_detail.iloc[0,17] = self.new_step1_4.input_money_2_3.text()
        self.estimate_company_detail.iloc[0,18] = self.new_step1_4.input_money_3_3.text()
        self.upload_company_service_detail()

    def save_new_step_1_5(self) : 
        self.upload_company_service_detail()

    def save_new_step_2_1(self) : 
        self.upload_company_service_detail()

    def save_new_step_2_2(self) : 
        self.upload_company_service_detail()

    def save_new_step_3_1(self) : 
        self.upload_company_service_detail()

    def save_new_step_3_2(self) : 
        self.upload_company_service_detail()

    def save_new_step_3_3(self) : 
        self.upload_company_service_detail()

    def save_new_step_3_4(self) : 
        self.upload_company_service_detail()

    def save_new_step_4_1(self) : 
        self.upload_company_service_detail()

    def save_new_step_4_2(self) : 
        self.upload_company_service_detail()

    #견적서 세부사항 이동

    def move_to_guide_receive(self, text, index, button) : #2-1 2-2
        button.hide()

        self.estimate_detail.iloc[index, 7] = 1
        self.estimate_detail.iloc[index, 6] = 0

        #12~17

        self.estimate_detail.iloc[index, 12] = button.label_content_right_1_1_calendar.text()

        new_step_2_2_item = Step_2_2(index, index, text, self)

        self.new_step2_2.content_right.addWidget(new_step_2_2_item)

    def move_to_run(self, text, index, button) : #2-2 3-1
        button.hide()

        new_step_3_1_item = Step_3_1(index, index, text, self)

        self.new_step3_1.content_right.addWidget(new_step_3_1_item)

        self.estimate_detail.iloc[index, 8] = 1
        self.estimate_detail.iloc[index, 7] = 0

        self.estimate_detail.iloc[index, 13] = button.label_content_right_1_1_calendar.text()

    def move_to_midterm(self, text, index, button) : #3-1 3-2
        button.hide()

        new_step_3_2_item = Step_3_2(index, index, text, self)

        self.new_step3_2.content_right.addWidget(new_step_3_2_item)

        self.estimate_detail.iloc[index, 9] = 1
        self.estimate_detail.iloc[index, 8] = 0

        self.estimate_detail.iloc[index, 14] = button.label_content_right_1_1_calendar.text()

    def move_to_complete(self, text, index, button) : #3-2 3-3
        button.hide()

        new_step_3_3_item = Step_3_3(index, index, text, self)

        self.new_step3_3.content_right.addWidget(new_step_3_3_item)

        self.estimate_detail.iloc[index, 10] = 1
        self.estimate_detail.iloc[index, 9] = 0

        self.estimate_detail.iloc[index, 15] = button.label_content_right_1_1_calendar.text()

    def move_to_final(self, text, index, button) : #3-3 3-4
        button.hide()

        new_step_3_4_item = Step_3_4(index, index, text, self)

        self.new_step3_4.content_right.addWidget(new_step_3_4_item)

        self.estimate_detail.iloc[index, 11] = 1
        self.estimate_detail.iloc[index, 10] = 0

        self.estimate_detail.iloc[index, 16] = button.label_content_right_1_1_calendar.text()

    def stay_final(self, text, index, button) : #3-4 ~

        self.estimate_detail.iloc[index, 17] = button.label_content_right_1_1_calendar.text()
    
    def load_lecture(self) : 
        pass
    