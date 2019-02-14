#coding:utf-8
import pymysql
import pymysql.cursors

'''
# 链接数据库
conn = pymysql.connect(host = '10.100.41.31',port = 3510, user = 'TCHotel_QA', passwd = '354AGkswO1XCxzSXYxCg', db = 'TCGHotelDistribution', charset = 'utf8')
#创建一个游标
cur = conn.cursor()
cur.execute("select * from test.RatePolicy where id=1")
print(cur.fetchone())
'''
class OperaMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host = '10.100.41.31',
            port = 3510,
            user = 'TCHotel_QA',
            passwd = '354AGkswO1XCxzSXYxCg',
            db = 'TCGHotelDistribution',
            charset = 'utf8',
            # 拿表字段
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    #查询一条数据
    def serch_one(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        print(res)

    #查询所有数据
    def serch_all(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        print(res)

    #插入单条数据
    def insert_db(self,sql):
        self.cur.execute(sql)
        res = self.conn.commit()
        print(res)
    #插入多条数据
    def insert_many_db(self,sql,list):
        self.cur.executemany(sql,list)
        res = self.conn.commit()
        print(res)

    #更新数据
    def update_db(self,sql):
        self.cur.execute(sql)
        res = self.conn.commit()
        print(res)

    #删除数据
    def delete_db(self,sql):
        self.cur.execute(sql)
        res = self.conn.commit()
        print(res)

'''
if __name__ == '__main__':
    op_sql = OperaMysql()
    str1='a'
    str2='b'
    listb=[(str1,str2)]
    print(listb)
    lista=[('a','b'),('c','d')]
    #print(type(lisa[0]))
    sql = """insert into test.RatePolicy(RateCode,pk) VALUES (%s,%s)"""
    sqla="select * from test.RatePolicy"
    sqld='delete from test.RatePolicy where id=3 '
    sqlu='update test.RatePolicy set ratecode="-8348403921146513380^151_441",pk="yjtestpk" where id=1'
    #op_sql.serch_all(sqla)
    #op_sql.insert_db(sql)
    #op_sql.update_db(sqlu)
    #op_sql.delete_db(sqld)
    op_sql.insert_many_db(sql,listb)
'''