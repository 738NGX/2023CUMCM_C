import pandas as pd

file_1='./dataset/附件1.xlsx'
file_2='./dataset/附件2.xlsx'
file_3='./dataset/附件3.xlsx'
file_4='./dataset/附件4.xlsx'

raw_data_1=pd.read_excel(file_1)
raw_data_2=pd.read_excel(file_2)
raw_data_3=pd.read_excel(file_3)
raw_data_41=pd.read_excel(file_4,sheet_name='平均损耗率(%)_小分类编码_不同值')
raw_data_42=pd.read_excel(file_4,sheet_name='Sheet1')

merged_data=pd.merge(raw_data_2,raw_data_1,on='单品编码',how='left')
merged_data = merged_data.rename(columns={'销售日期': '日期'})
merged_data=pd.merge(merged_data,raw_data_3,on=['日期', '单品编码'],how='left')
merged_data=pd.merge(merged_data,raw_data_42[['单品编码','损耗率(%)']],on='单品编码',how='left')
merged_data=pd.merge(merged_data,raw_data_41[['分类编码','平均损耗率(%)_小分类编码_不同值']],on='分类编码',how='left')

merged_data.to_csv('./export/dataset.csv')