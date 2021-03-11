#Stage 3
#4. Analytics I
#Save bike stations information https://s3.amazonaws.com/tripdata/index.html from 2019. The file
#names are 201901-citibike-tripdata.csv.zip where 2019 is the year and 01 is the month.
#Aggregate the files to have only the stations used in one year. The data source has bikes rides information
#that contains the station name and id where the user grab the bike and the end station where he left the
#bike (start_station_id, end_station_id)
#TODO
#Create an script for extracting the information from the bike stations and persist the data in a database.
import pandas as pd
import numphy as np


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
	