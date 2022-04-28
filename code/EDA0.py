# Filename: EDA0.py
# Copyright: (C)20220426 by Zheng Jiajun
# Function: show the integrity of each column of the dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
# Integrity
x=np.array(["location","iso_code","date","total_vaccinations","people_vaccinated","people_fully_vaccinated","daily_vaccinations_raw","daily_vaccinations","total_vaccinations_per_hundred","people_vaccinated_per_hundred","people_fully_vaccinated_per_hundred","daily_vaccinations_per_million"])
df=pd.read_csv('data/COVID2021.csv')
nan_column=df.isnull().values.astype(int).sum(axis=0)
nonan_column=df.notnull().values.astype(int).sum(axis=0)
integrity=nonan_column/(nan_column+nonan_column)*100
plt.title("COVID2021数据集各字段数据完整率")
plt.xlabel("数据完整率（%）")
plt.ylabel("字段名")
plt.xlim(20,100)
plt.barh(x,integrity)
for a,b,i in zip(x,integrity,range(len(x))):
    plt.text(b,a,"%s"%"%.2f"%integrity[i])
plt.tight_layout()
plt.savefig("output/EDA0.png")