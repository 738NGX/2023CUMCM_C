import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

mpl.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False

# 读取csv文件并转换为DataFrame对象
df = pd.read_csv('./export/dataset.csv',index_col=0)

# 将日期列转换为datetime类型
df['日期'] = pd.to_datetime(df['日期'])

# 按分类名称和日期对数据进行分组，并计算每个组的销售总量
grouped = df.groupby(['分类名称', '日期'])['销量(千克)'].sum()

# 将分组结果转换为DataFrame对象
result = grouped.reset_index()

# 按分类名称分组，并计算每个分类名称下每日总销量的平均值、标准差、最大值、最小值、偏度、峰度、样本数和变异系数
stats = result.groupby('分类名称')['销量(千克)'].agg(['mean', 'std', 'max', 'min', 'skew', kurtosis, 'count', 'mad'])

# 将所有分类名称的统计结果汇总成表
summary = pd.concat([stats], axis=1)
summary.columns=['平均值','标准差','最大值','最小值','偏度','峰度','样本数','变异系数']

# 打印汇总表
# summary.to_csv('./export/q1_1品类_描述分析.csv')

# 绘制箱线图
fig, axs = plt.subplots(nrows=1, ncols=6, figsize=(15, 5))

for i, category in enumerate(result['分类名称'].unique()):
    axs[i].boxplot(result[result['分类名称'] == category]['销量(千克)'], labels=[category])
    axs[i].set_title(category)

plt.subplots_adjust(wspace=0.5)
plt.show()

# 计算相关系数矩阵
distance_matrix = np.sqrt((1 - summary.T.corr()) / 2)

sns.heatmap(distance_matrix, annot=True, cmap='Blues')

plt.title('相关系数矩阵')
plt.xlabel('分类名称')
plt.ylabel('分类名称')

plt.show()