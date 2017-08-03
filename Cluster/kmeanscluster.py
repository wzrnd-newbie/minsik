from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import silhouette_samples, silhouette_score

NetworkDF = pd.read_csv('../log/(after) Network measures features.csv')
PinfoDF = pd.read_csv('../log/(after) Player information features.csv')
PactionDF = pd.read_csv('../log/(after) Player actions features.csv')
GactiveDF = pd.read_csv('../log/(after) Group activities features.csv')
SointerDF = pd.read_csv('../log/(after) Social interaction diversity features.csv')
ClusterDF = pd.read_csv('../log/ClusterResult.csv')

mergetmp = pd.merge(NetworkDF.iloc[:,0:-1], PinfoDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergetmp = pd.merge(mergetmp, PactionDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergetmp = pd.merge(mergetmp, GactiveDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergerDF = pd.merge(mergetmp, SointerDF.drop(['A_Acc'], axis =1), on='Actor', how='inner')

#Total_Action_Info_merge = mergerDF.query('Max_level == 55 & Type == "Bot"')
Total_Action_Info_merge = mergerDF.query('Type == "Bot"')

PcaDF = pd.read_csv('../log/predictpca.csv')
#features = ['NomalIndex','SlowIndex','NoplayIndex','FarmerIndex','MerchantIndex','HardIndex']

#print(PcaDF)
#print("query")
#print(PcaDF.query('HardIndex >= 5'))
#print(PcaDF.loc[0]['NomalIndex']>5)


print(PcaDF[['NomalIndex','SlowIndex','NoplayIndex','FarmerIndex','MerchantIndex','HardIndex']].idxmax(axis=1))
print(PcaDF[['NomalIndex','SlowIndex','NoplayIndex','FarmerIndex','MerchantIndex','HardIndex']].idxmax(axis=1)[0])


features = ['FarmerIndex','MerchantIndex']
#for i in range(0, len(features)):
#    for j in range(i+1, len(features)):
#        print(features[i])
#        print(features[j])

'''
#############변수 2개로 클러스터
frames = []
somefeatures = []
for i in range(0, len(features[:-1])):

    for j in range(i+1,len(features[:-1])):

        print("i: ",i)
        print("j: ",j)

        somefeatures.append(features[:-1][i])
        somefeatures.append(features[:-1][j])

        for k in somefeatures:
            frames.append(Total_Action_Info_merge[k])


        result = pd.concat(frames, axis=1)

        #X = preprocessing.scale(result.iloc[:,:-1].values.tolist())
        X = preprocessing.scale((np.asarray(result.iloc[:,:-1].values.tolist())))

        n_clu = 4
        #X = np.array(result.iloc[:,:-1].values.tolist())
        #X = preprocessing.scale(X)
        kmeans = KMeans(n_clusters=n_clu, random_state=0).fit(X)
        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_
        #print(kmeans.cluster_centers_ )
        silhouette_avg = silhouette_score(X,labels)
        print(somefeatures)
        print(silhouette_avg)
        frames = []
        somefeatures = []
'''
'''
##변수3개

frames = []
somefeatures = []
for i in range(0, len(features[:-1])):

    for j in range(i+1,len(features[:-1])):

        for k in range(j+1,len(features[:-1])):



            somefeatures.append(features[:-1][i])
            somefeatures.append(features[:-1][j])
            somefeatures.append(features[:-1][k])

            for input in somefeatures:
                frames.append(Total_Action_Info_merge[input])


            result = pd.concat(frames, axis=1)

            #X = preprocessing.scale(result.iloc[:,:-1].values.tolist())
            X = preprocessing.scale((np.asarray(result.iloc[:,:-1].values.tolist())))

            n_clu = 4
            #X = np.array(result.iloc[:,:-1].values.tolist())
            #X = preprocessing.scale(X)
            kmeans = KMeans(n_clusters=n_clu, random_state=0).fit(X)
            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            #print(kmeans.cluster_centers_ )
            silhouette_avg = silhouette_score(X,labels)
            print(somefeatures)
            print(silhouette_avg)
            frames = []
            somefeatures = []
'''
'''
###변수4개
frames = []
somefeatures = []
for i in range(0, len(features[:-1])):

    for j in range(i+1,len(features[:-1])):

        for k in range(j+1,len(features[:-1])):
            for l in range(k+1,len(features[:-1])):


                somefeatures.append(features[:-1][i])
                somefeatures.append(features[:-1][j])
                somefeatures.append(features[:-1][k])
                somefeatures.append(features[:-1][l])

                for input in somefeatures:
                    frames.append(Total_Action_Info_merge[input])


                result = pd.concat(frames, axis=1)

                #X = preprocessing.scale(result.iloc[:,:-1].values.tolist())
                X = preprocessing.scale((np.asarray(result.iloc[:,:-1].values.tolist())))

                n_clu = 4
                #X = np.array(result.iloc[:,:-1].values.tolist())
                #X = preprocessing.scale(X)
                kmeans = KMeans(n_clusters=n_clu, random_state=0).fit(X)
                labels = kmeans.labels_
                centroids = kmeans.cluster_centers_
                #print(kmeans.cluster_centers_ )
                silhouette_avg = silhouette_score(X,labels)
                print(somefeatures)
                print(silhouette_avg)
                frames = []
                somefeatures = []
'''


frames = []

for input in features:
    frames.append(PcaDF[input])

result = pd.concat(frames, axis=1)
#X = preprocessing.scale(result.iloc[:,:-1].values.tolist())
#X = preprocessing.scale((np.asarray(result.values.tolist())))
X = ((np.asarray(result.values.tolist())))
n_clu = 3
#X = np.array(result.iloc[:,:-1].values.tolist())
#X = preprocessing.scale(X)
kmeans = KMeans(n_clusters=n_clu, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
#print(kmeans.cluster_centers_ )
silhouette_avg = silhouette_score(X,labels)
print(features)
print(silhouette_avg)

exit()
frames = []
somefeatures = []

'''
labels = pd.DataFrame(labels)

labels.columns=['cluster']
X = pd.DataFrame(X, columns = features[:-1])
#X = X.reset_index()

result = pd.DataFrame(result, columns = ['Type'])
result = result.reset_index(drop=True)

result = pd.concat([X,result], axis=1, join_axes=[result.index])
cluster_result_df = pd.concat([result, labels], axis=1, join_axes=[result.index])
'''
'''
for i in range(0,k):
    print("----cluster : %s----"%i)
    print("human: ", cluster_result_df.query('cluster == %s & Type=="Human"'%i).count()[0])
    print("Bot: ", cluster_result_df.query('cluster == %s & Type=="Bot"'%i).count()[0])
'''
def log(x):
    return np.log(x)
def square(x):
    return x**2

x = PcaDF.NomalIndex.apply(square).apply(log)
x1 = PcaDF.SlowIndex.apply(square).apply(log)
x2 = PcaDF.NoplayIndex.apply(square).apply(log)
x3 = PcaDF.FarmerIndex.apply(square).apply(log)
x4 = PcaDF.MerchantIndex.apply(square).apply(log)
x5 = PcaDF.HardIndex.apply(square).apply(log)

f, axarr = plt.subplots(2, 3)

axarr[0, 0].boxplot(x)
axarr[0, 0].set_title('NomalIndex')

axarr[0, 1].boxplot(x1)
axarr[0, 1].set_title('SlowIndex')

axarr[0, 2].boxplot(x2)
axarr[0, 2].set_title('NoplayIndex')

axarr[1, 0].boxplot(x3)
axarr[1, 0].set_title('FarmerIndex')

axarr[1, 1].boxplot(x4)
axarr[1, 1].set_title('FarmerIndex')

axarr[1, 2].boxplot(x5)
axarr[1, 2].set_title('FarmerIndex')


# Fine-tune figure; make subplots farther from each other.
f.subplots_adjust(hspace=0.3)

plt.show()


exit()


def MakeHist(clustering1,clustering2, bot_or_Human1, compareV1, bot_or_Human2, compareV2, Save_or_Not=0):

    if (bot_or_Human1 =='Human'):
        x = cluster_result_df.query('cluster == %s & Type=="Human"'%clustering1)[compareV1]
    elif(bot_or_Human1 =='Bot'):
        x = cluster_result_df.query('cluster == %s & Type=="Bot"' % clustering1)[compareV1]

    if (bot_or_Human2 == 'Human'):
        y = cluster_result_df.query('cluster == %s & Type=="Human"'%clustering2)[compareV2]

    elif (bot_or_Human2 == 'Bot'):
        y = cluster_result_df.query('cluster == %s & Type=="Bot"' % clustering2)[compareV2]


    bins = [0, 1, 2, 3, 4, 5, 10]
    titlename = '%s_%s & %s_%s'%(bot_or_Human1, compareV1, bot_or_Human2, compareV2)
    print('%s_%s_%s의 평균'%(bot_or_Human1, compareV1, clustering1),x.mean())
    print('%s_%s_%s의 표준 편차'%(bot_or_Human1, compareV1, clustering1),x.std())
    print('%s_%s_%s의 평균'%(bot_or_Human2, compareV2, clustering2),y.mean())
    print('%s_%s_%s의 표준 편차'%(bot_or_Human2, compareV2, clustering2),y.std())
    plt.hist(x, bins, alpha=0.5, label='%s_%s_%s'%(bot_or_Human1, compareV1, clustering1), color = "b")
    plt.hist(y, bins, alpha=0.5, label='%s_%s_%s'%(bot_or_Human2, compareV2, clustering2), color = "r")
    plt.legend(loc='upper right')
    plt.title('%s'%titlename)
    if (Save_or_Not==1):
        plt.savefig("EDAPicture/Hist/"+"(Hist)"+titlename)

    plt.show()

def MakeBox(Save_or_Not=0):


    datax = cluster_result_df.query('cluster == 0 & Type=="Bot"').iloc[:,0:-2].as_matrix()
    datax1 = cluster_result_df.query('cluster == 1 & Type=="Bot"').iloc[:,0:-2].as_matrix()
    datax2 = cluster_result_df.query('cluster == 2 & Type=="Bot"').iloc[:,0:-2].as_matrix()
    datax3 = cluster_result_df.query('cluster == 3 & Type=="Bot"').iloc[:,0:-2].as_matrix()
    datax4 = cluster_result_df.query('cluster == 4 & Type=="Bot"').iloc[:,0:-2].as_matrix()

    titlename = 'Bot 0, 1, 2, 3, 4, 5 group'

    f, axarr = plt.subplots(2, 3)

    axarr[0, 0].boxplot(datax, labels=features[:-1])
    axarr[0, 0].set_title('cluster: 0 & Type: Bot')

    axarr[0, 1].boxplot(datax1, labels=features[:-1])
    axarr[0, 1].set_title('cluster: 1 & Type: Bot')

    axarr[1, 0].boxplot(datax2, labels=features[:-1])
    axarr[1, 0].set_title('cluster: 2 & Type: Bot')

    axarr[1, 1].boxplot(datax3, labels=features[:-1])
    axarr[1, 1].set_title('cluster: 3 & Type: Bot')

    axarr[1, 2].boxplot(datax4, labels=features[:-1])
    axarr[1, 2].set_title('cluster: 4 & Type: Bot')


    # Fine-tune figure; make subplots farther from each other.
    f.subplots_adjust(hspace=0.3)


    if (Save_or_Not==1):
        plt.savefig("../EDA/EDAPicture/Box/"+"(Box)"+titlename)
    plt.show()

'''
if __name__ == "__main__":
    #MakeHist(0,1,'Human', 't_deg', 'Bot', 't_deg')
    MakeBox(0)
'''

