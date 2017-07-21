import pandas as pd
NetworkDF = pd.read_csv('(after) Network measures features.csv')
PinfoDF = pd.read_csv('(after) Player information features.csv')

NetworkHumanDF = NetworkDF.loc[NetworkDF['Type'] == "Human"]
NetworkBotDF = NetworkDF.loc[NetworkDF['Type'] == "Bot"]
MaxLevelHuman = PinfoDF.query('Type == "Human" & Max_level == 55')
MaxLevelBot = PinfoDF.query('Type == "Bot" & Max_level == 55')

MaxLevelHuman_Actor = MaxLevelHuman.loc[MaxLevelHuman['Actor']]
MaxLevelBot_Actor = MaxLevelBot.loc[MaxLevelHuman['Actor']]

MaxLevelBot_Actor = MaxLevelBot['Actor']

MaxLevelHuman_Actor = MaxLevelHuman_Actor.set_index('Actor')
MaxLevelBot_Actor = MaxLevelBot_Actor.set_index('Actor')

Botjoin = [MaxLevelBot_Actor,NetworkBotDF]

result = pd.concat(Botjoin)

result.to_csv("result.csv", sep=',', encoding='utf-8')
exit()
Human_p_in_deg = NetworkHumanDF['p_in_deg']
Bot_p_in_deg = NetworkBotDF['p_in_deg']
Human_p_out_deg = NetworkHumanDF['p_out_deg']
Bot_p_out_deg = NetworkBotDF['p_out_deg']


import numpy as np
import matplotlib.pyplot as plt


g1 = (Human_p_in_deg, Human_p_out_deg)
g2 = (Bot_p_in_deg,Bot_p_out_deg )

data = (g1, g2)
colors = ("blue", "red")
groups = ("Human", "Bot")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('p_in_deg and p_out_deg')
plt.legend(loc=2)
plt.show()