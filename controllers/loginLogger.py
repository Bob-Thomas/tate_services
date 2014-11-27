import datetime
import os

import config
from models.database import db
from models.cashier import Cashier
from models.cashier_login import CashierLogin
from models.user import User
from models.user_groups import UserGroups
from os import listdir
from os.path import isfile, join
import xlwt
import xlrd

class LoginLogger():
    #name of the logfile to be created
    log_name = 'user_log'

    def write_to_log(self, email, faulty="valide login"):
        #if the file is not created create a header text
        if not os.path.exists(config.LOG_PATH+config.DIVIDER+'verkopers.log'):
            log = open(config.LOG_PATH+config.DIVIDER+'verkopers.log', 'a')
            log.write("|Naam|Email|Datum|Tijd|\n")
            log.close()
        #retrieve the user information
        user = self.get_login_information(email)
        #create date and time variables
        date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        time = str(datetime.datetime.now().strftime("%H:%M"))
        #create the layout of the file
        row = "|" + user.first_name + " " + user.last_name + "|" + user.email + "|" + date + "|" + time  + "|" + faulty + "\n"
        #append to existing file
        log = open(config.LOG_PATH+config.DIVIDER+self.log_name+'.log', 'a')
        #write the row to the file
        log.write(row)
        log.close()
        self.get_excel_from_log()

    def get_excel_from_log(self):

        # mypath should be the complete path for the directory containing the input text files
        #grab the path of were to log is
        mypath = config.LOG_PATH+config.DIVIDER+'verkopers.log'
        #check if it's number
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        #create an excel styling
        style = xlwt.XFStyle()
        #format for the number cell
        style.num_format_str = '#,###0.00'
        #create the file
        f = open(mypath, 'r+')
        row_list = []
        #add the header
        for row in f:
            row_list.append(row.split('|'))
        column_list = zip(*row_list)
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sheet1')
        i = 0
        #add the values
        for column in column_list:
            for item in range(len(column)):
                value = column[item].strip()
                if is_number(value):
                    worksheet.write(item, i, float(value), style=style)
                else:
                    worksheet.write(item, i, value)
            i+=1
        #save the file on the specified path
        workbook.save(config.EXCEL_PATH+config.DIVIDER+'verkopers.xls')

    def get_login_information(self, email):
        #get user object based on the user information
        user = Cashier.query.filter_by(email=email).first()
        if user:
            self.log_name = 'verkopers'
            return user
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                self.log_name = 'user_log'
                return user
        return 'no user found'


    def __init__(self):
        pass