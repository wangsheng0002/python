import requests
import csv
headers={"Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNDUxMTI2MzQ3NTQyODk2NjQyIiwidXNlckFjY291bnQiOiJhZG1pbl9JRFNCSUQiLCJ0ZW5hbnRJZCI6IjE0NTExMjYzNDc1MjYxMTk0MjYiLCJ0ZW5hbnRDb2RlIjoiSURTQklEIiwiZXhwIjoxNjQ5Mzk4NjkwLCJ1c2VyTmFtZSI6Iuezu-e7n-euoeeQhuWRmCIsImlhdCI6MTY0OTMxMjI5MCwidXNlckNvZGUiOiJJRFNCSUQifQ.XUWZg4ahLJi7_-seiMqF2Wh0BmtN983T7fPMYdz9bb8"}
datas={"vin":""}
def vhcRoute(data):
    # datas["vin"]=data
    url="https://ruisa-dev.intranet.ruixiude.com:15933/rt/v1/newbizmodel/vhcRoute/mergeRoute?vin="+data
    res=requests.get(url=url,headers=headers).json()
    return res


a="111"
a.split()

r= open(r'C:\Users\wangsheng\Desktop\vin.csv')
w= open(r'C:\Users\wangsheng\Desktop\vin1.csv',"w",newline='')
r_csv = list(csv.reader(r))
print(r_csv)
w_csv = csv.writer(w)
w_csv.writerow(["vin","totalTime","beginGps","endGps","totalKm","totalFuel","beginTime","endTime","routeCounter","开始位置","结束位置"])
for i in r_csv:
    res= vhcRoute(i[0])
    for j in res["data"]:
        totalTime=j["totalTime"]
        beginGps=j["beginGps"]
        endGps=j["endGps"]
        vin=j["vin"]
        totalKm=j["totalKm"]
        totalFuel=j["totalFuel"]
        beginTime=j["beginTime"]
        endTime=j["endTime"]
        routeCounter=j["routeCounter"]
        list=[vin+"\t",totalTime,beginGps,endGps,totalKm,totalFuel,beginTime,endTime,routeCounter]
        url1="https://restapi.amap.com/v3/assistant/coordinate/convert?coordsys=gps&output=JSON&key=6e0cea83085499ef58bb03cd785a355a&locations="+beginGps
        res1=requests.get(url=url1).json()
        url2="https://restapi.amap.com/v3/geocode/regeo?radius=50&key=6e0cea83085499ef58bb03cd785a355a&extensions=all&location="+res1["locations"]
        res2=requests.get(url=url2).json()
        list.append(res2["regeocode"]["formatted_address"])
        gps=endGps.split("|")
        for i in gps:
            url3="https://restapi.amap.com/v3/assistant/coordinate/convert?coordsys=gps&output=JSON&key=6e0cea83085499ef58bb03cd785a355a&locations="+i
            res3=requests.get(url=url3).json()
            url4="https://restapi.amap.com/v3/geocode/regeo?radius=50&key=6e0cea83085499ef58bb03cd785a355a&extensions=all&location="+res3["locations"]
            res4=requests.get(url=url4).json()
            list.append(res4["regeocode"]["formatted_address"])
        w_csv.writerow(list)





