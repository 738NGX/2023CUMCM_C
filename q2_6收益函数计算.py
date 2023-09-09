import pandas as pd
from sympy import *
df=pd.read_csv('./export/q2_5品类数学期望和多项式回归数据总表.csv',index_col=0)

result=pd.DataFrame(columns=['分类名称','r_max','w','p','q'])

for typ in df['分类名称'].values:
    # 导入常数
    df0=df[df['分类名称']==typ].copy()
    ec,ec2,ec3=df0['E(C)'].values[0],df0['E(C^2)'].values[0],df0['E(C^3)'].values[0]
    k1,k2,k3=df0['k1'].values[0],df0['k2'].values[0],df0['k3'].values[0]
    
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
    q=k1*p**2+k2*p+k3
    
    # 打表
    row={'分类名称':typ,'r_max':r_max,'w':w_max,'p':p,'q':q}
    result=pd.concat([result,pd.DataFrame(row,index=[0])],axis=0,ignore_index=True)

result.to_csv('./export/q2_6问题二最终结论.csv')