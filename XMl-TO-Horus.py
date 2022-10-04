import pandas as pd
import xml.etree.ElementTree as ET
'''
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[1]):
        schild = str(header[index])
        child = ET.SubElement(entry,schild)
        if str(data[schild][row])!='nan':
            child.text =str(data[schild][row])
        else:
            child.text = 'n/a'
        entry.append(child)
    result = ET.tostring(root)
    return result
'''
def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for i,child in enumerate(root):
        record={}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

#Input File
sInputFileName = 'F:/Data_Science/practical-data-science-master/VKHCG/05-DS/9999-Data/Country_Code.xml'
InputData = open(sInputFileName).read()
print('=======================================================================')
print('Input Data Values======================================================')
print('=======================================================================')
print(InputData)
print('=======================================================================')

#Processing Rules
ProcessDataXML = InputData

#Xml to  data frame
ProcessData = xml2df(ProcessDataXML)

#Remove Columns ISO-2-CODE AND ISO-3-CODE
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)

#Rename Country and ISO-M49
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

#Set new Index
ProcessData.set_index('CountryNumber',inplace=True)
#Sort data by CurrencyNumber
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print('=========================================================================')
print('Process Data Values======================================================')
print('========================================================================')
print(ProcessData)
print('=========================================================================')
OutputData = ProcessData
sOutputFileName = 'F:\\Data_Science\\OP\\Xml-To-CSV.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('=========================================================================')
print('XML to HORUS Done')
print('=========================================================================')
