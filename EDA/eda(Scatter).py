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

compare1 = 't_deg'
compare2 = 't_Wdeg'

Human_p_in_deg = Human_Net_Info_merge[compare1]
Human_p_out_deg = Human_Net_Info_merge[compare2]
Bot_p_in_deg = Bot_Net_Info_merge[compare1]
Bot_p_out_deg = Bot_Net_Info_merge[compare2]

#scatter
g1 = (Human_p_in_deg, Human_p_out_deg)
g2 = (Bot_p_in_deg,Bot_p_out_deg)

data = (g1, g2)
colors = ("blue", "red")
groups = ("Human", "Bot")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
titlename = 't_deg and t_Wdeg'
plt.title(titlename)
plt.legend(loc=2)
plt.savefig("EDAPicture/Scatter/"+"(Scatter)"+titlename)
plt.show()
