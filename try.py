'''
练习
    创建包含更多行和列的原始数据集。

    删除缺失值最多的列。
    将预处理后的数据集转换为张量格式。
'''

# 如果没有安装pandas，只需取消对以下行的注释来安装pandas
# !pip install pandas
import pandas as pd
import os

os.makedirs(os.path.join('.', 'data'), exist_ok=True)
data_file = os.path.join('.', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

data = pd.read_csv(data_file)
print(data)
# print(data.isna())

# 使用max_loc来记录缺失值最多的那一列对应的index
loc = 0
max_loc = 0
max = 0

for col in data.columns:
    count = 0
    for i in range(data.shape[0]):
        if data[col].isna().iloc[i] == True:
            count += 1
    if max < count:
        max = count
        max_loc = loc
    loc += 1
print("max: ", max)
print("max_loc: ", max_loc)

data = data.drop(data.columns[max_loc], axis=1)
print("after preprocess: data =", "\n", data)

# 将数据转换为张量：
