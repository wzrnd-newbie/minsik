from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


NetworkDF = pd.read_csv('../log/(after) Network measures features.csv')
PinfoDF = pd.read_csv('../log/(after) Player information features.csv')
PactionDF = pd.read_csv('../log/(after) Player actions features.csv')

NetworkHumanDF = NetworkDF.loc[NetworkDF['Type'] == "Human"]
NetworkBotDF = NetworkDF.loc[NetworkDF['Type'] == "Bot"]
ActionHumanDF = PactionDF.loc[PactionDF['Type'] == "Human"]
ActionBotDF = PactionDF.loc[PactionDF['Type'] == "Bot"]

MaxLevelTotal = PinfoDF.query('Max_level == 55')
MaxLevelHuman = PinfoDF.query('Type == "Human" & Max_level == 55')
MaxLevelBot = PinfoDF.query('Type == "Bot" & Max_level == 55')

MaxLevelTotal_Actor = MaxLevelTotal[['Actor']]
MaxLevelHuman_Actor = MaxLevelHuman[['Actor']]
MaxLevelBot_Actor = MaxLevelBot[['Actor']]

Total_Net_Info_merge = pd.merge(MaxLevelTotal_Actor, NetworkHumanDF, on='Actor', how='inner')
Human_Net_Info_merge = pd.merge(MaxLevelHuman_Actor, NetworkHumanDF, on='Actor', how='inner')
Bot_Net_Info_merge = pd.merge(MaxLevelBot_Actor, NetworkBotDF, on='Actor', how='inner')

Total_Action_Info_merge = pd.merge(MaxLevelTotal_Actor, ActionHumanDF, on='Actor', how='inner')
Human_Action_Info_merge = pd.merge(MaxLevelHuman_Actor, ActionHumanDF, on='Actor', how='inner')
Bot_Action_Info_merge = pd.merge(MaxLevelBot_Actor, ActionBotDF, on='Actor', how='inner')


feature1 = 'Exp_get_count'
feature2 = 'Item_get_count'
feature3 = 'Money_get_count'
feature4 = 'Abyss_get_count'
feature5 = 'Exp_repair_count'
feature6 = 'Killed_bypc_count'
feature7 = 'Killed_bynpc_count'
feature8 = 'Teleport_count'
feature9 = 'Type'

Total_feature1 = Total_Action_Info_merge[feature1]
Total_feature2 = Total_Action_Info_merge[feature2]
Total_feature3 = Total_Action_Info_merge[feature3]
Total_feature4 = Total_Action_Info_merge[feature4]
Total_feature5 = Total_Action_Info_merge[feature5]
Total_feature6 = Total_Action_Info_merge[feature6]
Total_feature7 = Total_Action_Info_merge[feature7]
Total_feature8 = Total_Action_Info_merge[feature8]
Total_feature9 = Total_Action_Info_merge[feature9]


frames = [Total_feature1, Total_feature2, Total_feature3, Total_feature4, Total_feature5, Total_feature6, Total_feature7, Total_feature8 ,Total_feature9]
result = pd.concat(frames, axis=1)

k = 4
X = np.array(result.iloc[:,:-1].values.tolist())
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

labels = pd.DataFrame(labels)
labels.columns=['cluster']

cluster_result_df = pd.concat([result, labels], axis=1, join_axes=[result.index])




