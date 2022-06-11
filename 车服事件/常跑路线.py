import requests,json,hashlib
hashlib.sha256()

header={
    "WF-Noise":"1814c327410",
    "WF-Content-Sign": "jUihAQOJo2YlyF3kKcscV6g5ljNli4V70zF+WuGRShM=",
    "Content-Type": "application/json;charset=utf-8",
    "Authorization":"WF-SHA2 H-04700d5900x0002-df13049622a300x0002:25/vJqt/2yzWWRKW8T6MYZYmZ9LSbatCoM688zebtT4=",
    "access_id":"H-04700d5900x0002-df13049622a300x0002",
    "access_key":"5161597ac4adfbe6c5793b048fd71173668682955f6fefcd8990d359fbea1ea1"

}
url="https://api.ruixiude.com/jscf_business_route"
data={
    "wf_req": {
        "ver": "1.0",
        "trace_id": "",
        "res_id": "",
        "tenat_id": ""
    },
    "invoke": {
        "method": "test/get_work_routes",
        "params": {
            "conventional_route_id": "",
            "page": 1,
            "vin": "LFWSRXSJ3KAD57951",
            "_global": {}
        }
    }
}


r=requests.post(url=url,headers=header,data=json.dumps(data)).json()
print(r)



