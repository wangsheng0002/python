import configparser

"""
# 因为python2的模块名命名的规范没有统一, 所以在python2中导入方式是:  import ConfigParser
# 基于这种模块的运用, 文件的后缀名结尾一般命名成2种格式: 文件.ini 或者 文件.cfg
"""
config = configparser.ConfigParser()
config.read(r'D:\pythonFile\python\test00\a.ini')

# 查看所有的标题: 获取文件中所有的"sections". 返回值一个列表类型, 列表中的元素。对应着每一个section。
print(config.sections())  # ['section1', 'section2']

# 查看标题section1下所有key=value的key: 获取文件中对应的"section1"下所有的"options"。返回值一个列表类型, 列表中的元素。对应着当前"section"中的每一个option
print(config.options('section1'))  # ['k1', 'k2', 'user', 'age', 'is_admin', 'salary']

# 查看标题section1下所有key=value的(key,value)格式: 返回类似于这种格式[(option1, value1), (option2, value2)]
print(config.items('section1'))  # [('k1', 'v1'), ('k2', 'v2'), ('user', 'egon'), ('age', '18'), ('is_admin', 'true'), ('salary', '31.1')]

# 查看标题section1下user的值: 获取文件中"section1"下的"user"这个options对应的值. 返回的是字符串类型
print(config.get('section1', 'k2'))  # v2
res = config.get('section1', 'user')
print(res, type(res))  # egon <class 'str'>

# 查看标题section1下age的值: 返回整型int类型
res = int(config.get('section1', 'age'))
print(res, type(res))  # 18 <class 'int'>
res = config.getint('section1', 'age') # 替代上面使用int的方式
print(res, type(res))  # 18 <class 'int'>

# 查看标题section1下is_admin的值: 返回布尔值
res = config.getboolean('section1', 'is_admin')
print(res, type(res))  # True <class 'bool'>

# 查看标题section1下salary的值: 返回浮点型
res = config.getfloat('section1', 'salary')
print(res, type(res))  # 31.1 <class 'float'>

import configparser

config = configparser.ConfigParser()
config.read('a.cfg', encoding='utf-8')

# 删除整个标题section2
config.remove_section('section2')

# 删除标题section1下的某个k1和k2
config.remove_option('section1', 'k1')
config.remove_option('section1', 'k2')

# 判断是否存在某个标题
print(config.has_section('section1'))

# 判断标题section1下是否有user
print(config.has_option('section1', ''))

# 添加一个标题
config.add_section('egon')

# 在标题egon下添加name=egon,age=18的配置
config.set('egon', 'name', 'egon')
# config.set('egon', 'age', 18)  # 报错,必须是字符串

# 最后将修改的内容写入文件,完成最终的修改
config.write(open('a.cfg', 'w'))


import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
