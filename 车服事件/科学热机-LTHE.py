from kafka import KafkaProducer
import json


"""
 ---科学超长热机开始 （注意是超长的时候才告知，热机一开始不用告知）
 推送主题： TRANSPORT-SOM-EVENT
{
  "subEvtId": "1475779418512297984",
  "modelId": "124",
  "eventCode": "LTHE-START",#事件编码,超长热机 long time heat engine
  "vin": "LWLDAANG4LL003153",#vin
  "startTime": "2022-01-05 07:11:53",#开始时间
  "startWarm": "58.4",#开始水温
   "useTime": "10",#热机时间
  "t0Time": "60",#T0标准时间
  "longitude": "120.334145",#GPS经度
  "latitude": "31.507029",#GPS纬度
  "envTemp" : "-5",#环境温度，单位:摄氏度
}



{
  "subEvtId": "1475779418512297984",
  "modelId": "124",
  "eventCode": "LTHE-STOP",#事件编码,超长热机 long time heat engine
  "wcdtCode":"",#工况编码，启动工况
  "vin": "LWLDAANG4LL003153",#vin
  "startTime": "2022-01-05 07:11:53",#开始时间
  "endTime": "2022-01-05 07:21:53",#结束时间
  "startWarm": "58.4",#开始水温
  "stopWarm": "96.8",#结束水温
  "fuelConsum":5,  # 事件开始到结束所消耗燃油，单位L。（会计算平均油耗速度，统计节已节油使用，避免再次查询数据中台，减少交互次数）
  "useFuel": "58.4",#降油潜力
   "useTime": "10",#热机时间
  "t0Time": "60",#T0标准时间
  "longitude": "120.334145",#GPS经度
  "latitude": "31.507029",#GPS纬度
  "envTemp" : "-5",#环境温度，单位:摄氏度
  "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的冷启动怠速热机时间过长行为。相关参数输出：VIN、起止时间、热机持续时长 、GPS位置、降油潜力xxL"
}
业务中台通知应用前台语音播报
kafka消息：
主题： BIZMODEL-PUB-VOICE
 {
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "svcCode":"LTHE-SVC",                   # 服务编码
    "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的冷启动怠速热机时间过长行为。相关参数输出：VIN、起止时间、热机持续时长 、GPS位置、降油潜力xxL"
}
业务中台通知数据中台语音播报
kafka消息：
主题： BIZMODEL-VOICEACK
 {
    "time": "2022-01-06 12:00:00",
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LTHE",                     # 事件编码
    "state":"1",                          # 1已经语音播报 0 未语音播报
}

数据中台发布：科学热机是否遵从
kafka消息：
topic:TRANSPORT-SOM-EVENT
key:COMPLIANCE_MODEL
message:
 {
 "vin":vin,
 "subEvtId":subSvcId,
 "modelId":120,
 "eventCode":"LTHE-OBEY-END",
 "status":1,# 0 标识未遵从 1标识遵从，在模型识别周期内，是否遵从都要向业务中台发消息通知。业务中台进行统计次数
 "startTime":遵从开始时间,
 "fuelConsumRate":瞬时油耗= 喷油嘴当前喷油速度 ，单位（L/秒）
 "endTime": #结束遵从不需要，热机结束就是一瞬间的事情
}
"""
#推送主题： TRANSPORT-SOM-EVENT
start= {
    "subEvtId": 1001,
    "modelId": "124",
    "eventCode": "LTHE-START",#事件编码,超长热机 long time heat engine
    "vin": "1001",#vin
    "startTime": "2022-01-06 10:00:00",#开始时间
    "startWarm": "58.4",#开始水温
    "useTime": "10",#热机时间
    "t0Time": "60",#T0标准时间
    "longitude": "120.334145",#GPS经度
    "latitude": "31.507029",#GPS纬度
    "envTemp" :"-5"#环境温度，单位:摄氏度
}

end={
    "subEvtId": 1001,
    "modelId": "124",
    "eventCode": "LTHE-STOP",#事件编码,超长热机 long time heat engine
    "wcdtCode":"",#工况编码，启动工况
    "vin": "1001",#vin
    "startTime": "2022-01-06 10:00:00",#开始时间
    "endTime": "2022-01-06 10:10:00",#结束时间
    "startWarm": "58.4",#开始水温
    "stopWarm": "96.8",#结束水温
    "fuelConsum":5,  # 事件开始到结束所消耗燃油，单位L。（会计算平均油耗速度，统计节已节油使用，避免再次查询数据中台，减少交互次数）
    "useFuel": "58.4",#降油潜力
    "useTime": "10",#热机时间
    "t0Time": "60",#T0标准时间
    "longitude": "120.334145",#GPS经度
    "latitude": "31.507029",#GPS纬度
    "envTemp" : "-5",#环境温度，单位:摄氏度
    "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的冷启动怠速热机时间过长行为。相关参数输出：VIN、起止时间、热机持续时长 、GPS位置、降油潜力xxL"
}

VOICE={
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "svcCode":"LTHE-SVC",                   # 服务编码
    "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的冷启动怠速热机时间过长行为。相关参数输出：VIN、起止时间、热机持续时长 、GPS位置、降油潜力xxL"
}
VOICEACK={
    "time": "2022-01-06 10:05:00",
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LTHE",                     # 事件编码
    "state":"1"                          # 1已经语音播报 0 未语音播报
}
comply={
    "vin":"1001",
    "subEvtId":1001,
    "modelId":"124",
    "eventCode":"LTHE-OBEY-END",
    "status":1,# 0 标识未遵从 1标识遵从，在模型识别周期内，是否遵从都要向业务中台发消息通知。业务中台进行统计次数
    "startTime":"2022-01-06 10:05:00",#遵从开始时间,
    "fuelConsumRate":0.003,#瞬时油耗= 喷油嘴当前喷油速度 ，单位（L/秒）
    "endTime":"2022-01-06 10:10:00" #结束遵从不需要，热机结束就是一瞬间的事情
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



