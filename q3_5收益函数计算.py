import pandas as pd
from sympy import *
df=pd.read_csv('./export/q3_4数学期望和多项式回归数据总表.csv',index_col=0)
waste_data=pd.read_excel('./dataset/附件4.xlsx',sheet_name='Sheet1',index_col='单品名称')['损耗率(%)']

result=pd.DataFrame(columns=['单品名称','R_max','W','P','Q','S(Q)'])

for typ in df['单品名称'].values:
    # 导入常数
    df0=df[df['单品名称']==typ].copy()
    ec,ec2,ec3=df0['E(C)'].values[0],df0['E(C^2)'].values[0],df0['E(C^3)'].values[0]
    k1,k2,k3=df0['k1'].values[0],df0['k2'].values[0],df0['k3'].values[0]
    waste=waste_data[typ]/100
    
    # 定义函数
    w=symbols('w')
    r=k1*ec3*w*(1+w)**2+k2*ec2*(1+w)+k3*ec*w
    
    # 求导&求解
    dr=diff(r,w)
    solutions=solve(dr,w,real=True)
    
    # 计算
    w_max=max(solutions,key=lambda x: re(x))
    if im(w_max) != 0:
        r_max=r.subs(w,3) if r.subs(w,3)>=r.subs(w,0) else r.subs(w,0)
        w_max=3 if r.subs(w,3)>=r.subs(w,0) else 0
    else:
        r_max=r.subs(w,w_max)
    p=ec*(1+w_max)
    q=(k1*p**2+k2*p+k3)
    sq=q/(1-waste)
    
    # 打表
    row={'单品名称':typ,'R_max':r_max,'W':w_max,'P':p,'Q':q,'S(Q)':sq}
    result=pd.concat([result,pd.DataFrame(row,index=[0])],axis=0,ignore_index=True)

result.to_csv('./export/q3_5问题三利润总表(未筛选单品).csv')