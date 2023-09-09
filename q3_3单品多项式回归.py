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
df=pd.read_csv('./export/q3_2单品数据筛选.csv')

df['日期'] = pd.to_datetime(df['日期'])
df=df.set_index(['日期'])

result=pd.DataFrame(columns=['单品名称','t','k1','k2','k3'])

for typ in df['单品名称'].unique():
    df0=df[df['单品名称']==typ].copy()
    
    # 计算总销量
    total_sales = df0['销量(千克)_否'].sum() 
    
    # 计算权重
    df0['weights'] = df0['销量(千克)_否'] / total_sales
    
    # 绘制散点图
    plt.scatter(df0['销售单价(元/千克)_否'].values, df0['销量(千克)_否'].values,alpha=df0['weights'].values/df0['weights'].max())
    plt.xlabel('销售单价(元/千克)_否')
    plt.ylabel('销量(千克)_否')
    plt.title(typ)
    
    # 多项式拟合
    x = df0['销售单价(元/千克)_否'].values
    y = df0['销量(千克)_否'].values
    weights = df0['weights'].values
    z = np.polyfit(x, y, 2, w=weights)
    p = np.poly1d(z)
    
    df0['SSx'] =(df0['销售单价(元/千克)_否'] -df0['销售单价(元/千克)_否'].mean())**2
    df0['ssxy'] = (df0['销售单价(元/千克)_否'] -df0['销售单价(元/千克)_否'].mean())*(df0['销量(千克)_否']-df0['销量(千克)_否'].mean())
    b1 = df0['SSx'].sum()/df0['ssxy'].sum()
    s =  (df0['SSx'].mean()/df0['SSx'].sum())**0.5
    t = (z[0]-b1)/s
    #print(f"{typ}t统计量的值为: {t}")
    #print(f"多项式系数为: {z}")
    
    # 画出拟合线
    xp = np.linspace(x.min(), x.max(), 100)
    plt.plot(xp, p(xp), color='red')
    #plt.show()
    row=pd.DataFrame({'单品名称':typ,'t':t,'k1':z[0],'k2':z[1],'k3':z[2]},index=[0])
    result=pd.concat([result,row],axis=0,ignore_index=True)

result.to_csv('./export/q3_3单品多项式回归.csv')