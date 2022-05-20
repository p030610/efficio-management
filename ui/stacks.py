#main class which displays ui
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *

import pymysql
import time

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

    def get_table_deadline_align(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from company order by deadline_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_deadline_align.setColumnCount(6)

        self.mainwindow.table_deadline_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            self.mainwindow.table_deadline_align.setItem(index, 0, QTableWidgetItem(str(i["deadline_date"])))
            self.mainwindow.table_deadline_align.setItem(index, 1, QTableWidgetItem(str(i["name"])))
            self.mainwindow.table_deadline_align.setItem(index, 2, QTableWidgetItem(str(i["service_name"])))
            self.mainwindow.table_deadline_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))
            self.mainwindow.table_deadline_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))
            self.mainwindow.table_deadline_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
            index += 1

    def get_table_estimate_align(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from company order by estimate_publish_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_estimate_align.setColumnCount(6)

        self.mainwindow.table_estimate_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            self.mainwindow.table_estimate_align.setItem(index, 0, QTableWidgetItem(str(i["deadline_date"])))
            self.mainwindow.table_estimate_align.setItem(index, 1, QTableWidgetItem(str(i["name"])))
            self.mainwindow.table_estimate_align.setItem(index, 2, QTableWidgetItem(str(i["represent"])))
            self.mainwindow.table_estimate_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))
            self.mainwindow.table_estimate_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))
            self.mainwindow.table_estimate_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
            index += 1

    def mainwindow_search_1(self) : 

        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='efficio_manage',
                             cursorclass=pymysql.cursors.DictCursor)

        cursors = self.connection.cursor()

        sql = "select * from company where name = '" + self.mainwindow.line_search_1.text() + "' order by name desc"

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

        sql = "select * from company where name = '" + self.mainwindow.line_search_2.text() + "' order by deadline_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_deadline_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            self.mainwindow.table_deadline_align.setItem(index, 0, QTableWidgetItem(str(i["deadline_date"])))
            self.mainwindow.table_deadline_align.setItem(index, 1, QTableWidgetItem(str(i["name"])))
            self.mainwindow.table_deadline_align.setItem(index, 2, QTableWidgetItem(str(i["service_name"])))
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

        sql = "select * from company where name = '" + self.mainwindow.line_search_3.text() + "' order by estimate_publish_date desc"

        cursors.execute(sql)

        self.data = cursors.fetchall()

        self.connection.close()

        self.mainwindow.table_estimate_align.setRowCount(len(self.data))

        index = 0

        for i in self.data : 
            self.mainwindow.table_estimate_align.setItem(index, 0, QTableWidgetItem(str(i["deadline_date"])))
            self.mainwindow.table_estimate_align.setItem(index, 1, QTableWidgetItem(str(i["name"])))
            self.mainwindow.table_estimate_align.setItem(index, 2, QTableWidgetItem(str(i["represent"])))
            self.mainwindow.table_estimate_align.setItem(index, 3, QTableWidgetItem(str(i["stock_left"])))
            self.mainwindow.table_estimate_align.setItem(index, 4, QTableWidgetItem(str(i["entire_stock"])))
            self.mainwindow.table_deadline_align.setItem(index, 5, QTableWidgetItem(str(i["id"])))
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
        self.company_detail.line_edit_content_down_2_4.setText(str(self.data[0]["memo"]))

        self.company_detail.table.setColumnCount(10)
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

