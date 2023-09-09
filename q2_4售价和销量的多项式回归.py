import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
warnings.filterwarnings("ignore")
mpl.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False

# 不打折
df=pd.read_csv('./export/q2_2往期品类销量定价关系汇总(去除离群值).csv')

df['日期'] = pd.to_datetime(df['日期'])
mask = (
     ((df['日期'] >= '2023-06-01') & (df['日期'] <= '2023-06-30'))
    )
#df = df.loc[mask]
df=df.set_index(['日期'])

for typ in df['分类名称'].unique():
    df0=df[df['分类名称']==typ].copy()

    # 绘制散点图
    plt.scatter(df0['销量(千克)_否'].values, df0['批发价格(元/千克)_否'].values)
    plt.xlabel('销量(千克)_否')
    plt.ylabel('批发价格(元/千克)_否')
    plt.title(typ)
    
    # 计算总销量
    total_sales = df0['销量(千克)_否'].sum()

    # 计算权重
    df0['weights'] = df0['销量(千克)_否'] / total_sales
    
    # 多项式拟合
    x = df0['销量(千克)_否'].values
    y = df0['批发价格(元/千克)_否'].values
    weights = df0['weights'].values
    z = np.polyfit(x, y, 2, w=weights)
    p = np.poly1d(z)
    print(f"{typ}t统计量的值为: {z[1] / np.sqrt(z[2])}")
    print(f"多项式系数为: {z}")
    
    # 画出拟合线
    xp = np.linspace(x.min(), x.max(), 100)
    plt.plot(xp, p(xp), color='red')
    plt.show()
    
    result=pd.concat([result,df0],axis=0)
    
# 打折
df=pd.read_csv('./export/q2_2往期品类销量定价关系汇总(去除离群值).csv')

df['日期'] = pd.to_datetime(df['日期'])
mask = (
     ((df['日期'] >= '2023-06-01') & (df['日期'] <= '2023-06-30'))
    )
#df = df.loc[mask]
df=df.set_index(['日期'])

for typ in df['分类名称'].unique():
    df0=df[df['分类名称']==typ].copy()

    # 绘制散点图
    plt.scatter(df0['销量(千克)_是'].values, df0['批发价格(元/千克)_是'].values)
    plt.xlabel('销量(千克)_是')
    plt.ylabel('批发价格(元/千克)_是')
    plt.title(typ)
    
    # 计算总销量
    total_sales = df0['销量(千克)_是'].sum()

    # 计算权重
    df0['weights'] = df0['销量(千克)_是'] / total_sales
    
    # 多项式拟合
    x = df0['销量(千克)_是'].values
    y = df0['批发价格(元/千克)_是'].values
    weights = df0['weights'].values
    z = np.polyfit(x, y, 2, w=weights)
    p = np.poly1d(z)
    print(f"{typ}t统计量的值为: {z[1] / np.sqrt(z[2])}")
    print(f"多项式系数为: {z}")
    
    # 画出拟合线
    xp = np.linspace(x.min(), x.max(), 100)
    plt.plot(xp, p(xp), color='red')
    plt.show()
    
    result=pd.concat([result,df0],axis=0)