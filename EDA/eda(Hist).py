import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


NetworkDF = pd.read_csv('log/(after) Network measures features.csv')
PinfoDF = pd.read_csv('log/(after) Player information features.csv')

NetworkHumanDF = NetworkDF.loc[NetworkDF['Type'] == "Human"]
NetworkBotDF = NetworkDF.loc[NetworkDF['Type'] == "Bot"]
MaxLevelHuman = PinfoDF.query('Type == "Human" & Max_level == 55')
MaxLevelBot = PinfoDF.query('Type == "Bot" & Max_level == 55')


MaxLevelHuman_Actor = MaxLevelHuman[['Actor']]
MaxLevelBot_Actor = MaxLevelBot[['Actor']]
print(type(MaxLevelBot_Actor))

Bot_Net_Info_merge = pd.merge(MaxLevelBot_Actor, NetworkBotDF, on='Actor', how='inner')
Human_Net_Info_merge = pd.merge(MaxLevelHuman_Actor, NetworkHumanDF, on='Actor', how='inner')
#result.to_csv("result.csv", sep=',', encoding='utf-8')

compare1 = 't_deg'
compare2 = 't_Wdeg'

Human_p_in_deg = Human_Net_Info_merge[compare1]
Human_p_out_deg = Human_Net_Info_merge[compare2]
Bot_p_in_deg = Bot_Net_Info_merge[compare1]
Bot_p_out_deg = Bot_Net_Info_merge[compare2]


x = Human_p_in_deg
y = Bot_p_in_deg

bins = np.linspace(-10, 100, 100)
titlename = 'Human_p_in_deg & Bot_p_in_deg'
plt.hist(x, bins, alpha=0.5, label='Human_p_in_deg', color = "b")
plt.hist(y, bins, alpha=0.5, label='Bot_p_in_deg', color = "r")
plt.legend(loc='upper right')
plt.title('Human_p_in_deg & Bot_p_in_deg')
plt.savefig("EDAPicture/Hist/"+"(Hist)"+titlename)
plt.show()
