# 导入 csv 库
import csv

# 以读方式打开文件
with open("data.csv", mode="r", encoding="utf-8-sig") as f:

    # 基于打开的文件，创建csv.reader实例
    reader = csv.reader(f)

    # 获取第一行的header
    # header[0] = "设备编号"
    # header[1] = "温度"
    # header[2] = "湿度"
    # header[3] = "转速"
    header = next(reader)

    # 逐行获取数据，并输出
    for row in reader:
        print("{}{}: {}={}, {}={}, {}={}".format(header[0], row[0],
                                                 header[1], row[1],
                                                 header[2], row[2],
                                                 header[3], row[3]))





# 导入 csv 库
import csv

# 打开文件
with open("data.csv", encoding="utf-8-sig", mode="r") as f:

    # 基于打开的文件，创建csv.DictReader实例
    reader = csv.DictReader(f)

    # 输出信息
    for row in reader:
        print("设备编号{}: 温度={}, 湿度={}, 转速={}".format(row["设备编号"],
                                                   row["温度"],
                                                   row["湿度"],
                                                   row["转速"]))







# 导入 csv 库
import csv

# 创建列表，保存header内容
header_list = ["设备编号", "温度", "湿度", "转速"]

# 创建列表，保存数据
data_list = [
    [0, 31, 20, 1000],
    [1, 30, 22, 998],
    [2, 32, 33, 1005]
]

# 以写方式打开文件。注意添加 newline=""，否则会在两行数据之间都插入一行空白。
with open("new_data.csv", mode="w", encoding="utf-8-sig", newline="") as f:

    # 基于打开的文件，创建 csv.writer 实例
    writer = csv.writer(f)

    # 写入 header。
    # writerow() 一次只能写入一行。
    writer.writerow(header_list)

    # 写入数据。
    # writerows() 一次写入多行。
    writer.writerows(data_list)



# 导入 csv 库
import csv

# 创建 header 列表
header_list = ["设备编号", "温度", "湿度", "转速"]

# 创建数据列表，列表的每个元素都是字典
data_list = [
    {"设备编号": "0", "温度": 31, "湿度": 20, "转速": 1000},
    {"设备编号": "1", "温度": 30, "湿度": 22, "转速": 998},
    {"设备编号": "2", "温度": 32, "湿度": 23, "转速": 1005},
]

# 以写方式打开文件。注意添加 newline=""，否则会在两行数据之间都插入一行空白。
with open("new_data.csv", mode="w", encoding="utf-8-sig", newline="") as f:

    # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
    writer = csv.DictWriter(f, header_list)

    # 写入 header
    writer.writeheader()

    # 写入数据
    writer.writerows(data_list)
