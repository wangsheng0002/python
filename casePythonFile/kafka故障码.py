import requests,json,time,csv
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.structs import TopicPartition


'''dev是开发环境，test是测试环境'''
testEnvironment = "dev"
host="10.192.33.78:9092"
headers = {"Authorization": None}
'''登录信息'''
url= "https://ruisa-" + testEnvironment +".intranet.ruixiude.com:15933/rt/v1/pms/manage/user/login"

data={
    "username": "admin_IDSBID",
    "password": "360e46f15f432af83c77017177a759aba8a58519",
    "clientId": "",
    "imgCode": "",
    "system": 2
}
'''#获取所有的上架服务接口信息'''
listByUpstate_url = "https://ruisa-" + testEnvironment + ".intranet.ruixiude.com:15933/rt/v1/bizmodel/evt/subEventRef/listByUpstate"
listByUpstate_type = "get"
'''#根据车辆VIN订阅所有服务接口信息'''
subEvts_url = "https://ruisa-" + testEnvironment + ".intranet.ruixiude.com:15933/rt/v1/bizmodel/evt/subEventRef/subEvts"
subEvts_type = "post"
subEvts_data = {
    "vin": None,
    "vehicleModelCode": None,
    "evtIds": None
}
'''#查询VIN所有的订阅服务接口信息'''
getEvtByVin_url = "https://ruisa-"+testEnvironment+".intranet.ruixiude.com:15933/rt/v1/bizmodel/evt/subEventRef/getEvtByVin"
getEvtByVin_type = "get"
getEvtByVin_data = {
    "vin": None,
}

'''故障码信息'''
msg = {
    "eventCode": "evt_dtc",
    "dtc": [
        {
            "spn": "",
            "fmi": "",
            "pcode": "P011500"
        }
    ],
    "pickTime": int(time.time()),
    "protocolCode": "",
    "vin": ""
}

class Rui():

    def __init__(self):
        self.req = requests.session()
        self.token = self.req.post(url=url, json=data).json()
    def dtc(self):
        headers["Authorization"] = self.token["data"]["token"]
        a = self.req.request(method=listByUpstate_type, url=listByUpstate_url,
                             headers=headers).json()

    def Evts(self, vin, vehicleModelCode):
        headers["Authorization"] = self.token["data"]["token"]
        '''获取上架列表'''
        a = self.req.request(method=listByUpstate_type, url=listByUpstate_url,
                                  headers=headers).json()
        print("获取上架列表成功")

        '''订阅上架事件'''
        subEvts_data["vin"] = vin
        subEvts_data["vehicleModelCode"] = vehicleModelCode
        for i in a["data"]:
            '''根据服务id进行订阅'''
            subEvts_data["evtIds"] = i['id']
            b = self.req.request(method=subEvts_type, url=subEvts_url, headers=headers,
                                 data=subEvts_data).json()
        print("订阅上架事件成功")

        # '''订阅的结果'''
        # getEvtByVin_data["vin"]=vin
        # c = self.req.request(method=getEvtByVin_type, url=getEvtByVin_url, headers=headers,
        #                         data=getEvtByVin_data).json()
        # for i in c["data"]:
        #     if i["name"]=="故障码事件":
        #         result=i["subEvtId"]
        #         print("车辆%s的故障码事件subEvtId:%s"%(vin,i["subEvtId"]))
    def Producer(self,protocolCode,vin):
        producer = KafkaProducer(bootstrap_servers=host)  # 连接kafka
         # 发送内容,必须是bytes类型
        # msg["dtc"]=dtc
        msg["protocolCode"]=protocolCode
        msg["vin"]=vin
        producer.send("RXD-SOM-EVENT", json.dumps(msg).encode("utf-8"))  # 发送的topic为RXD-SOM-EVENT
        print("kafka推送成功------------------------------------------------------------")
        producer.close()

    def Consumer(self,vin):
        a=[]
        consumer = KafkaConsumer(group_id="mygroup", bootstrap_servers=host, auto_offset_reset="latest",
                                 consumer_timeout_ms=1000)
        # consumer.assign([TopicPartition(topic='BIZMODEL-EVENT-DTC', partition=0)])
        # consumer.seek(TopicPartition(topic='BIZMODEL-EVENT-DTC', partition=0), offset=2113583)
        consumer.subscribe("BIZMODEL-EVENT-DTC")
        for msg in consumer:
            if vin in msg.value.decode():
                a.append(msg.value.decode())
        consumer.close()

        print("消费完成-----------------------------------------------------------------",a)
        return a

if __name__ == '__main__':
    rui=Rui()
    r= open(r'C:\Users\wangsheng\Desktop\新建.csv')
    r_csv = list(csv.reader(r))

    w= open(r'C:\Users\wangsheng\Desktop\新建2.csv',"w",newline='')
    w_csv = csv.writer(w)
    head=r_csv[0]
    head.extend(["一级内容","二级内容","三级内容","四级内容","描述"])
    w_csv.writerow(head)
    vehicleModelCode=""
    i=0
    vins="test123456aabbcc"
    for row in r_csv[1:]:

        if row[2]==vehicleModelCode:
            vin=vins+str(i)
            msg["dtc"][0]["spn"]=row[5]
            msg["dtc"][0]["fmi"]=row[4]
            msg["dtc"][0]["pcode"]=row[3]
            rui.Producer(vin=vin,protocolCode="123456789")
            c=rui.Consumer(vin=vin)
            bb=eval(c[0])
            if bb["cfgDtcList"]!=[]:
                row.extend(["一级"])
                if "dtcResolveTemplate" in bb["cfgDtcList"][0].keys():
                    if bb["cfgDtcList"][0]["dtcResolveTemplate"]!=[]:
                        row.extend(["二级"])
                else:
                    row.extend([""])
                if "selfSolutionList" in bb["cfgDtcList"][0].keys():
                    if bb["cfgDtcList"][0]["selfSolutionList"]!=[]:
                        row.extend(["三级","四级"])
                else:
                    row.extend(["",""])
            else:
                row.extend(["","","","","异常"])
            w_csv.writerow(row)
        else:
            i=i+1
            vin=vins+str(i)
            vehicleModelCode=row[2]
            rui.Evts(vin=vin,vehicleModelCode=vehicleModelCode)
            msg["dtc"][0]["spn"]=row[5]
            msg["dtc"][0]["fmi"]=row[4]
            msg["dtc"][0]["pcode"]=row[3]
            rui.Producer(vin=vin,protocolCode="123456789")
            c=rui.Consumer(vin=vin)
            bb=eval(c[0])
            if bb["cfgDtcList"]!=[]:
                row.extend(["一级"])
                if "dtcResolveTemplate" in bb["cfgDtcList"][0].keys():
                    if bb["cfgDtcList"][0]["dtcResolveTemplate"]!=[]:
                        row.extend(["二级"])
                else:
                    row.extend([""])
                if "selfSolutionList" in bb["cfgDtcList"][0].keys():
                    if bb["cfgDtcList"][0]["selfSolutionList"]!=[]:
                        row.extend(["三级","四级"])
                else:
                    row.extend(["",""])

            else:
                row.extend(["","","","","异常"])
            w_csv.writerow(row)
        print("完成第一个车型%s"%vin)




    # rui=Rui()
    # rui.Evts(vin="aa1234567",vehicleModelCode="000905022")
    # rui.Producer(vin="aa1234567",protocolCode="1495959397954818051")
    # rui.Consumer()


