import string
import datetime as dt

#Removing leading or lagging spaces from a data enty
print('#1 removing lradin or lagging spaaces from a data entry')
baddata = " Data Science with too many spaces id bad!!!"
print('>',baddata,'<')
cleandata = baddata.strip()
print('>',cleandata,'<')

#2 Removing nonprintable charcters from a data entry
print('#2 Removing nonprintable characters from a data entry')
printable = set(string.printable)
baddata = "Data\x00Science with\x02 funny characters is \x10bad!!!"
cleandata = ' '.join(filter(lambda x: x in string.printable,baddata))
print('Bad Data :',baddata)
print('Clean Data : ',cleandata)


#3 Reformatting data entry to maych specific formatting criteria
#Convert YYYY/MM/DD to DD MONTH YYYY

print('# 3 Reforming data entry to match specific formatting criteria.')
baddate = dt.date(2019, 10, 31)
baddata=format(baddate,'%Y-%m-%d')
gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddate,'%d %B %Y')
print('Bad Data : ',baddata)
print('Good Data : ',gooddata)
