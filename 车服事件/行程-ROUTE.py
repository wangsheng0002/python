'''
行程信息会存储在 t_vhc_route 表中

-- 行程开始
{
‘eventCode’: ‘TRANSPORT_STATUS_CHANGE’, # 状态码
‘vin’: “1001”, # 车辆识别码
‘subEvtId’: 1001, # 订阅id
‘wcdtCode’:4, # 启动
‘conditionNumber’:”RXD_GK_DL_HY_dai_su_V1.0” # 工况编号
‘startTime’:”2021-11-24 19:44:15”, # 工况的开始时间
‘endTime’:”2021-11-24 19:44:50”, # 工况的结束时间
‘oilConsumption’:100, # 工况的油耗
‘startMileage’:50, # 工况的开始里程
‘endMileage’:100, # 工况的结束里程
‘startLongitude’:last_s_lng, # 工况的开始经度
‘startLatitude’:last_s_lat, # 工况的开始纬度
‘endLongitude’:last_e_lng, # 工况的结束经度
‘endLatitude’:last_e_lat, # 工况的结束纬度
}
-- 行程结束
{
‘eventCode’: ‘TRANSPORT_STATUS_CHANGE’, # 状态码
‘vin’: “1001”, # 车辆识别码
‘subEvtId’: 1001, # 订阅id
‘wcdtCode’:2, # 启动
‘conditionNumber’:”RXD_GK_DL_HY_dai_su_V1.0” # 工况编号
‘startTime’:”2021-11-24 19:44:15”, # 工况的开始时间
‘endTime’:”2021-11-24 19:44:50”, # 工况的结束时间
‘oilConsumption’:100, # 工况的油耗
‘startMileage’:50, # 工况的开始里程
‘endMileage’:100, # 工况的结束里程
‘startLongitude’:last_s_lng, # 工况的开始经度
‘startLatitude’:last_s_lat, # 工况的开始纬度
‘endLongitude’:last_e_lng, # 工况的结束经度
‘endLatitude’:last_e_lat, # 工况的结束纬度
}
'''


start={
    "eventCode": "TRANSPORT_STATUS_CHANGE", # 状态码
    "vin": "1001",# 车辆识别码
    "subEvtId": 1001, # 订阅id
    "wcdtCode":4, # 启动
    "conditionNumber":"RXD_GK_DL_HY_dai_su_V1.0",# 工况编号
    "startTime":"2022-01-06 10:00:00",# 工况的开始时间
    "endTime":"2022-01-06 10:00:00", # 工况的结束时间
    "oilConsumption":100, # 工况的油耗
    "startMileage":50, # 工况的开始里程
    "endMileage":100, # 工况的结束里程
    "startLongitude":120.334145, # 工况的开始经度
    "startLatitude":31.507029, # 工况的开始纬度
    "endLongitude":120.334145, # 工况的结束经度
    "endLatitude":31.507029, # 工况的结束纬度
}

end={
    "eventCode": "TRANSPORT_STATUS_CHANGE", # 状态码
    "vin": "1001",# 车辆识别码
    "subEvtId": 1001, # 订阅id
    "wcdtCode":2, # 停机
    "conditionNumber":"RXD_GK_DL_HY_dai_su_V1.0",# 工况编号
    "startTime":"2022-01-06 14:00:00",# 工况的开始时间
    "endTime":"2022-01-06 14:00:00", # 工况的结束时间
    "oilConsumption":100, # 工况的油耗
    "startMileage":50, # 工况的开始里程
    "endMileage":100, # 工况的结束里程
    "startLongitude":120.334145, # 工况的开始经度
    "startLatitude":31.507029, # 工况的开始纬度
    "endLongitude":120.334145, # 工况的结束经度
    "endLatitude":31.507029, # 工况的结束纬度
}

