# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061217.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
def get_max(target_data, ls , station_id):
   try:
      ls = sorted(ls,key=lambda x:x['WDSD'],reverse = True)   
      target_data.append( [station_id,float(ls[0]['WDSD'])-float(ls[-1]['WDSD'])] )
   except:
      target_data.append( [station_id,None] )
target_data = []
C0A880 = []
C0F9A0 = []
C0G640 = []
C0R190 = []
C0X260 = []
for i in data:
   if i['WDSD'] == '-99.000' or i['WDSD'] == '-999.000':
      data.remove(i)
   if i['station_id'] == 'C0A880':
      C0A880.append(i)
   elif i['station_id'] == 'C0F9A0':
      C0F9A0.append(i)
   elif i['station_id'] == 'C0G640':
      C0G640.append(i)
   elif i['station_id'] == 'C0R190':
      C0R190.append(i)
   elif i['station_id'] == 'C0X260':
      C0X260.append(i)
get_max(target_data,C0A880,'C0A880')
get_max(target_data,C0F9A0,'C0F9A0')
get_max(target_data,C0G640,'C0G640')
get_max(target_data,C0R190,'C0R190')
get_max(target_data,C0X260,'C0X260')

target_data = sorted(target_data,key=lambda x:x[0]) 


#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================