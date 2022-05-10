import time
# def getXXXTime():
#     print()
#     return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())
# 如果我们需要在所有这样的函数 返回字符串前面 都加上开头: 当地时间
#
# 这时候，我们完全可以 不去修改原来的函数 ， 而是 使用装饰器 ，像这样

from goto import with_goto
@with_goto
def range(start, stop):
    i = start
    result = []
    label.begin
    print("转到begin")
    if i == stop:
        goto.end
    result.append(i)
    i += 1
    goto.begin
    label.end
    print("转到end")
    return result
range(2, 3)
