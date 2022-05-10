from kafka import KafkaProducer
import json


'''
数据中台向业务中台通知“超长怠速” 事件发生
主题 topic：TRANSPORT-SOM-EVENT

-- 超长怠速开始（注意是超长的时候，才通知，非一开始就通知）
{
  "subEvtId": "1475779418512297984",
  "modelId": "124",
  "eventCode": "LTIE-START",#事件编码,超长怠速，long time idle engine）
  "vin": "LWLDAANG4LL003153",#vin
  "startTime": "2022-01-05 07:11:53",#怠速开始时间
  "endTime": "2022-01-05 07:21:53",#怠速结束时间
  "envTemp"  "-5",#环境温度，单位:摄氏度
  "t0Time": "60",#怠速工况标准时间t0,单位秒
  "longitude": "120.334145",#GPS经度
  "latitude": "31.507029",#GPS纬度
}
{
  "subEvtId": "1475779418512297984",
  "modelId": "124",
  "eventCode": "LTIE-STOP",#事件编码,超长怠速，long time idle engine）
  "vin": "LWLDAANG4LL003153",#vin
  "startTime": "2022-01-05 07:11:53",#怠速开始时间
  "endTime": "2022-01-05 07:21:53",#怠速结束时间
   "envTemp"  "-5",#环境温度，单位:摄氏度
  "useFuel": "58.4",#降油潜力
  'fuelConsum':5,  # 事件开始到结束所消耗燃油，单位L。（会计算平均油耗速度，统计节已节油使用，避免再次查询数据中台，减少交互次数）
  "t0Time": "60",#怠速工况标准时间t0,单位秒
  "longitude": "120.334145",#GPS经度
  "latitude": "31.507029",#GPS纬度
  "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的作业货场怠速时间过长行为。
相关参数输出：VIN、起止时间、持续时间T、 GPS位置、降油潜力xx升"
}
业务中台通知应用前台语音播报
kafka消息：
主题： BIZMODEL-PUB-VOICE
 {
    'vin': "1001",                          # 车辆识别码
    'subEvtId': 1001,                       # 订阅id
    'svcCode':'LTIE-SVC',                   # 服务编码
    'msg':"车辆XXX在XXX-XXX时段，出现持续XX秒的作业货场怠速时间过长行为。
相关参数输出：VIN、起止时间、持续时间T、 GPS位置、降油潜力xx升"
}
业务中台向数据中台反馈语音播报是否发生
主题 topic：’BIZMODEL-VOICEACK’

`{
  "eventCode": "LTIE",
  "subSvcId": "1480485334876819456",
  "vin": "LFV2A1150H1199113",
  "state": "1",
  "time": "2022-01-11 19:32:01"
}`
数据中台向业务中台反馈是否遵从，监测周期内，是否遵从都要发送消息

主题 ‘TRANSPORT-SOM-EVENT’

 {
 "vin":vin,
 "subSvcId":subSvcId,
 "modelId":modelid,
 'eventCode':'LTIE-OBEY-END',        # 事件编码
 'status':1,             # 事件状态码
 "startTime":now_time,
 }
'''
start= {
    "subEvtId": 1001,
    "modelId": "118",
    "eventCode": "LTIE-START",#事件编码,超长怠速，long time idle engine）
    "vin": "1001",#vin
    "startTime": "2022-01-06 13:50:00",#怠速开始时间
    "endTime": "2022-01-06 14:00:00",#怠速结束时间
    "envTemp": "-5",#环境温度，单位:摄氏度
    "t0Time": "60",#怠速工况标准时间t0,单位秒
    "longitude": "120.334145",#GPS经度
"latitude": "31.507029"#GPS纬度
}

end={
    "subEvtId": 1001,
    "modelId": "118",
    "eventCode": "LTIE-STOP",#事件编码,超长怠速，long time idle engine）
    "vin": "1001",#vin
    "startTime": "2022-01-06 13:55:00",#怠速开始时间
    "endTime": "2022-01-06 14:00:00",#怠速结束时间
    "envTemp" : "-5",#环境温度，单位:摄氏度
    "useFuel": "58.4",#降油潜力
    'fuelConsum':5,  # 事件开始到结束所消耗燃油，单位L。（会计算平均油耗速度，统计节已节油使用，避免再次查询数据中台，减少交互次数）
    "t0Time": "60",#怠速工况标准时间t0,单位秒
    "longitude": "120.334145",#GPS经度
    "latitude": "31.507029",#GPS纬度
    "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的作业货场怠速时间过长行为,相关参数输出：VIN、起止时间、持续时间T、 GPS位置、降油潜力xx升"
}

VOICE={
    'vin': "1001",                          # 车辆识别码
    'subEvtId': 1001,                       # 订阅id
    'svcCode':'LTIE-SVC',                   # 服务编码
    'msg':"车辆XXX在XXX-XXX时段，出现持续XX秒的作业货场怠速时间过长行为,相关参数输出：VIN、起止时间、持续时间T、 GPS位置、降油潜力xx升"
}
VOICEACK={
    "eventCode": "LTIE",
    "subSvcId": 1001,
    "vin": "1001",
    "state": "1",
    "time": "2022-01-06 13:55:00"
}
comply={
    "vin":"1001",
    "subSvcId":1001,
    "modelId":"118",
    'eventCode':'LTIE-OBEY-END',        # 事件编码
    'status':1,             # 事件状态码
    "startTime":"2022-01-06 14:00:00"
}


'''连接kafka'''
producer = KafkaProducer(bootstrap_servers="10.192.33.204:9092")
'''开始热机'''
producer.send("TRANSPORT-SOM-EVENT",json.dumps(start).encode("utf-8"))
'''业务中台通知应用前台语音播报'''
producer.send("BIZMODEL-PUB-VOICE",json.dumps(VOICE).encode("utf-8"))
'''业务中台向数据中台通知是否语音播报'''
producer.send("BIZMODEL-VOICEACK",json.dumps(VOICEACK).encode("utf-8"))
'''热机结束'''
producer.send("TRANSPORT-SOM-EVENT",json.dumps(end).encode("utf-8"))
'''遵从开始结束'''
producer.send("TRANSPORT-SOM-EVENT",json.dumps(comply).encode("utf-8"))
