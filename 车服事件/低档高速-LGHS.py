from kafka import KafkaProducer
import json


"""
-- 1.低档高速开始
kafka消息：
topic:TRANSPORT-SOM-EVENT
 {
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LGHS-START",               # 事件编码
    "modelId":"120",                        # 模型id
    "startTime":"2021-12-23 14:43:15",      # 怠速开始时间
    "startGps":[latitude,longitude],        # 低档高速的开始GPS
    "ward":4                                # 低档高速档位
}

--2. 低档高速结束
 {
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LGHS-STOP",                # 事件编码
    "modelId":"120",                        # 模型id
    "startTime":"2021-12-23 14:43:15",      # 怠速开始时间
    "endTime":"2021-12-23 14:59:24",        # 低档高速结束时间
    "startGps":[latitude,longitude],        # 低档高速的开始GPS
    "endGps":[latitude,longitude],          # 低档高速的结束GPS
    "mileage":10,                           # 低档高速工况里程
    "fuel":5,                               # 低档高速工况油耗
    "ward":4,                               # 低档高速档位
    "potentialDegree ":0.05,                # 降油潜力
    "msg":"车辆vin在2022-01-06 10:30 到 2022-01-06 10:35:00 时段,出现持续300秒的低档高速驾驶行为，累计行驶5公里，若按提示及时+1档，将可降低30L油耗"
}
3.业务中台通知应用前台语音播报
kafka消息：
主题： BIZMODEL-PUB-VOICE
发出去的记录，会存储到t_pub_voice 表
 {
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "svcCode":"LGHS-SVC",                   # 服务编码
    "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的冷启动怠速热机时间过长行为。相关参数输出：VIN、起止时间、热机持续时长 、GPS位置、降油潜力xxL"
}
--4.业务中台向数据中台通知是否语音播报
kafka消息：
主题： BIZMODEL-VOICEACK
收到的记录 会存储在 t_voice_ack 表
 {
     "time": "2022-01-06 12:00:00",
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LGHS",                     # 事件编码
    "state":"120",                          # 1已经语音播报 0 未语音播报
}

 --5.遵从开始结束
kafka消息：
topic:TRANSPORT-SOM-EVENT
key:COMPLIANCE_MODEL
message:
遵从记录会存储在 t_comply_stat 表
 {
 "vin":vin,
 "subEvtId":subSvcId,
 "modelId":120,
 "eventCode":"LGHS-OBEY-END",
 "status":1,
 "startTime":startTime,
 "endTime":endTime
}
"""


#主题： TRANSPORT-SOM-EVENT
start={
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LGHS-START",               # 事件编码
    "modelId":"120",                        # 模型id
    "startTime":"2022-01-06 11:00:00",      # 低档高速的开始时间
    "startGps":[31.507029,120.334145],      # 低档高速的开始GPS
    "ward":4                                # 低档高速档位
}
end={
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LGHS-STOP",                # 事件编码
    "modelId":"120",                        # 模型id
    "startTime":"2022-01-06 11:00:00",      # 低档高速的开始时间
    "endTime":"2022-01-06 11:10:00",        # 低档高速结束时间
    "startGps":[31.507029,120.334145],      # 低档高速的开始GPS
    "endGps":[31.507029,120.334145],        # 低档高速的结束GPS
    "mileage":10,                           # 低档高速工况里程
    "fuel":5,                               # 低档高速工况油耗
    "ward":4,                               # 低档高速档位
    "potentialDegree ":0.35,                # 降油潜力
    "msg":"车辆vin在2022-01-06 10:30 到 2022-01-06 10:35:00 时段,出现持续300秒的低档高速驾驶行为，累计行驶5公里，若按提示及时+1档，将可降低30L油耗"
}
#主题： BIZMODEL-PUB-VOICE
VOICE={
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "svcCode":"LGHS-SVC",                   # 服务编码
    "msg":"车辆XXX在XXX-XXX时段，出现持续XX秒的低档高速驾驶行为。相关参数输出：VIN、起止时间、热机持续时长 、GPS位置、降油潜力xxL"
}
#主题： BIZMODEL-VOICEACK
VOICEACK={
    "time": "2022-01-06 11:10:00",
    "vin": "1001",                          # 车辆识别码
    "subEvtId": 1001,                       # 订阅id
    "eventCode":"LGHS",                     # 事件编码
    "state":"1",                          # 1已经语音播报 0 未语音播报
}

#主题： TRANSPORT-SOM-EVENT
comply={
    "vin":"1001",
    "subEvtId":1001,
    "modelId":"120",
    "eventCode":"LGHS-OBEY-END",
    "status":1,
    "startTime":"2022-01-06 11:10:00",
    "endTime":"2022-01-06 11:20:00"
}

'''连接kafka'''
producer = KafkaProducer(bootstrap_servers="10.192.33.204:9092")
'''低档高速开始'''
producer.send("TRANSPORT-SOM-EVENT",json.dumps(start).encode("utf-8"))
'''业务中台通知应用前台语音播报'''
producer.send("BIZMODEL-PUB-VOICE",json.dumps(VOICE).encode("utf-8"))
'''业务中台向数据中台通知是否语音播报'''
producer.send("BIZMODEL-VOICEACK",json.dumps(VOICEACK).encode("utf-8"))
'''低档高速结束'''
producer.send("TRANSPORT-SOM-EVENT",json.dumps(end).encode("utf-8"))
'''遵从开始结束'''
producer.send("TRANSPORT-SOM-EVENT",json.dumps(comply).encode("utf-8"))