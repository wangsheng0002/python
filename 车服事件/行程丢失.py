import pymysql
cont=pymysql.connect(host='10.192.33.78',port=3306,user='root',passwd='MysqlSA7878',db='rxd_newbizmodel')
cursor=cont.cursor()
cursor.execute("select *from t_vhc_route where vin_='LFWSRXSJOKFA10760' and end_gps_ is not null;")
all=cursor.fetchall()
print(all)
print(type(all))

