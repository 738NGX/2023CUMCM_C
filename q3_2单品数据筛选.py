import pandas as pd

df=pd.read_csv('./export/q3_1单品每日批发售价销量损耗率汇总.csv')

mask=((df['日期'] >= '2023-06-24') & (df['日期'] <= '2023-06-30'))
df0=df[mask].copy()
df0['单品名称'].unique().size,df['单品名称'].unique().size

mask = df['单品名称'].isin(df0['单品名称'].unique())
df_filtered = df[mask]

df_filtered.to_csv('./export/q3_2单品数据筛选.csv')