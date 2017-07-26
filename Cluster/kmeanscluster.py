from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

NetworkDF = pd.read_csv('../log/(after) Network measures features.csv')
PinfoDF = pd.read_csv('../log/(after) Player information features.csv')
PactionDF = pd.read_csv('../log/(after) Player actions features.csv')
GactiveDF = pd.read_csv('../log/(after) Group activities features.csv')
SointerDF = pd.read_csv('../log/(after) Social interaction diversity features.csv')

mergetmp = pd.merge(NetworkDF.iloc[:,0:-1], PinfoDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergetmp = pd.merge(mergetmp, PactionDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergetmp = pd.merge(mergetmp, GactiveDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergerDF = pd.merge(mergetmp, SointerDF.drop(['A_Acc'], axis =1), on='Actor', how='inner')

Total_Action_Info_merge = mergerDF.query('Max_level == 55 & Type == "Bot"')


features = ['p_deg', 't_deg','Abyss_get_count','collect_max_count','Exp_get_count', 'Type']



frames = []
for i in features:
    frames.append(Total_Action_Info_merge[i])


result = pd.concat(frames, axis=1)

X = preprocessing.scale(result.iloc[:,:-1].values.tolist())

k = 5
#X = np.array(result.iloc[:,:-1].values.tolist())
#X = preprocessing.scale(X)
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print(kmeans.cluster_centers_ )

labels = pd.DataFrame(labels)

labels.columns=['cluster']
X = pd.DataFrame(X, columns = ['p_deg','t_deg','Abyss_get_count','collect_max_count','Exp_get_count'])
#X = X.reset_index()

result = pd.DataFrame(result, columns = ['Type'])
result = result.reset_index(drop=True)

result = pd.concat([X,result], axis=1, join_axes=[result.index])
cluster_result_df = pd.concat([result, labels], axis=1, join_axes=[result.index])


for i in range(0,k):
    print("----cluster : %s----"%i)
    print("human: ", cluster_result_df.query('cluster == %s & Type=="Human"'%i).count()[0])
    print("Bot: ", cluster_result_df.query('cluster == %s & Type=="Bot"'%i).count()[0])



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

def MakeBox(clustering1,clustering2, bot_or_Human1, bot_or_Human2, Save_or_Not=0):

    if (bot_or_Human1 =='Human'):
        datax = cluster_result_df.query('cluster == %s & Type=="Human"'%clustering1).iloc[:,0:-2].as_matrix()
    elif(bot_or_Human1 =='Bot'):
        datax = cluster_result_df.query('cluster == %s & Type=="Bot"'%clustering1).iloc[:,0:-2].as_matrix()

    if (bot_or_Human2 == 'Human'):
        datay = cluster_result_df.query('cluster == %s & Type=="Human"'%clustering2).iloc[:,0:-2].as_matrix()

    elif (bot_or_Human2 == 'Bot'):
        datay = cluster_result_df.query('cluster == %s & Type=="Bot"'%clustering2).iloc[:,0:-2].as_matrix()

    titlename = '%s_%s & %s_%s' % (bot_or_Human1,clustering1, bot_or_Human2, clustering2)
    plt.figure(1)
    plt.subplot(121)
    #plt.gca().set_ylim([-2, 4])
    plt.title('cluster: %s & Type: %s'%(clustering1, bot_or_Human1))
    plt.boxplot(datax, labels=features[:-1])
    plt.subplot(122)
    #plt.gca().set_ylim([-2, 4])
    plt.title('cluster: %s & Type: %s'%(clustering2, bot_or_Human2))
    plt.boxplot(datay, labels=features[:-1])

    if (Save_or_Not==1):
        plt.savefig("EDAPicture/Hist/"+"(Box)"+titlename)
    plt.show()


if __name__ == "__main__":
    #MakeHist(0,1,'Human', 't_deg', 'Bot', 't_deg')
    MakeBox(1,2,'Bot', 'Bot')

