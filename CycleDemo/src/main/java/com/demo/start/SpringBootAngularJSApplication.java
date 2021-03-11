package com.demo.start;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = {"com.demo"})
public class SpringBootAngularJSApplication {

	public static void main(String[] args) 
	{
		SpringApplication.run(SpringBootAngularJSApplication.class, args);   
	}
}