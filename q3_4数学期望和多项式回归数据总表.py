import pandas as pd
from sympy import *

df=pd.read_csv('./export/q3_2单品数据筛选.csv')

result=pd.DataFrame(columns=['单品名称','μ','σ','E(C)','E(C^2)','E(C^3)'])

for typ in df['单品名称'].unique():
    df0=df[df['单品名称']==typ].copy()
    miu=df0['批发价格(元/千克)_否'].mean()
    sigma=df0['批发价格(元/千克)_否'].std()
    x=symbols('x')
    f1=integrate((x*exp(-(x-miu)**2/sigma**2))/(sigma*(2*pi)**0.5),(x,-oo,oo)).round(4)
    f2=integrate((x**2*exp(-(x-miu)**2/sigma**2))/(sigma*(2*pi)**0.5),(x,-oo,oo)).round(4)
    f3=integrate((x**3*exp(-(x-miu)**2/sigma**2))/(sigma*(2*pi)**0.5),(x,-oo,oo)).round(4)
    row=pd.DataFrame({'单品名称':typ,'μ':miu,'σ':sigma,'E(C)':simplify(f1),'E(C^2)':simplify(f2),'E(C^3)':simplify(f3)},index=[0])
    result=pd.concat([result,row],axis=0,ignore_index=True)
    
df2=pd.read_csv('./export/q3_3单品多项式回归.csv',index_col=0)
result=pd.merge(result,df2,on='单品名称',how='left')    

result.to_csv('./export/q3_4数学期望和多项式回归数据总表.csv')