import pandas as pd

# 读取csv文件并转换为DataFrame对象
df = pd.read_csv('./export/dataset.csv',index_col=0)

# 将日期列转换为datetime类型
df['日期'] = pd.to_datetime(df['日期'])

# 筛选出历史上前期和同期的数据
mask = (((df['日期'] >= '2020-07-01') & (df['日期'] <= '2020-07-07')) | 
        ((df['日期'] >= '2021-06-01') & (df['日期'] <= '2021-07-07')) |
        ((df['日期'] >= '2022-06-01') & (df['日期'] <= '2022-07-07')) |
        ((df['日期'] >= '2023-06-01') & (df['日期'] <= '2023-06-30')) 
       )
df = df.loc[mask]

# 按分类名称和日期对数据进行分组，并计算每个组的批发价格平均值
grouped = df.groupby(['分类名称', '日期'])['批发价格(元/千克)'].mean()

# 将分组结果转换为DataFrame对象
result = grouped.reset_index()

result.to_csv('./export/q2_1往期品类批发价格汇总.csv')