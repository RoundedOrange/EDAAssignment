# Filename: EDA3.py
# Copyright: (C)20220428 by Zheng Jiajun
# Function: explore the correlation between people_vaccinated_per_hundred and people_fully_vaccinated_per_hundred
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df=pd.read_csv('data/COVID2021.csv',usecols=[9,10])
df2=df['people_vaccinated_per_hundred'].notnull()
df=df[df2]
df2=df['people_fully_vaccinated_per_hundred'].notnull()
df=df[df2]
df.to_csv('output/EDA3.csv',sep=',')
plt.scatter(df['people_vaccinated_per_hundred'],df['people_fully_vaccinated_per_hundred'],s=20,c='r')
plt.title("每百人接种人数和每百人完全接种人数的关系散点图")
plt.xlabel('每百人接种人数')
plt.ylabel('每百人完全接种人数')
plt.savefig("output/EDA3_1.png")