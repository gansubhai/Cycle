#Stage 0
#1. Extracting from external sources https://data.cityofnewyork.us/Public-Safety/NYPD-MotorVehicle-Collisions-Crashes/h9gi-nx95. First step is to do some #data mining in the dataset.
#TODO
#Create an Script that given a BOROUGH it give the collisions information for injured killed cycles

import pandas as pd
import numphy as np

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