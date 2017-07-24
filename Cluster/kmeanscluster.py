from sklearn.cluster import KMeans
import numpy as np













X = np.array([[1, 2 ,12, 5], [1, 4,14, 6], [1, 0,17, 1], [4, 2,18, 9], [4, 4,16, 7], [4, 0,10, 5]])
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

print(kmeans.labels_)
print(kmeans.predict([[0, 0,12, 5], [4, 4,1, 5]]))