import time,datetime
a=datetime.datetime.now().replace(microsecond=0)
print(a)
# a=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( ))
# print(a)
# print(type(a))
# c=datetime.datetime.strptime(a,"%Y-%m-%d %H:%M:%S")
# print(c+datetime.timedelta(days=5))
# print(type(c))

settime={
    "a":"2022-01-06 10:00:00"
}