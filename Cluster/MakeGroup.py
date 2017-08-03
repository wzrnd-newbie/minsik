
import numpy as np
import pandas as pd

PcaDF = pd.read_csv('../log/predictpca.csv')


Grouplist = []
for i in range(0, PcaDF.shape[0]):
    if((PcaDF[['NomalIndex','SlowIndex','NoplayIndex','FarmerIndex','MerchantIndex','HardIndex']].idxmax(axis=1)[i]=='FarmerIndex') and PcaDF.loc[i]['FarmerIndex']>4):
        Grouplist.append(0)
    elif((PcaDF[['NomalIndex','SlowIndex','NoplayIndex','FarmerIndex','MerchantIndex','HardIndex']].idxmax(axis=1)[i]=='MerchantIndex') and PcaDF.loc[i]['MerchantIndex']>5):
        Grouplist.append(1)
    else:
        Grouplist.append(2)
    print(i)

PcaDF["Group"] = np.asarray(Grouplist)
print(PcaDF)
PcaDF.to_csv("ClusterResult.csv", sep=',', encoding='utf-8')