import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import datetime 
import sys
style.use('ggplot')

def get1mYahooData(ticker):
    if ticker.lower()=='spx':
        ticker='^GSPC'
    end=datetime.date.today()
    start = datetime.date.today()-datetime.timedelta(29)
    end=start+datetime.timedelta(7)
    tick = yf.Ticker(ticker)
    data=[]
    while end<datetime.date.today():
        df = tick.history(start=start, end=end,interval='1m')
        data.append(df)
        start=start+ datetime.timedelta(7)
        end=end+ datetime.timedelta(7)

    data=pd.concat(data)
    return data



figsize=(20,15)
saturation_point=0.05
clustersize=11
noclusters=3

if len(sys.argv) <2:
  ticker='QQQ'
if len(sys.argv) >=2:
  ticker=sys.argv[1]
if len(sys.argv) >=3:
  saturation_point=float(sys.argv[2])
if len(sys.argv) >=4:
  clustersize=int(sys.argv[3])

if len(sys.argv) >=5:
  noclusters=int(sys.argv[4])



data=get1mYahooData(ticker)
low = pd.DataFrame(data=data['Low'], index=data.index)
high = pd.DataFrame(data=data['High'], index=data.index)

# finding the optimum k through elbow method
def get_optimum_clusters(data, saturation_point=0.05, size=11):

    wcss = []
    k_models = []

    for i in range(1, size):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
        k_models.append(kmeans)
        
    plt.plot(range(1,size), wcss)
            
    return k_models

if noclusters> len(low):
    noclusters=len(low)
if noclusters> len(high):
    noclusters=len(high)

# index 3 as 4 is the value of K (elbow point)
low_clusters = get_optimum_clusters(low, saturation_point=saturation_point, size=clustersize)[noclusters]
high_clusters = get_optimum_clusters(high, saturation_point=saturation_point, size=clustersize)[noclusters]

low_centers = low_clusters.cluster_centers_
high_centers = high_clusters.cluster_centers_
#plt.plot(data['Close'])
#fig1,ax1=mpf.plot(df,type='candle',volume=True,addplot=apdict, figsize=figsize,tight_layout=True,style=s,returnfig=True,block=False)

hlines=[]
colors=[]

#data['Close'].plot(figsize=(16,8), c='b')
for i in low_centers:
    hlines.append(i[0])
    colors.append('g')
    #plt.axhline(i, c='g', ls='--')
for i in high_centers:
    hlines.append(i[0])
    colors.append('r')
    #plt.axhline(i, c='r', ls='--')
mpf.plot(data,type='candle', hlines=dict(hlines=hlines,colors=colors),figsize=figsize, block=False,title='top 3')

#finding the optimum k using the silhouette method
def optimum_Kvalue(data):
    kmax = 11
    sil = {}
    k_model = {}
    for k in range(2, kmax+1):
        kmeans = KMeans(n_clusters = k).fit(data)
        k_model[k] = kmeans
        labels = kmeans.labels_
        sil[k]=(silhouette_score(data, labels))
    optimum_cluster = k_model[max(sil, key=sil.get)]
    plt.plot(range(2,12), sil.values())
    return optimum_cluster
  
low_cl = optimum_Kvalue(high)
high_cl = optimum_Kvalue(low)

low_ce = low_cl.cluster_centers_
high_ce = high_cl.cluster_centers_

hlines=[]
colors=[]

#plt.plot(data['Close'])
#data['Close'].plot(figsize=(16,8), c='b')
for i in low_ce:
    hlines.append(i[0])
    colors.append('g')
    #plt.axhline(i, c='g', ls='--')
for i in high_ce:
    hlines.append(i[0])
    colors.append('r')
    #plt.axhline(i, c='r', ls='--')
mpf.plot(data,type='candle', hlines=dict(hlines=hlines,colors=colors),figsize=figsize, title='optimum_Kvalue')
plt.show()
