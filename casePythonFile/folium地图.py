import folium
import os,csv,random
from folium import plugins



r= open(r'C:\Users\wangsheng\Desktop\vin - 副本1.csv')
dic={}

vin=""

r_csv = list(csv.reader(r))
for a in  r_csv:
    if a[0] in dic:
        dic[a[0]].append([a[9],a[1],a[6],a[7]])
    else:
        dic.setdefault(a[0],[])
        dic[a[0]].append([a[9],a[1],a[6],a[7]])




for j in dic.keys():

    # list1=[]
    print(dic[j][0])
    x=dic[j][0][0].split("|")[0].split(",")
    m = folium.Map([eval(x[1]),eval(x[0])], tiles= 'http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}',attr= '中国行政区划边界',zoom_start=10)  #中心区域的确定
    for f in dic[j]:
        q="#"+str(hex(random.randint(16,255))[2:])+str(hex(random.randint(16,255))[2:])+str(hex(random.randint(16,255))[2:])
        list1=[]
        gps=f[0].split("|")
        print(f,f[1])
        for k in gps:
            l=k.split(",")
            list1.append([eval(l[1]),eval(l[0])])#输入坐标点（注意）folium包要求坐标形式以纬度在前，经度在后

        route = folium.PolyLine(    #polyline方法为将坐标用线段形式连接起来
            list1,    #将坐标点连接起来
            weight=15,  #线的大小为3
            color= q,  #线的颜色为橙色
            opacity=0.8    #线的透明度
        ).add_to(m)    #将这条线添加到刚才的区域m内
        folium.Marker(
            location=list1[0], # 位置
            popup=f[2]+"绿色起点", # 鼠标点击 弹出的说明
            icon=folium.Icon(icon='cny',color="green") # 图标样式
        ).add_to(m)
        folium.Marker(
            location=list1[-1], # 位置
            popup=f[3]+"红色终点", # 鼠标点击 弹出的说明
            icon=folium.Icon(icon='cny',color="red") # 图标样式
        ).add_to(m)

        folium.plugins.AntPath(
            locations=list1[::-1], reverse="True", dash_array=[20, 30]
        ).add_to(m)
        m.fit_bounds(m.get_bounds())

        # attr = {"fill": "red"}
        # plugins.PolyLineTextPath(
        #     list1,               #坐标
        #     "\u27B8",         #文本或特殊符号
        #     repeat=True,     #重复
        #     offset=6,         #偏移量
        #     attributes=attr   #外观设置
        # ).add_to(m)
        # m.fit_bounds(m.get_bounds())

    m.save(os.path.join(r'C:\Users\wangsheng\Desktop\html', j+".html"))  #将结果以HTML形式保存到桌面上




