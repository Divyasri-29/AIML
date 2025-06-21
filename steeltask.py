# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:35:56 2023

@author: Divyasri
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\Divyasri\Desktop\AIML\Steel_industry_data.csv")
data.shape
data.size
x=data['Lagging_Current_Reactive.Power_kVarh']
y=data['Lagging_Current_Power_Factor']
x1=x[10:15]
y1=y[10:15]
colors=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#8c564b"]
explode=(0.1,0,0,0,0)
plt.pie(x1,labels=y1,explode=explode,colors=colors)
plt.title("Pie Chart",fontsize=20,color="#fa2a55")
plt.show()
