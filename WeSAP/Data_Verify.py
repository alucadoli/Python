# _*_ coding = utf-8 _*_
#http://pymssql.org/en/stable/pymssql_examples.html
# https://blog.csdn.net/chenyulancn/article/details/50624442
import pymssql
import re

# class MSSQL:
#     def __init__(self,host,user,pwd,db):
#         self.host = host
#         self.user = user
#         self.pwd = pwd
#         self.db = db
#
#     def __getconnect(self):
#         if not self.db:
#             raise (NameError,"No database information!")
#         self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf-8")
#         cur = self.conn.cursor()
#         if not cur:
#             raise (NameError,"Fail to connect database!")
#         else:
#             return cur
#
#     def execquery(self,sql):
#         cur = self.__getconnect()
#         cur.execute(sql)
#         reslist = cur.fetchall()
#
#         self.conn.close()
#         return reslist
#
#     def execnonquery(self,sql):
#         cur = self.__getconnect()
#         cur.execute(sql)
#         self.conn.commit()
#         self.conn.close()
#
#     def main():
#         # ms = MSSQL(host=)
#         resList = ms.ExecQuery(sql)
#
#     if __name__ == '__main__':
#         main()


def is_email(value):
    patt = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z]+){0,4}$'
    if not re.match(patt,value):
        print('Email Error!')
    return True


def is_mobile(value):
    patt = r'^1[0-9]{10}$'
    if not re.search(patt, str(value)):
        print('Mobile Error')
    return True

def is_phonenumber(value):
    patt = r'0\d{2,3}-\d{7,8}|0\d{2,3}-\d{7,8}-\d{3,5}'
    if not re.match(patt,value):
        print('PhoneNumber Error')
    return True

str = '0221-33221132-093'
is_phonenumber(str)

