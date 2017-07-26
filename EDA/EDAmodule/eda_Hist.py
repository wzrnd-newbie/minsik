import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


NetworkDF = pd.read_csv('../log/(after) Network measures features.csv')
PinfoDF = pd.read_csv('../log/(after) Player information features.csv')
PactionDF = pd.read_csv('../log/(after) Player actions features.csv')
GactiveDF = pd.read_csv('../log/(after) Group activities features.csv')
SointerDF = pd.read_csv('../log/(after) Social interaction diversity features.csv')

mergetmp = pd.merge(NetworkDF.iloc[:,0:-1], PinfoDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergetmp = pd.merge(mergetmp, PactionDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergetmp = pd.merge(mergetmp, GactiveDF.drop(['A_Acc'], axis =1).iloc[:,0:-1], on='Actor', how='inner')
mergerDF = pd.merge(mergetmp, SointerDF.drop(['A_Acc'], axis =1), on='Actor', how='inner')





HumanDF = mergerDF.query('Type == "Human" & Max_level == 55')
BotDF = mergerDF.query('Type == "Bot" & Max_level == 55')

def MakeHist(bot_or_Human1, compareV1, bot_or_Human2, compareV2, Save_or_Not=0):

    compare1 = str(compareV1)
    compare2 = str(compareV2)

    Human_compare1 = HumanDF[compare1]
    Human_compare2 = HumanDF[compare2]
    Bot_compare1 = BotDF[compare1]
    Bot_compare2 = BotDF[compare2]

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