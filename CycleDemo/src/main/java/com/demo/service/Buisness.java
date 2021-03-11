package com.demo.service;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import com.demo.entity.Address;
import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;
import com.opencsv.exceptions.CsvValidationException;

public class Buisness {
	
	public static void main (String args[])
	{
		//readCSV();
		Buisness obj = new Buisness();
		try {
			//obj.getBikeStation();
			obj.getCities();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public List<Address> getAddress(String city) throws IOException, CsvException
	{
		System.out.println("||Buisness||getAddress||Starts ...");
		System.out.println("||Buisness||getAddress|| City looking for : "+city);
		
		ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		InputStream is = classloader.getResourceAsStream("cycleAddress.csv");
		Reader targetReader = new InputStreamReader(is);
		List<Address> li = new ArrayList<Address>();
		/*try (CSVReader reader = new CSVReader(new FileReader("D:\\ds\\interview\\cycleAddress.csv"))) {*/
		try (CSVReader reader = new CSVReader(targetReader)) {
		      String[] lineInArray;
		      while ((lineInArray = reader.readNext()) != null) {
		         
		          if(lineInArray[0].equals(city))
		          { System.out.println("||Buisness||getAddress|| Matched values latitude :"+lineInArray[1]+" || Longitude :"+lineInArray[2]);
		        	  Address obj = new Address();
			          obj.setLat(Double.parseDouble(lineInArray[1]));
			          obj.setLongi(Double.parseDouble(lineInArray[2]));
			          li.add(obj);  
			          
		          }
		          
		      }
		  }	
		System.out.println("||Buisness||getAddress||Ends !!!");
		return li;
	}
	
	public List<String> getBikeStation() throws IOException, CsvException
	{
		System.out.println("||Buisness||getBikeStation||Starts ...");
		ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		InputStream is = classloader.getResourceAsStream("cycleStationTop5Records.csv");
		Reader targetReader = new InputStreamReader(is);
		
		List<String> li = new ArrayList<String>();
		/*try (CSVReader reader = new CSVReader(new FileReader("D:\\ds\\cycleStationData\\cycleStationTop5Records.csv"))) {*/
		try (CSVReader reader = new CSVReader(targetReader)) {
		      String[] lineInArray;
		      while ((lineInArray = reader.readNext()) != null) {
		          System.out.println("||Buisness||getBikeStation|| BikeStationName: "+lineInArray[5]);
		          li.add(lineInArray[5]);
		        
		      }
		  }	
		System.out.println("||Buisness||getBikeStation||Ends ...");
		return li;
	}
	
	public List<Address> getBikeStationAddress(String bikeStation) throws IOException, CsvException
	{
		System.out.println("||Buisness||getBikeStationAddress||Starts ...");
		System.out.println("||Buisness||getBikeStationAddress||bikeStation address to be looked for :"+bikeStation);
		ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		InputStream is = classloader.getResourceAsStream("cycleStationTop5Records.csv");
		Reader targetReader = new InputStreamReader(is);
		List<Address> li = new ArrayList<Address>();
		/*try (CSVReader reader = new CSVReader(new FileReader("D:\\ds\\cycleStationData\\cycleStationTop5Records.csv"))) {*/
		try (CSVReader reader = new CSVReader(targetReader)) {
		      String[] lineInArray;
		      while ((lineInArray = reader.readNext()) != null) {
		          System.out.println("||Buisness||getBikeStation|| BikeStationName: "+lineInArray[5] +" || Latitude :"+ lineInArray[6] +" || Lomgitude :"+ lineInArray[7]);
		          if(lineInArray[5].equals(bikeStation))
		          {
		        	  Address obj = new Address();
			          obj.setLat(Double.parseDouble(lineInArray[6]));
			          obj.setLongi(Double.parseDouble(lineInArray[7]));
			          li.add(obj);  
		          }
		          
		      }
		  }	
		System.out.println("||Buisness||getBikeStationAddress||Ends ...");
		return li;
	}
	
	public List<Address> getCrashAddress(Double lat, Double longi) throws IOException, CsvException
	{
		System.out.println("||Buisness||getCrashAddress||Starts ...");
		System.out.println("||Buisness||getCrashAddress||Recived value for latitude:"+lat+" || longitude :"+longi);
		double startLatRange=0.0;
		double endLatRange=0.0;
		double startLongiRange=0.0;
		double endLongiRange=0.0;
		if(lat>0)
		{startLatRange=lat-0.02;
		endLatRange=lat+0.02;}
		else
		{startLatRange=lat+0.02;
		endLatRange=lat-0.02;}
		if(longi>0)
		{startLongiRange=longi-0.02;
		 endLongiRange=longi+0.02;}
		else
		{startLongiRange=longi-0.02;
		 endLongiRange=longi+0.02;}
		System.out.println("||Buisness||getCrashAddress|| Latitute:"+lat+" || Longitude:"+longi);
		System.out.println("||Buisness||getCrashAddress||Searching range Start Latitute:"+startLatRange+" || End Latitute::"+endLatRange);
		System.out.println("||Buisness||getCrashAddress||Searching range Start Longitude:"+startLongiRange+" || End Longitude::"+endLongiRange);
		ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		InputStream is = classloader.getResourceAsStream("CrashRecords.csv");
		Reader targetReader = new InputStreamReader(is);
		List<Address> li = new ArrayList<Address>();
		/*try (CSVReader reader = new CSVReader(new FileReader("D:\\ds\\cycleStationData\\CrashRecords.csv"))) {*/
		try (CSVReader reader = new CSVReader(targetReader)) {
		      String[] lineInArray;
		      while ((lineInArray = reader.readNext()) != null) {
		         /* System.out.println(lineInArray[1] + lineInArray[2] + lineInArray[3]);*/
		          if(Double.parseDouble(lineInArray[2])>=startLatRange && Double.parseDouble(lineInArray[2])<=endLatRange && Double.parseDouble(lineInArray[3])>=startLongiRange && Double.parseDouble(lineInArray[3])<=endLongiRange )
		          {
		        	  System.out.println("||Buisness||getCrashAddress||"+lineInArray[1] + lineInArray[2] + lineInArray[3]);
		        	  Address obj = new Address();
			          obj.setLat(Double.parseDouble(lineInArray[2]));
			          obj.setLongi(Double.parseDouble(lineInArray[3]));
			          li.add(obj);  
		          }
		          
		          if(li.size()>5)
		        	  break;
		          
		      }
		  }	
		System.out.println("||Buisness||getCrashAddress||Ends !!!");
		return li;
	}
	 
	
	public static void readCSV()
	{
		
		try {
			try (CSVReader reader = new CSVReader(new FileReader("D:\\ds\\cycleStationData\\CrashRecords.csv"))) {
			      String[] lineInArray;
			      while ((lineInArray = reader.readNext()) != null) {
			          System.out.println("||0||"+lineInArray[0] +"||1||"+ lineInArray[1] +"||2||"+ lineInArray[2]+"||3||"+lineInArray[3]);
			         
			          
			      }
			  }
		} catch (CsvValidationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
	}
	
	public List<String> getCities() throws IOException, CsvException
	{	
		System.out.println("||Buisness||getCities||Starts ...");
		ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		InputStream is = classloader.getResourceAsStream("city.csv");
		Reader targetReader = new InputStreamReader(is);
		List<String> li = new ArrayList<String>();
		try {
			try (CSVReader reader = new CSVReader(targetReader)) {
		      String[] lineInArray;
		      while ((lineInArray = reader.readNext()) != null) {
		          System.out.println("||Buisness||getCities||"+lineInArray[0]);
		          li.add(lineInArray[0]);
		         
		          
		      }
		  }	
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("||Buisness||getCities||Ends !!!");
		return li;
	}
}
