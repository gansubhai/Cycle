package com.demo.controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.demo.entity.Address;
import com.demo.service.Buisness;
import com.opencsv.exceptions.CsvException;

@RestController
public class DemoController {

	@RequestMapping(value = "/getCities", method = RequestMethod.GET, headers = "Accept=application/json")
	@ResponseBody
	public List<String> getCities() {
		System.out.println("||DemoController||getCities||Starts ...");
		Buisness obj = new Buisness();
		List<String> li = null;

		try {
			li = obj.getCities();
			Collections.sort(li);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("||DemoController||getCities||Ends ...");
		return li;
	}

	@RequestMapping(value = "/getBikeStation", method = RequestMethod.GET, headers = "Accept=application/json")
	@ResponseBody
	public List<String> getBikeStation() {
		System.out.println("||DemoController||getBikeStation||Starts ...");
		Buisness obj = new Buisness();
		List<String> li = null;
		try {
			li = obj.getBikeStation();
			Collections.sort(li);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		System.out.println("||DemoController||getBikeStation||Ens !!!");
		return li;
	}

	@RequestMapping(value = "/getAddress", method = RequestMethod.POST, headers = "Accept=application/json")
	@ResponseBody
	public Map<String, Object> getAddress(@RequestBody Map<String, String> bothVar, HttpServletRequest request) {
		System.out.println("||DemoController||getAddress||Starts ...");
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
		System.out.println("||DemoController||getAddress||Ends !!!");
		return mp;
	}

	@RequestMapping(value = "/getCrashNearByAddress", method = RequestMethod.POST, headers = "Accept=application/json")
	public Map<String, Object> getCrashNearByAddress(@RequestBody Map<String, String> bothVar,
			HttpServletRequest request) {
		System.out.println("||DemoController||getCrashNearByAddress||Starts ...");
		Map<String, Object> mp = new HashMap<String, Object>();
		Buisness obj = new Buisness();
		try {
			List<Address> li = obj.getBikeStationAddress(bothVar.get("inputBikeStation"));
			mp.put("bikeStationAddress", li);
			mp.put("crashAddress", obj.getCrashAddress(li.get(0).getLat(), li.get(0).getLongi()));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("||DemoController||getCrashNearByAddress||Ends ...");
		return mp;
	}

}
