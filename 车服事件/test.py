import csv,xlrd,time
book=xlrd.open_workbook('D:\python\车服事件\总成类型字段统一.xls')
table=book.sheet_by_name('数据字典')
code_s=table.col_values(1,2)
name_s=table.col_values(2,2)
id_=1438059895889920000
name_="发动机控制系统(ECU)"
code_="EMS"
sort_value_=""
dictionary_id_=2
status_=1
readonly_=1
dictionary_type_=1
creator_=1377099300533764097
create_time_=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
updator_=""
update_time_=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
remark_=""
delete_=0
delete_version_=0
rows1=[]
rows2=[]
for i in range(len(code_s)):
    row=[id_,name_,code_,sort_value_,dictionary_id_,status_,readonly_,dictionary_type_,
         creator_,create_time_,updator_,update_time_,remark_,delete_,delete_version_]
    row[1]=name_s[i]
    row[2]=code_s[i]
    rows1.append(row)
    id_=id_+1
for i in range(len(code_s)):
    row=[id_,name_,code_,sort_value_,dictionary_id_,status_,readonly_,dictionary_type_,
         creator_,create_time_,updator_,update_time_,remark_,delete_,delete_version_]
    row[1]="总成类型-"+name_s[i]+"特征"
    row[2]=code_s[i]
    row[4]=17
    row[7]=2
    rows2.append(row)
    id_=id_+1
headers = ['id_','name_','code_','sort_value_','dictionary_id_','status_','readonly_','dictionary_type_',
           'creator_','create_time_','updator_','update_time_','remark_','delete_','delete_version_']
with open('test.csv', 'w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows1)
    f_csv.writerows(rows2)