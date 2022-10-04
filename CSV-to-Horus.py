#CSV To Horus

import pandas as pd

sInputFileName = 'F:/Data_Science/practical-data-science-master/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData = pd.read_csv(sInputFileName,encoding="latin-1")
print('Input data Values=================================')
print(InputData)
print('===============================')
# Processing Rules
ProcessData = InputData

#Remove Columns ISO-2-Code and ISO-3-Code
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-CODE',axis=1,inplace=True)

#Rename Cloumns Country and ISO-M49
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

#Set new Index
ProcessData.set_index('CountryNumber',inplace=True)

#Sort Data by Country Number
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)

print('Processed Data Values===============')
print(ProcessData)
print('====================================')

#Output Agreement
OutputData = ProcessData
sOutputFileName='F:/Data_Science/OP/Horus-to-CSV.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('CSV to Horus Done====================')
#END
