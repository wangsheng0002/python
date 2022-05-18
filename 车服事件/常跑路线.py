import requests,json


header={"access_id":"H-0418cd7800x0001-620c041f501400x0002",
       "Content-Type": "application/json",
        "access_key":"0d71fe0eea05bc3af3920384395bf8a5373dafa6e2aeff5597b1dd2a7d696541"}
url="http://wf-dev.intranet.ruixiude.com:16015/apidoc/index?name=business_route#"
"'描述： 获取车辆最近停靠点'"
url1=url+"route_service/get_near_area_points"
data1={"wf_req":{"ver":"1.0","trace_id":"","res_id":"","tenat_id":""},"invoke":{"method":"route_service/get_near_area_points","params":{"count":4,"vin":"LFWSRXSJ6J1F14273","_global":{}}}}
"'描述： 创建常跑线路'"
url2=url+"route_service/create_route_rule"
"'描述： 获取常跑线路'"
url3=url+"route_service/get_route_rules"
"'描述：  删除常跑线路'"
url4=url+"route_service/remove_route_rule"
"'描述： 根据常跑线路，取趟次列表'"
url5=url+"route_service/get_routes"
"'描述： 获取趟次详情'"
url6=url+"route_service/get_route"




def add():
    num = 0
    while True:
        yield num
        num += 1

a = add()
print(next(a))
print(next(a))
print(next(a))