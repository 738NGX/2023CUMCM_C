import pandas as pd
import warnings
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False
warnings.filterwarnings("ignore")

# 读取csv文件
df = pd.read_csv('./export/dataset.csv',index_col=0)

# 将日期列转换为datetime类型
df['日期'] = pd.to_datetime(df['日期'])

# 按日期和品类名称分组，计算销量、销售单价和批发价格的平均值
grouped = df.groupby(['日期', '单品名称', '是否打折销售']).agg(
        {'销量(千克)': 'sum','销售单价(元/千克)':'mean','批发价格(元/千克)': 'mean',
         '损耗率(%)': 'mean'
         })

# 将分组后的数据透视成表格，行为日期和品类名称，列为是否打折销售，值为销量、销售单价和批发价格的平均值
pivot_table = pd.pivot_table(grouped, index=['日期', '单品名称'], columns='是否打折销售', values=['销量(千克)', '销售单价(元/千克)', '批发价格(元/千克)','损耗率(%)'])

# 将透视表格展开，将列名中的层级展开为一级，方便查看和操作
pivot_table.columns = ['_'.join(col).strip() for col in pivot_table.columns.values]

# 对空值统一赋0
pivot_table.fillna(0,inplace=True)

# 将透视表格保存为csv文件
pivot_table=pivot_table[['批发价格(元/千克)_否','销售单价(元/千克)_否','销量(千克)_否','损耗率(%)_否']]
pivot_table.to_csv('./export/q3_1单品每日批发售价销量损耗率汇总.csv')