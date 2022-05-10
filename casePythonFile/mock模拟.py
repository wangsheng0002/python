
import unittest
from unittest import mock
'''
mock 可以通过指定返回值的方式模拟一个函数
在函数可以使用时，通过 side_effect 指定函数
可以指定一个可迭代对象，每次调用该方法就会返回不一样的值，当对象的值循环完之后就会报错
'''


class Foo:
    def bar(self):
        return 3
    def bar1(self):
        # 不会实际调用
        pass


class TestFoo():
    def test_bar(self):
        foo = Foo()
        # 指定函数返回值
        foo.bar = mock.Mock(return_value=1, side_effect=foo.bar)
        result = foo.bar()
        print(result)
        foo.bar1 = mock.Mock(return_value=1)
        result = foo.bar1()
        print(result)
        # 指定函数返回值
        foo.bar = mock.Mock(side_effect=[1, 2, 3])
        for i in range(3):
            print(foo.bar())



if __name__ == '__main__':
    TestFoo().test_bar()

