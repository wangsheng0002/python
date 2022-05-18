import requests,json,csv
url1="https://xmeta.intranet.ruixiude.com:15933/rt/v1/vehicle/inner/vehicle/vehicleList"
header={
    "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNDk3MDgzODcxMTI3MjEyMDM0IiwidXNlckFjY291bnQiOiJhZG1pbl9qY3h4IiwidGVuYW50SWQiOiIxNDk3MDgzODcxMTIzMDE3NzI5IiwidGVuYW50Q29kZSI6ImpjeHgiLCJleHAiOjE2NTIzMTkyNTgsInVzZXJOYW1lIjoi57O757uf566h55CG5ZGYIiwiaWF0IjoxNjUyMjMyODU4LCJ1c2VyQ29kZSI6ImpjeHgifQ.sBQzkExWLDB355U-QGU7827y0NVyZv3GyhF7st06YYM"
}


with open("new_data - 业务.csv", mode="r", encoding="utf-8-sig") as f:
    # 基于打开的文件，创建csv.reader实例
    reader = csv.reader(f)
    dic={}
    for i in reader:
        dic.setdefault(i[0],i[1])



re=requests.request(method="get",url=url1,headers=header).json()
with open("new_data-xmate.csv", mode="w", encoding="utf-8-sig", newline="") as f:

    # 基于打开的文件，创建 csv.writer 实例
    writer = csv.writer(f)
    header_list = ["id", "vin", "Code", "是否一致"]
    # 写入 header。
    # writerow() 一次只能写入一行。
    writer.writerow(header_list)
    for i in re['data']:

        if dic.get(str(i['vin']))==str(i['modelCode']):
            list1=[str(i['id'])+"\t",str(i['vin'])+"\t",str(i['modelCode'])+"\t","一致",dic.get(str(i['vin']))+"\t"]
            writer.writerow(list1)
        else:
            list1=[str(i['id'])+"\t",str(i['vin'])+"\t",str(i['modelCode'])+"\t","不一致",dic.get(str(i['vin']))]
            writer.writerow(list1)
