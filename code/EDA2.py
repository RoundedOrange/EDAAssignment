# Filename: EDA2.py
# Copyright: (C)20220427 by Zheng Jiajun
# Function: explore the top 10 countries which consume the most amount of vaccines daily
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df=pd.read_csv('data/COVID2021.csv',usecols=[0,2,7])
actual_day=df['daily_vaccinations'].notnull()
df=df[actual_day]
output=df.groupby('location')['daily_vaccinations'].mean().sort_values(ascending=False)
output.to_csv('output/EDA2.csv',sep=',')
output1=output.iloc[1:11]
plt.yticks(fontsize=12)
plt.figure(dpi=300,figsize=(10,8))
output1.plot(kind='barh',title="每日接种疫苗数前十国家统计",xlabel="国家",ylabel="每日接种疫苗数")
plt.tight_layout()
plt.savefig("output/EDA2_1.png")
tempDF=pd.Series(data={'Other':output.iloc[11:].sum()},index=['Other'])
output2=pd.concat([tempDF,output1],axis=0)
plt.figure(figsize=(9,9))
plt.pie(output2,autopct='%.2f%%',labels=output2.index,colors=['green','red','yellow','blue','green','red','yellow','blue','green','red','yellow','blue'])
plt.title("每日接种疫苗数各国占比")
plt.savefig("output/EDA2_2.png")