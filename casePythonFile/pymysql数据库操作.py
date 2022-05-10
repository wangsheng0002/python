# import pymysql
# cont=pymysql.connect(host='192.168.233.132',port=3306,user='root',passwd='123456',db='wangsheng')
# cursor=cont.cursor()
# cursor.execute("select *from test00;")
# all=cursor.fetchall()
# print(all)
# print(type(all))
# one=cursor.fetchone()
# print(one)#注意：被取出的数据，后面在执行取数，取不到之前被取出的数据


import pymysql
class shujuku():
    def __init__(self):
        self.host='192.168.233.132'
        self.database='wangsheng'
        self.user='root'
        self.password='123456'
        self.prot=3306
    def conect(self):#登录数据库
        db=pymysql.connect(host='192.168.233.132',port=3306,user='root',passwd='123456',db='wangsheng')
        return db
    def select(self):#数据库查询
        pass
    def insert(self,insert1):#数据库插入数据
        db=self.conect()
        cursor = db.cursor()
        cursor.execute(insert1)
        db.commit()
        cursor.execute("select *from test00")
        insert2 = cursor.fetchall()
        print(insert2)
    def update(self,update1):#数据库更新数据
        db=self.conect()
        cursor=db.cursor()
        cursor.execute(update1)
        db.commit()
        cursor.execute("select *from test00")
        update2=cursor.fetchall()
        print(update2)
    def delete(self,delete1):#数据库删除数据
        db=self.conect()
        cursor=db.cursor()
        cursor.execute(delete1)
        db.commit()
        cursor.execute("select *from test00")
        delete2=cursor.fetchall()
        print(delete2)
if __name__ == '__main__':
    a=shujuku()
    # a.update("update test00 set name='wangsheng001' where id=1")
    a.delete("delete from test00 where name='wangsheng006'")
    # a.insert("insert into test00 value(6,95,'wangsheng006')")

