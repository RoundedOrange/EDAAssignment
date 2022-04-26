import pandas
import matplotlib.pyplot as plt
from pyecharts import options
from pyecharts.charts import Bar
import numpy as np
# Integrity
x=np.array(["a","b","c","d"])
y=np.array([1,2,3,4])
plt.bar(x,y)
plt.savefig("output/Integrity.png")