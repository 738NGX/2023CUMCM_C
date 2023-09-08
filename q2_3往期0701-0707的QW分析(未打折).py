import pandas as pd

df=pd.read_csv('./export/q2_2往期品类销量定价关系汇总.csv')

df['日期'] = pd.to_datetime(df['日期'])
mask = (((df['日期'] >= '2020-07-01') & (df['日期'] <= '2020-07-07')) | 
        ((df['日期'] >= '2021-07-01') & (df['日期'] <= '2021-07-07')) |
        ((df['日期'] >= '2022-07-01') & (df['日期'] <= '2022-07-07'))
       )
df = df.loc[mask]
df=df.set_index(['日期'])
result=pd.DataFrame(columns=['W_水生根茎类', 'W_花叶类', 'W_花菜类', 'W_茄类', 'W_辣椒类', 'W_食用菌'])
for typ in df['分类名称'].unique():
    df0=df[df['分类名称']==typ]
    result[f'W_{typ}']=df0['销售单价(元/千克)_否']/df0['批发价格(元/千克)_否']-1
    
result.to_csv('./export/q2_3往期0701-0707的W分析(未打折).csv')

result=pd.DataFrame(columns=['Q_水生根茎类', 'Q_花叶类', 'Q_花菜类', 'Q_茄类', 'Q_辣椒类', 'Q_食用菌'])

for typ in df['分类名称'].unique():
    df0=df[df['分类名称']==typ]
    result[f'Q_{typ}']=df0['销量(千克)_否']
    
result.to_csv('./export/q2_3往期0701-0707的Q分析(未打折).csv')