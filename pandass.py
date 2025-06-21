# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
data=pd.read_csv(r'C:\Users\Divyasri\Desktop\file\Movie-Data.csv')
data.shape
data.size
data.ndim
data.head()
data.tail()
data.columns
data['Revenue (Millions)'].max()
data['Revenue (Millions)'].sum()
data['Revenue (Millions)'].mean()
data['Year'].unique()
#print(data['Year'].value_counts)

data.isna().sum()
data.dropna(inplace=True)
data.shape


data.drop(['Revenue (Millions)','Metascore'],axis=1,inplace=True)
data.shape

data=data.append(data)
data.shape

data.drop_duplicates(inplace=True)
data.shape

data[data['Year']==2016].count()
data[data['Revenue (Millions)']>250]
data[data['Revenue (Millions)']>250].count()
data[(data['Year']==2015) | (data['Year']==2016)]
data[(data['Year']==2016) & (data['Revenue (Millions)']>250)]

data.iloc[3]
data.iloc[0:5,0:5]








