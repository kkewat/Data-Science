import pandas as pd
import sqlite3 as sq

sInputFileName ='C:/Users/JAI AMBE/Downloads/utility.db'
#'F:/Data_Science/practical-data-science-master/VKHCG/05-DS/9999-Data/utility.db'
sInputTable = 'Country_Code'
conn=sq.connect(sInputFileName)
sSql='select * FROM '+sInputTable+';'
InputData = pd.read_sql_query(sSql,conn)
print('Input Data Tables')
print(InputData)
print('============================================')

ProcessData = InputData

ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)

ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

ProcessData.set_index('CountryNumber',inplace=True)
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)

print('Process Data Values')
print(ProcessData)
print('=========================================')

OutputData = ProcessData
sOutputFileName='F:\\Data_Science\\OP\\SQl-to-Horus.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('DAtabase to CSv done')
