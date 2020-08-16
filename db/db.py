# -*- coding: utf-8 -*-
def connect(self):
    self.mydb = pymysql.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            passwd=os.environ.get('DB_PASSWD'),
            db=os.environ.get('DB_NAME')
            )

def query(self, sql):
    try:
        cursor = self.mydb.cursor()
        cursor.execute(sql)
    except:
        self.connect()
        cursor = self.mydb.cursor()
        cursor.execute(sql)
    self.mydb.commit()
    return cursor
