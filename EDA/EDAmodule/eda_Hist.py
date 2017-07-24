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

def MakeHist(bot_or_Human1, compareV1, bot_or_Human2, compareV2, Save_or_Not=0):

    compare1 = str(compareV1)
    compare2 = str(compareV2)

    Human_compare1 = Human_Net_Info_merge[compare1]
    Human_compare2 = Human_Net_Info_merge[compare2]
    Bot_compare1 = Bot_Net_Info_merge[compare1]
    Bot_compare2 = Bot_Net_Info_merge[compare2]

    if (bot_or_Human1 =='Human'):
        x = Human_compare1
    elif(bot_or_Human1 =='Bot'):
        x = Bot_compare1

    if (bot_or_Human2 == 'Human'):
        y = Human_compare2
    elif (bot_or_Human2 == 'Bot'):
        y = Bot_compare2

    bins = np.linspace(-10, 100, 100)
    titlename = '%s_%s & %s_%s'%(bot_or_Human1, compare1, bot_or_Human2, compare2)
    plt.hist(x, bins, alpha=0.5, label='%s_%s'%(bot_or_Human1, compare1), color = "b")
    plt.hist(y, bins, alpha=0.5, label='%s_%s'%(bot_or_Human2, compare2), color = "r")
    plt.legend(loc='upper right')
    plt.title('%s'%titlename)
    if (Save_or_Not==1):
        plt.savefig("EDAPicture/Hist/"+"(Hist)"+titlename)
    plt.show()

#if __name__ == "__main__":
#    MakeHist('Human', 'p_in_deg', 'Human', 'p_out_deg')