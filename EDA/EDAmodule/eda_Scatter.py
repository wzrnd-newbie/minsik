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

Bot_Net_Info_merge = pd.merge(MaxLevelBot_Actor, NetworkBotDF, on='Actor', how='inner')
Human_Net_Info_merge = pd.merge(MaxLevelHuman_Actor, NetworkHumanDF, on='Actor', how='inner')



def MakeScatter(bot_or_Human1, bot_or_Human2, compareV1, compareV2, Save_or_Not=0):

    compare1 = str(compareV1)
    compare2 = str(compareV2)


    Human_compare1 = Human_Net_Info_merge[compare1]
    Human_compare2 = Human_Net_Info_merge[compare2]
    Bot_compare1 = Bot_Net_Info_merge[compare1]
    Bot_compare2 = Bot_Net_Info_merge[compare2]


    if (bot_or_Human1 =='Human'):
        x = Human_compare1
        y = Human_compare2

    elif(bot_or_Human1 =='Bot'):
        x = Bot_compare1
        y = Bot_compare2

    if (bot_or_Human2 == 'Human'):
        x1 = Human_compare1
        y1 = Human_compare2
    elif (bot_or_Human2 == 'Bot'):
        x1 = Bot_compare1
        y1 = Bot_compare2


    # scatter
    g1 = (x, y)
    g2 = (x1, y1)

    data = (g1, g2)
    colors = ("blue", "red")
    groups = ("Human", "Bot")

    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    titlename = '%s & %s  %s_%s'%(bot_or_Human1, bot_or_Human2, compare1, compare2)

    plt.title(titlename)
    plt.xlabel('%s'%compare1)
    plt.ylabel('%s'%compare2)
    plt.legend(loc=2)
    if (Save_or_Not == 1):
        plt.savefig("EDAPicture/Scatter/" + "(Scatter)" + titlename)
    plt.show()

#if __name__ == "__main__":
#    MakeScatter('Human', 'Bot', 'p_in_deg', 'p_out_deg')




