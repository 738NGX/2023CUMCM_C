import pandas as pd
from scipy.stats import skew, kurtosis

# 读取csv文件并转换为DataFrame对象
df = pd.read_csv('./export/dataset.csv',index_col=0)

# 将日期列转换为datetime类型
df['日期'] = pd.to_datetime(df['日期'])

# 按分类名称和日期对数据进行分组，并计算每个组的销售总量
grouped = df.groupby(['单品名称', '日期'])['销量(千克)'].sum()

# 将分组结果转换为DataFrame对象
result = grouped.reset_index()

# 按分类名称分组，并计算每个分类名称下每日总销量的平均值、标准差、最大值、最小值、偏度、峰度、样本数和变异系数
stats = result.groupby('单品名称')['销量(千克)'].agg(['mean', 'std', 'max', 'min', 'skew', kurtosis, 'count', 'mad'])

# 将所有分类名称的统计结果汇总成表
summary = pd.concat([stats], axis=1)
summary.columns=['平均值','标准差','最大值','最小值','偏度','峰度','样本数','变异系数']

# 打印汇总表
summary.to_csv('./export/q1_2单品_描述分析.csv')