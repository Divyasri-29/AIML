# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:01:49 2023

@author: Divyasri
"""

import pandas as pd
d=pd.DataFrame([['sunny','warm','normal','strong','warm','same','yes'],
                ['sunny','warm','high','strong','warm','same','yes'],
                ['rain','cold','high','strong','warm','change','no'],
                ['sunny','warm','normal','strong','cool','change','yes']])

a=list(d.iloc[:,:-1].values)
b=list(d.iloc[:,-1].values)
s=['@' for i in range(len(a[0]))]
g=[['?' for i in range(len(a[0]))] for j in range(len(a[0]))]
r=0 

for i in range(len(b)):
    if(b[i]=='yes' and r==0):
        s=a[i].copy()
        r+=1
    if(b[i]=='yes' and r>0):
        for j in range(len(s)):
            if(s[j]!=a[i][j]):
                s[j]='?'
    if(b[i]=='no'):
        for k in range(len(g)):
            if s[k]!=a[i][k]:
                g[k][k]=s[k]
            else:
                g[k][k]='?'

print(s)
print(g)
n=[]
for i in range(len(s)):
    if(s[i]!=g[i][i]):
        g[i][i]='?'
    if(g[i].count('?')!=len(s)):
        n.append(g[i])
        
print(n)