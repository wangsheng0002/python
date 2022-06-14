import datetime

from  openpyxl import  Workbook

# 实例化
wb = Workbook()
# 激活 worksheet
ws = wb.active
# 方式一：数据可以直接分配到单元格中(可以输入公式)
ws['A1'] = 42
# 方式二：可以附加行，从第一列开始附加(从最下方空白处，最左开始)(可以输入多行)
ws.append([1, 2, 3])
# 方式三：Python 类型会被自动转换
ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")
wb.save('test.xlsx')

