
import pandas as pd


ClusterDF = pd.read_csv('../log/TotalLogGrouping.csv')



print(ClusterDF.query('Group == 1').describe())
exit()

