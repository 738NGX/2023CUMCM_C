# 2023 CUMCM 数模国赛 202309007016组 程序记录

## ✅Finished
把论文中原Q型聚类分析部分删除 换上箱线图和新的相关系数矩阵
问题2（1）
需要六张图片中W与Q的相关性评估（相关系数，是否显著相关，正负相关性等）
目前修正了问题2（2）的思路 
现在需要
1. 用时间序列预测20230701-20230707各品类每日销量
2. 直接拟合各品类销量Q与定价P的关系，画出图线;根据上述某品类Q-P图线带入预估的当日销量Q值;算出预估的需求价格弹性a=PdQ/QdP;再带入公式w=a/1+a 即可算出当日定价策略中w的值;
每个品类的批发价按照期望和方差计算
设置成按照正态分布的随机变量
计算数学期望

## 📝ToDo List

