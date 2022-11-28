import pandas as pd 
sInputFileName = 'F:\Country_Code.csv'
InputData = pd.read_csv(sInputFileName,encoding="latin-1")
print('Input Data Values =======================================')
print(InputData)
print("===================================================")

# Processing Rules===================
ProcessData = InputData
#Remove Coolumns iso2code and iso3 code
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-CODE',axis=1,inplace=True)
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'countryNumber'},inplace=True)
# set new index
ProcessData.set_index('CountryNumber',inplace=True)
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print('Process data values======================')
print(ProcessData)
print('===========================')
OutputData = ProcessData
sOutputFileName='F:\MSC\ds\Horus-csv-country.csv'
OutputData.to_csv(sOutputFileName,index=False)
Print('Done')