# Filename: EDA1.py
# Copyright: (C)20220426 by Zheng Jiajun
# Function: explore the correlation between location and people_vaccinated_per_hundred
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# correlation between location and people_vaccinated_per_hundred
df=pd.read_csv('data/COVID2021.csv',usecols=[0,2,9])
actual_day=df['people_vaccinated_per_hundred'].notnull()
df=df[actual_day]
output=df.groupby('location')['people_vaccinated_per_hundred'].mean().sort_values(ascending=False)
output.to_csv('output/EDA1.csv',sep=',')
plt.yticks(fontsize=12)
plt.figure(dpi=300,figsize=(8,14))
output.plot(kind='barh',title="各地区每百人接种疫苗人数",xlabel="地区",ylabel="每百人接种疫苗人数（人）",xlim=(0,20))
plt.tight_layout()
plt.savefig("output/EDA1_1.png")
output=output.iloc[1:11]
plt.figure(figsize=(8,8))
output.plot(kind='barh',title="各地区每百人接种疫苗人数",xlabel="地区",ylabel="每百人接种疫苗人数（人）",xlim=(0,20))
plt.tight_layout()
plt.savefig("output/EDA1_2.png")