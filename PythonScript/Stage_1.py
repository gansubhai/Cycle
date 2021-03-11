#Stage 1
#2. Loading the data
#The second stage we are going to store the information in an external database (with a proper data model).
#Recommendation:
#Try to think if you need more than one entity to store the information.
#TODOUsing the script that you created before to insert the data in a data store.
#LOAD ABOVE DATA TO TABLES
import pyodbc
import pandas as pd
import numphy as np

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
