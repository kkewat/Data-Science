import pandas as pd
InputFileName='IP_DATA_CORE.csv'
OutputFileName='Retrieve_Router_Location.csv'
Base='F:/practical-data-science-master/VKHCG'
Print('############################')
print('Working Base : ',Base,'using')
Print('#############################')
sFileName=Base+'/01-Vermeulen/00-RawData/'+InputFileName
print('Loading : ',sFileName)
IP_DATA_ALL = pd.read_csv(sFileName,header=0,low_memory=False,usecols=['Country','Place Name','Latitude','Longitude'],encoding="latin-1")
IP_DATA_ALL.rename(columns={'PlaceName':'Place_Name'},inplace=True)
AllData = IP_DATA_ALL[['Country','Place_Name','Latitude']]
print(AllData)
MeanData=AllData.groupby(['Country','Place_Name'])('Latitude').mean()
print(MeanData)
