# -*- encoding : utf-8 -*-
'''connect to Chandao's databases for query data what to you want
   Note:
       database information :
       IP: 10.10.12.47
       port: 3306
       user: tester
       password: tester@com
       databases name = zentao
'''

import pymysql
class connectDatabases:
    def __init__(self):
        self.IP = "10.10.12.47"
        self.port = 3306
        self.user = "tester"
        self.password = "tester@com"
        self.database = "zentao"

    def queryData(self, sql_query):
        try:
            connection = pymysql.connect(host=self.IP, port=self.port,
                                         user=self.user, password=self.password,
                                         db=self.database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        except Exception as e:
            print(e)

        try:
            curs = connection.cursor()
            curs.execute(sql_query)
            result = curs.fetchall()
            connection.close()
            return result
        except ConnectionError as e1:
            print(e1)

# if __name__ == "__main__":
#     #sql = "SELECT * FROM zt_build WHERE `name` IN('SPC700B010', 'SPC700B020', 'SPC700B030', 'SPC700B050', 'SPC700B060') and project = 67"
#     #sql = "select * from zt_bug"
#     sql ="select name, bugs from zt_build where `name` in ('SPC700B010','SPC700B020','SPC700B030','SPC700B050','SPC700B060') and project = 67"
#     a = connectDatabases().queryData(sql_query=sql)
#     print(a)