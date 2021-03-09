Stage 0
1. Extracting from external sources https://data.cityofnewyork.us/Public-Safety/NYPD-MotorVehicle-Collisions-Crashes/h9gi-nx95. First step is to do some data mining in the dataset.
TODO
Create an Script that given a BOROUGH it give the collisions information for injured killed cycles

import pandas as pd
import numphy as np
from matlib import pyplot as plt
%matplotlib inline
import matplotlib

df1= pd.read_csv("Vehicle_Colliosion.csv")
df1.head()
list(df1)
df1['BOROUGH'].unique()
df2=df1[df1['BOROUGH'].notna()]
dfCycle=df2[df2['NUMBER OF CYCLIST INJURED'] >0 | df2['NUMBER OF CYCLIST KILLED'] >0]
dfCycle.to_csv('cycle.csv')

def getInjuredCyclist(city):
    subset_df = dfCycle[dfCycle["BOROUGH"] == city]
	column_sum= subset_df['NUMBER OF CYCLIST INJURED'].sum()
	return column_sum
	
def getInjuredKilled(city):
    subset_df = dfCycle[dfCycle["BOROUGH"] == city]
	column_sum= subset_df['NUMBER OF CYCLIST KILLED'].sum()
	return column_sum	
	
	
dfCycle.to_csv('cycle_Address.csv',[columns=['COLLISION_ID','CRASH DATE','BOROUGH','ZIP CODE','LATITUDE','LONGITUDE','LOCATION','ON STREET NAME','CROSS STREET NAME','OFF STREET NAME']])
dfCycle.to_csv('cycle_Accidents.csv',[columns=['COLLUSION_ID','NUMBER OF PERSONS INJURED','NUMBER OF PEDESTRIANS INJURED','NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED','NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED','NUMBER OF MOTORIST KILLED' ]])
dfCycle.to_csv('cycle_Vehicles.csv',[columns=['COLLUSION_ID','CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3','CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5','VEHICLE TYPE CODE 1','VEHICLE TYPE CODE 2','VEHICLE TYPE CODE 3','VEHICLE TYPE CODE 4','VEHICLE TYPE CODE 5'])

Stage 1
2. Loading the data
The second stage we are going to store the information in an external database (with a proper data model).
Recommendation:
Try to think if you need more than one entity to store the information.
TODOUsing the script that you created before to insert the data in a data store.
#LOAD ABOVE DATA TO TABLES
import pyodbc

conn = pyodbc.connect('DRIVER={SQL SERVER};'
					  'Server=RON\SQLEXPRESS;'
					  'Database=TestDB;'
					  'Trusted_Connection=yes;')
cursor = conn.cursor()
dfCycle_Address = pd.read_csv('cycle_Address.csv')
dfCycle_Accidents = pd.read_csv('cycle_Accidents.csv')
dfCycle_Vehicles = pd.read_csv('cycle_Vehicles.csv')

for row in dfCycle_Address.itertuples():
     cursor.execute('''
	                INSERT INTO TestDB.cycle_Address('COLLISION_ID','CRASH DATE','BOROUGH','ZIP CODE','LATITUDE','LONGITUDE','LOCATION','ON STREET NAME','CROSS STREET NAME','OFF STREET NAME') VALUES(?,?,?,?,?,?,?,?,?,?,?),row.COLLISION_ID,row.CRASH DATE,row.BOROUGH,row.ZIP CODE,row.LATITUDE,row.LONGITUDE,row.LOCATION,row.ON STREET NAME,row.CROSS STREET NAME,row.OFF STREET NAME']])''')

conn.commit()					

for row in dfCycle_Accidents.itertuples():
     cursor.execute('''
	                INSERT INTO TestDB.cycle_Accidents('COLLUSION_ID','NUMBER OF PERSONS INJURED','NUMBER OF PEDESTRIANS INJURED','NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED','NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED','NUMBER OF MOTORIST KILLED' ) VALUES(?,?,?,?,?,?,?,?,?),row.COLLUSION_ID,row.NUMBER OF PERSONS INJURED,row.NUMBER OF PEDESTRIANS INJURED,row.NUMBER OF PEDESTRIANS KILLED,row.NUMBER OF CYCLIST INJURED,row.NUMBER OF CYCLIST KILLED,row.NUMBER OF MOTORIST INJURED,row.NUMBER OF MOTORIST KILLED' ]])''')

conn.commit()	


for row in dfCycle_Vehicles.itertuples():
     cursor.execute('''
	                INSERT INTO TestDB.cycle_Vehicles('COLLUSION_ID','CONTRIBUTING FACTOR VEHICLE 1','CONTRIBUTING FACTOR VEHICLE 2','CONTRIBUTING FACTOR VEHICLE 3','CONTRIBUTING FACTOR VEHICLE 4','CONTRIBUTING FACTOR VEHICLE 5','VEHICLE TYPE CODE 1','VEHICLE TYPE CODE 2','VEHICLE TYPE CODE 3','VEHICLE TYPE CODE 4','VEHICLE TYPE CODE 5') VALUES(?,?,?,?,?,?,?,?,?,?,?),row.COLLISION_ID,row.CONTRIBUTING FACTOR VEHICLE 1,row.CONTRIBUTING FACTOR VEHICLE 2,row.CONTRIBUTING FACTOR VEHICLE 3,row.CONTRIBUTING FACTOR VEHICLE 4,row.CONTRIBUTING FACTOR VEHICLE 5,row.VEHICLE TYPE CODE 1,row.VEHICLE TYPE CODE 2,row.VEHICLE TYPE CODE 3,row.VEHICLE TYPE CODE 4,row.VEHICLE TYPE CODE 5']])''')

conn.commit()


# Stage 4 Analyatics 1

dfTrip01=pd.read_csv('201901.csv')
dfTrip02=pd.read_csv('201902.csv')
dfTrip03=pd.read_csv('201903.csv')
dfTrip04=pd.read_csv('201904.csv')
dfTrip05=pd.read_csv('201905.csv')
dfTrip06=pd.read_csv('201906.csv')
dfTrip07=pd.read_csv('201907.csv')
dfTrip01=pd.read_csv('201908.csv')
dfTrip08=pd.read_csv('201909.csv')
dfTrip09=pd.read_csv('201910.csv')
dfTrip10=pd.read_csv('201911.csv')
dfTrip11=pd.read_csv('201912.csv')
dfTrip12=pd.read_csv('201913.csv')

frames = [dfTrip01,dfTrip02,dfTrip03,dfTrip04,dfTrip05,dfTrip06,dfTrip07,dfTrip08,dfTrip09,dfTrip10,dfTrip11,dfTrip12]
result= pd.concat(frames)
list(result)

startStationNameUnique= result['start station name'].unique()
endStationNameUnique= result['end station name'].unique()
allStation = np .concat((startStationNameUnique,endStationNameUnique))
allStationSet = list(set(allStation))
len(allStationSet)

for row in result.itertuples():
     cursor.execute('''
	                INSERT INTO TestDB.tripDate('tripduration','startTime','stopTime','start station id','start station name','start station latitude','start station longitude','end station id','end station name','end station latitude',
					'end station longitude') VALUES(?,?,?,?,?,?,?,?,?,?,?),row.tripduration,row.startTime,row.stopTime,row.start station id,row.start station name,row.start station latitude',
					'start station longitude,row.end station id,row.end station name,row.end station latitude','end station longitude']])''')

conn.commit()

# Stage 5 Analyatics 2

def getCrashesNearBy(lat,lon):

    selectedStationArea = dfCycle[(dfCycle['LATITUDE']> lat+0.2) & (dfCycle['LATITUDE']> lat-0.2) & (dfCycle['LONGITUDE']> lon+0.2) & (dfCycle['LONGITUDE']> lon-0.2)]
	return selectedStationArea
	