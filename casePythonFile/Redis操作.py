import redis
# r = redis.Redis(host='10.192.33.78', port=6379, decode_responses=True, password='testtest')
#
# a=r.lrange("BIZ:LGHS:00001321102800645",0,1)#获取列表元素
# print(a)
# b=r.smembers("BIZ:LGHS:100004")#获取集合元素
# print(b)
# # r.set("aa:bb","1234")
# r.set("aa:bb:CC","1234")
# print(r.get("aa:bb:CC"))


r = redis.Redis(host='121.43.41.1', port=6379, decode_responses=True)
r.set("wangsheng",18)
b=r.get("wangsheng")
print(b)
r.zadd("fruit",{"xiowang":3,"dawang":4,"laowang":2})
c=r.zrange("fruit",0,-1,withscores=True)
print(c)
r.sadd("fruit_other", "香蕉", "葡萄", "柚子")
d=r.smembers('fruit_other')
print(d)
r.hset("yyds","RNG","xiaohu",{"污渍":"zui","嘎啦8":"gala"})
a=r.hget("yyds","污渍")
print(a)
e=r.hmget("yyds","RNG","嘎啦8")
print(e)


