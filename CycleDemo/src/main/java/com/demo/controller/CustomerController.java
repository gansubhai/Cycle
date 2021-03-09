package com.demo.controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.demo.service.Buisness;
import com.opencsv.exceptions.CsvException;

@RestController
public class CustomerController {

	
	@RequestMapping(value = "/getCities", method = RequestMethod.GET, headers = "Accept=application/json")
	public List<String> getAllCustomers() {

		List<String> li = new ArrayList<String>();
		li.add("MANHATTAN");
		li.add("BROKLYN");
		li.add("BRONX");
		li.add("QUEENS");
		li.add("STATEN ISLAND");
		Collections.sort(li);
		return li;
	}

	
	@RequestMapping(value = "/getAddress", method = RequestMethod.POST, headers = "Accept=application/json")
	public Map<String,Object> getAddress(@RequestBody Map<String,String> bothVar, HttpServletRequest request)
	{
		Map<String, Object> mp = new HashMap<String, Object>();
		Buisness obj = new Buisness();
		try {
			mp.put("address", obj.getAddress(bothVar.get("inputCity")));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return mp;
	}
	
	@RequestMapping(value = "/getCrashNearByAddress", method = RequestMethod.POST, headers = "Accept=application/json")
	public Map<String,Object> getCrashNearByAddress(@RequestBody Map<String,String> bothVar, HttpServletRequest request)
	{
		Map<String, Object> mp = new HashMap<String, Object>();
		Buisness obj = new Buisness();
		try {
			mp.put("address", obj.getAddress(bothVar.get("inputCity")));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return mp;
	}
	

	

	/*@RequestMapping(value = "/addCustomer", method = RequestMethod.POST, headers = "Accept=application/json")
	public Customer addCustomer(@RequestBody Customer customer) {
		return customerService.addCustomer(customer);

	}*/

	}
