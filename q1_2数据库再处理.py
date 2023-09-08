import pandas as pd
dataset=pd.read_csv('./export/dataset.csv',index_col=0)

dataset=dataset.rename(columns={'平均损耗率(%)_小分类编码_不同值': '平均损耗率(%)'})
dataset=dataset[['日期','扫码销售时间','单品编码','单品名称','分类编码','分类名称',
                 '销售类型','销量(千克)','销售单价(元/千克)','是否打折销售',
                 '批发价格(元/千克)','损耗率(%)','平均损耗率(%)']]
dataset.to_csv('./export/dataset.csv')