package com.demo.service;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.demo.entity.Address;
import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;

public class Buisness {
	
	public static void main (String args[])
	{
		Buisness obj = new Buisness();
		try {
			obj.getAddress("MANHATTAN");
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
		List<Address> li = new ArrayList<Address>();
		try (CSVReader reader = new CSVReader(new FileReader("D:\\ds\\interview\\cycleAddress.csv"))) {
		      String[] lineInArray;
		      while ((lineInArray = reader.readNext()) != null) {
		          System.out.println(lineInArray[0] + lineInArray[1] + "etc...");
		          if(lineInArray[0].equals(city))
		          {
		        	  Address obj = new Address();
			          obj.setLat(Double.parseDouble(lineInArray[1]));
			          obj.setLongi(Double.parseDouble(lineInArray[2]));
			          li.add(obj);  
		          }
		          
		      }
		  }	
		return li;
	}
}
