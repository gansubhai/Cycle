Stage 0
1. Extracting from external sources https://data.cityofnewyork.us/Public-Safety/NYPD-MotorVehicle-Collisions-Crashes/h9gi-nx95. First step is to do some data mining in the dataset.
TODO
Create an Script that given a BOROUGH it give the collisions information for injured killed cycles.
Please run the python script in PythonScript/Stage_0.py please check the path of appropriate csv file mention in the script

Stage 1
2. Loading the data
The second stage we are going to store the information in an external database (with a proper data model).
Recommendation:
Try to think if you need more than one entity to store the information.
TODO
Using the script that you created before to insert the data in a data store.
Please run the python script in PythonScript/Stage_1.py please check the database configuration in mysql

Stage 2
3. Visualization
The third stage is to visualize the data.
TODO
Create website that show information of where the crashes happend using a map
extra: filter by BOROUGH the crash accidents

Please clone CycleDemo and import it in eclipse ide , please clean and build the project and create a jar and run command java -jar CycleMap-0.0.1-SNAPSHOT.jar
Open url http://localhost:8080/cycle.html
In case eclipse IDE is not present run "mvn clean" and "mvn install" and then use target jar file create 

Stage 3
4. Analytics I
Save bike stations information https://s3.amazonaws.com/tripdata/index.html from 2019. The file
names are 201901-citibike-tripdata.csv.zip where 2019 is the year and 01 is the month.
Aggregate the files to have only the stations used in one year. The data source has bikes rides information
that contains the station name and id where the user grab the bike and the end station where he left the
bike (start_station_id, end_station_id)
TODO
Create an script for extracting the information from the bike stations and persist the data in a database.

Please run the python script in PythonScript/Stage_3.py please check the database configuration in mysql


Stage 4
5. Analytics II
Show the information of the bycicle stations in the same map and how close are they are from a crash
place.
Recommendation:
Use visualization techniques for showing how close are they from the crash station.
TODO
Show the bicycle stations in a map.
On select one of the stations you can see how close are they from a crash place.

Please clone CycleDemo and import it in eclipse ide , please clean and build the project and create a jar and run command java -jar CycleMap-0.0.1-SNAPSHOT.jar
Open url http://localhost:8080/station.html
In case eclipse IDE is not present run "mvn clean" and "mvn install" and then use target jar file create


Final Words
Good luck with the project and We hope this can be your first project in CreditShelf!!!