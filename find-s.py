# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:58:13 2023

@author: Divyasri
"""

import pandas as pd
d=pd.DataFrame([['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
                ['Sunny','Warm','high','Strong','Warm','Same','Yes'],
                ['rainy','cold','high','Strong','Warm','change','no'],
                ['Sunny','Warm','Normal','Strong','cool','change','Yes']])

a=list(d.iloc[:,:-1].values)
b=list(d.iloc[:,-1].values)
g=['@' for i in range(len(a[0]))]
s=0
for i in range(len(b)):
    if b[i]=='Yes' and s==0:
        g=a[i].copy()
        s+=1
    if b[i]=='Yes' and s>0:
        for j in range(len(g)):
            if g[j]!=a[i][j]:
                g[j]='?'
                
print(g)
