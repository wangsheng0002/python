'''
a）键值对形式
user: admin
pwd: 123
job:
  - teacher
  - nurese
输出为：{'user': 'admin', 'pwd': 123, 'job': ['teacher', 'nurese']}

b）序列list
- admin1: 123456
- admin2: 111111
- admin3: 222222
输出：[{'admin1': 123456},
      {'admin2': 111111},
      {'admin3': 222222}]

c）纯量str

n1: 52.10
输出：{'n1': 52.1}

n2: true
n3: false    #不区分大小写
输出：{'n2': True, 'n3': False}

None用~表示
n4: ~
输出：{'n4': None}


d）强制转换，使用!!
n7: !!str true
输出：{'n7': 'true'}

e）多个文件：一个yaml文件里存在多个文件，用---表示，只能一起读取，不能分开读取



'''


'''3.yaml文件的读取xx.yaml'''
import yaml

#由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
# yaml.warnings({'YAMLLoadWarning':False})
f=open('1.yaml','r',encoding='utf-8')      #打开yaml文件
a=f.read()
print(a)
d=yaml.safe_load_all(a)     #将数据转换成python字典行驶输出，存在多个文件时，用load_all，单个的时候load就可以
for data in d:
    print(data)
f.close()

'''输出：
{'user': 'admin', 'pwd': None, 'job': ['teacher', 'nurese']}
{'school': 'erxiao', 'location': 'sky'}'''

# '''单个文件'''
# yaml.warnings({'YAMLLoadWarning':False})
# f=open('1.yaml','r',encoding='utf-8')
# cfg=f.read()
# print(cfg)
# d=yaml.load(cfg)
# print(d)
# f.close()
#
# '''输出：
# user: admin
# pwd: ~
# job:
# - teacher
# - nurese
# {'user': 'admin', 'pwd': None, 'job': ['teacher', 'nurese']}'''



'''写入'''
import yaml
import os



def yaml_doc(yampath):
    data={'school':'erxiao',
          'studens':['lili','jj']}
    file=open(yampath,'w',encoding='utf-8')
    yaml.dump(data,file)
    file.close()

currentpath=os.path.abspath('.')     #获取当前路径
yamlpath=os.path.join(currentpath,'generate.yaml')    #创建yaml文件
yaml_doc(yamlpath)
'''输出：
generate.yaml文件
school: erxiao
studens:
- lili
- jj
```※注意：如果是在已存在数据的yaml文件中执行此脚本，那么数据会被覆盖※```'''