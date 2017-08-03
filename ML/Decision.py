from sklearn import tree


from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import silhouette_samples, silhouette_score


ClusterDF = pd.read_csv('../log/ClusterResult.csv')
xlist = []
ylist = []


for i in range(0,5000):
    xlist.append(ClusterDF.loc[i][['NomalIndex','FarmerIndex','MerchantIndex','HardIndex']].tolist())
    ylist.append(ClusterDF.loc[i][7].tolist())


#X = [[6, 0, 1, 2], [1, 1, 5, 6], [3, 5, 3, 1]]
#Y = [0, 1, 2]
X = xlist
Y = ylist
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(ClusterDF.loc[6001])


print("result")
print(clf.predict([ClusterDF.loc[5801][['NomalIndex','FarmerIndex','MerchantIndex','HardIndex']].tolist()]))
print(clf.predict([ClusterDF.loc[5672][['NomalIndex','FarmerIndex','MerchantIndex','HardIndex']].tolist()]))
print(clf.predict([ClusterDF.loc[5665][['NomalIndex','FarmerIndex','MerchantIndex','HardIndex']].tolist()]))
print(clf.predict([ClusterDF.loc[5407][['NomalIndex','FarmerIndex','MerchantIndex','HardIndex']].tolist()]))
print(clf.predict([ClusterDF.loc[5154][['NomalIndex','FarmerIndex','MerchantIndex','HardIndex']].tolist()]))




with open("result.txt", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)


