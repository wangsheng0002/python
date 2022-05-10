# from loguru import logger
#
# # 打印不同类型的日志
# logger.debug("debug  message")
# logger.info("info  message")
# logger.success("success  message")
# logger.warning("warning  message")
# logger.error("error  message")
# logger.critical("critical  message")
#
#
# # 日志格式和存入日志级别
# logger.add("test00.log", format="{time}|{level}|{message}", level="DEBUG")
#
# # 序列化日志
# logger.add("test00.log", serialize=True)
#
# # 按照日志大小自动切割日志，还可以按照时间切割：rotation='00:00'，rotation='1 week'，我们想要设置日志文件最长保留10天，retention='10 days'
# logger.add("test00.log", rotation="50 MB")
#
# # loguru 还可以配置文件的压缩格式，比如使用 zip 文件格式保存
# # logger.add('test00.log', compression='zip')
#
# # 在很多情况下，如果遇到运行错误，而我们在打印输出 log 的时候万一不小心没有配置好 Traceback 的输出，很有可能我们就没法追踪错误所在了。但用了 loguru 之后，我们用它提供的装饰器就可以直接进行 Traceback 的记录，类似这样的配置即可：
# @logger.catch
# def my_function(x, y, z):
#     # An error? It's caught anyway!
#
#     return 1 / (x + y + z)
#
# # 我们做个测试，我们在调用时三个参数都传入 0，直接引发除以 0 的错误，看看会出现什么情况：
# my_function(0, 0, 1)
#
#
# # 运行完毕之后，可以发现 log 里面就出现了 Traceback 信息，而且给我们输出了当时的变量值，真的是不能再赞了！结果如下：


import unittest  # 导入unittest
from loguru import logger


def login(username=None, password=None):
    if username is None or password is None:
        return {"code": "400", "msg": "用户名或密码为空"}
    if username == 'yuz' and password == '123':
        return {"code": "200", "msg": "登录成功"}
    return {"code": "300", "msg": "用户名或密码错误"}


# 添加日志文件
logger.add(sink='test00.log', encoding='utf-8')


class TestLogin(unittest.TestCase):
    def test_login_1(self):
        username = 'li'
        password = '123'
        expected = {"code": "300", "msg": "用户名或密码错误"}
        logger.info('正在执行测试用1...')
        actual = login(username, password)
        self.assertEqual(expected, actual)
        logger.info('测试用例1执行完毕')
    # @logger.catch()
    def test_login_2(self):
        username = 'yuz'
        password = '123'
        expected = {"code": "300", "msg": "用户名或密码错误"}
        logger.info('正在执行测试用2...')
        actual = login(username, password)

        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            # 在日志中记录断言异常
            logger.error('测试用例2失败')
            # 捕获异常后，一定要手动抛出
            raise e
        logger.info('测试用例2执行完毕')
    # @logger.catch()
    def test_login_3(self):
        username = None
        password = '123'
        expected = {"code": "400", "msg": "用户名或密码为空"}
        logger.info('正在执行测试用3...')
        actual = login(username, password)
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            # 在日志中记录断言异常
            logger.error('测试用例3失败')
            # 捕获异常后，一定要手动抛出
            raise e
        logger.info('测试用例3执行完毕')



if __name__ == '__main__':
    unittest.main()


