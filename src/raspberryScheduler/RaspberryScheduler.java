package raspberryScheduler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.Comparator;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;

public class RaspberryScheduler {

	private boolean isInitialized;
	private File settingsFile;
	private long settingsFileTimeStamp;
	
	private final GpioController controller;
	
	private HashMap<Integer, RaspberryGPIO> GPIOMap = new HashMap<>();
	
	public RaspberryScheduler() {

		boolean errorFound = false;

		if(RaspberrySchedulerSettings.DEBUG == false)
		{
			controller = GpioFactory.getInstance();
		}
		else
		{
			controller = null;
		}
		
		if(createFiles() == false)
		{
			errorFound = true;
		}

		if(errorFound == false)
		{
			errorFound = readSettingsFile();
		}

		if(errorFound == false)
		{
			this.isInitialized = true;
		}
	}
	
	private boolean readSettingsFile()
	{
		boolean errorFound = false;
		
		BufferedReader br = null;
		try {
			br = new BufferedReader(new FileReader(settingsFile));
			
			boolean startFound = false;
			int gpioId = 0;
			
			List<String> ScheduleStringList = new ArrayList<>();
			
		    String line = br.readLine();
		    while (line != null) {
		    	
		    	line = line.trim();
		    	
		    	if(line.startsWith("[GPIO"))
		    	{
		    		gpioId = getPinIdFromString(line.trim());
		    		
		    		ScheduleStringList.clear();
		    		
		    		if(gpioId > 0)
		    		{
		    			startFound = true;
		    		}
		    	}
		    	else if(line.startsWith("[/GPIO"))
		    	{
		    		if(startFound == false)
		    		{
		    			printMessage("");
		    		}
		    		
		    		startFound = false;
		    		
		    		HashMap<Integer, List<RaspberrySchedule>> DayScheduleMap = getSchedulesFromStringList(ScheduleStringList);
		    		if(DayScheduleMap != null)
		    		{
		    			RaspberryGPIO gpio = new RaspberryGPIO(gpioId, controller);
		    			gpio.setSchedule(DayScheduleMap);
		    			
		    			if(GPIOMap.get(gpioId) == null)
		    			{
		    				GPIOMap.put(gpioId, gpio);
		    			}
		    			else
		    			{
		    				printMessage("GPIO with ID [" + gpioId + "] has been defined multiple times. Using the first setting.");
		    			}
		    		}
		    	}
		    	else if(startFound == true)
		    	{
	    			ScheduleStringList.add(line.trim());
		    	}
		    	
		        line = br.readLine();
		    }
		    
		} catch (Exception e) {
			printMessage("Could not open settings file(" + RaspberrySchedulerSettings.SETTINGS_FILE_NAME + ").");
			errorFound = true;
		} finally {
			if(br != null)
			{
				try {
					br.close();
				} catch (Exception e2) {
					errorFound = true;
					printMessage("Could not close settings file(" + RaspberrySchedulerSettings.SETTINGS_FILE_NAME + ").");
				}
			}
		}
		
		if(errorFound == false)
		{
			settingsFileTimeStamp = settingsFile.lastModified();
		}
		
		return errorFound;
	}
	
	public boolean isInitialized()
	{
		return this.isInitialized;
	}
	
	public void start()
	{
		while(true)
		{
			if(settingsFile.lastModified() != settingsFileTimeStamp)
			{
				if(readSettingsFile() == true)
				{
					printMessage("Setting file modified but could not be read.");
					break;
				}
			}
			
			for (RaspberryGPIO raspberryGPIO : GPIOMap.values()) {
				
				raspberryGPIO.checkSchedule();
			}
		}
	}
	
	private boolean createFiles()
	{
		settingsFile = new File(RaspberrySchedulerSettings.SETTINGS_FILE_NAME);

		if(!settingsFile.exists())
		{
			printMessage("Could not find settings file(" + RaspberrySchedulerSettings.SETTINGS_FILE_NAME + ").");
			return false;
		}
		
		return true;
	}

	private void printMessage(String message)
	{
		Calendar cal = Calendar.getInstance();
		String dateAndTime = RaspberrySchedulerSettings.DATE_FORMAT.format(cal.getTime());

		message = "["+dateAndTime+"] " + message;
		
		System.out.println(message);
		
		if(RaspberrySchedulerSettings.PRINT_TO_LOG)
		{
			appendToLog(message);
		}
	}
	
	private void appendToLog(String message)
	{
		try {
		    Files.write(Paths.get(RaspberrySchedulerSettings.LOG_FILE_NAME), message.getBytes(), StandardOpenOption.APPEND);
		}catch (IOException e) {
		}
	}
	
	private Integer getPinIdFromString(String s)
	{
		s = s.trim();
		
		if(s.startsWith("[") && s.endsWith("]"))
		{
			int startIndex = s.indexOf("=");
			int endIndex = s.indexOf("]");
			
			if(startIndex > 0 && endIndex > 0)
			{
				s = s.substring(startIndex+1, endIndex);
				
				int retVal = getIntegerFromString(s);
				if(retVal >= 0)
				{
					return retVal;
				}
				else
				{
					printMessage("Could not extract the PIN ID from : " + s);
				}
			}
		}
		
		return -1;
	}
	
	private Integer getIntegerFromString(String s)
	{
		s = s.trim();
		
		try {
			return Integer.valueOf(s);
		} catch (Exception e) {
		}
		
		return -1;
	}
	
	private HashMap<Integer, List<RaspberrySchedule>> getSchedulesFromStringList(List<String> StringList)
	{
		HashMap<Integer, List<RaspberrySchedule>> DayToScheduleMap = new HashMap<>();
		boolean errorFound = false;
		
		for (String string : StringList) {
			
			String[] parts = string.split("\\|");
			if(parts.length > 0)
			{
				int dayIndex = getDayFromScheduleString(parts[0]); 
				
				if(dayIndex > 0)
				{
					List<RaspberrySchedule> ScheduleList = new ArrayList<>();
					
					for (int i=1;i<parts.length;i++) 
					{
						String part = parts[i];
						
						if(part.startsWith("[") && part.endsWith("]"))
						{
							int count = part.length() - part.replace(",", "").length();

							if(count == 0)
							{
								RaspberrySchedule schedule = getScheduleFromTimePeriod(part);
								
								if(schedule != null)
								{
									ScheduleList.add(schedule);
								}
								else
								{
									errorFound = true;
								}
							}
							else if(count == 2)
							{
								List<RaspberrySchedule> ScheduleListTemp = getScheduleFromTimePeriodTimeOnTimeOff(part);
								if(ScheduleListTemp != null && ScheduleListTemp.size() > 0)
								{
									ScheduleList.addAll(ScheduleListTemp);
								}
								else
								{
									errorFound = true;
								}
							}
							else if(count == 3)
							{
								List<RaspberrySchedule> ScheduleListTemp = getScheduleFromStartTimeOnTimeOffRepetitions(part);
								if(ScheduleListTemp != null && ScheduleListTemp.size() > 0)
								{
									ScheduleList.addAll(ScheduleListTemp);
								}
								else
								{
									errorFound = true;
								}
							}
							else
							{
								errorFound = true;
							}
						}
						else
						{
							errorFound = true;
						}
						
						if(errorFound == true)
						{
							printMessage("Could not extract schedule from: " + part);
							break;
						}
					}

					if(errorFound == false)
					{
						//first sort the list so we can make searching more efficient
						Collections.sort(ScheduleList, new Comparator<RaspberrySchedule>() {
							@Override
							public int compare(RaspberrySchedule left, RaspberrySchedule right) {

								Integer leftStart = left.getStartHour()*100 + left.getStartMinute();
								Integer rightStart = right.getStartHour()*100 + right.getStartMinute();

								return leftStart.compareTo(rightStart); 
							}
						});
						
						DayToScheduleMap.put(dayIndex, ScheduleList);
					}
					else
					{
						break;
					}
				}
				else
				{
					printMessage("Could not extract day from " + parts[0]);
					errorFound = true;
				}
			}
		}
		
		if(errorFound == false)
		{
			return DayToScheduleMap;
		}
		
		return null;
	}
	
	private Integer getDayFromScheduleString(String s)
	{
		s = s.trim();
		
		if(s.startsWith("[") && s.endsWith("]"))
		{
			s = s.substring(1, s.length()-1).trim();
			
			int index = getDayIndexFromName(s);
			
			if(index > 0)
			{
				return index;
			}
		}
		
		return null;
	}
	
	private RaspberrySchedule getScheduleFromTimePeriod(String s)
	{
		s = s.trim();
		
		if(s.startsWith("[") && s.endsWith("]"))
		{
			s = s.substring(1, s.length()-1).trim();
			
			String[] parts = s.split("-");
			if(parts.length == 2)
			{
				Calendar startTime = getHourAndMinutesFromString(parts[0]);
				Calendar endTime = getHourAndMinutesFromString(parts[1]);
				
				if(startTime != null && endTime != null)
				{
					int startTimeHour = startTime.get(Calendar.HOUR_OF_DAY);
					int startTimeMinute =  startTime.get(Calendar.MINUTE);
					
					int endTimeHour = endTime.get(Calendar.HOUR_OF_DAY);
					int endTimeMinute =  endTime.get(Calendar.MINUTE);
					
					if(endTimeHour == 0 && endTimeMinute == 0)
					{
						endTimeHour = 24;
					}
			
					RaspberrySchedule schedule = new RaspberrySchedule(startTimeHour, startTimeMinute, endTimeHour, endTimeMinute);
					
					return schedule;
				}
			}
		}
		
		return null;
	}
	
	private List<RaspberrySchedule> getScheduleFromTimePeriodTimeOnTimeOff(String s)
	{
		List<RaspberrySchedule> ScheduleList = new ArrayList<>();
		boolean errorFound = false;
		
		s = s.trim();
		
		if(s.startsWith("[") && s.endsWith("]"))
		{
			s = s.substring(1, s.length()-1).trim();
			
			String[] parts = s.split(",");
		
			String[] partsPeriod = parts[0].split("-");
			if(partsPeriod.length == 2)
			{
				Calendar startTime = getHourAndMinutesFromString(partsPeriod[0]);
				Calendar endTime = getHourAndMinutesFromString(partsPeriod[1]);

				int timeOn = getIntegerFromString(parts[1]);
				int timeOff = getIntegerFromString(parts[2]);
				
				if(startTime != null && endTime != null && timeOn > 0 && timeOff > 0)
				{
					Calendar newEndTime = Calendar.getInstance();
					
					while(startTime.before(endTime))
					{
						newEndTime.setTime(startTime.getTime());
						newEndTime.add(Calendar.MINUTE, timeOn);
						
						if(newEndTime.after(endTime))
						{
							newEndTime.setTime(endTime.getTime());
						}
						
						int startTimeHour = startTime.get(Calendar.HOUR_OF_DAY);
						int startTimeMinute =  startTime.get(Calendar.MINUTE);
						
						int endTimeHour = newEndTime.get(Calendar.HOUR_OF_DAY);
						int endTimeMinute =  newEndTime.get(Calendar.MINUTE);
						
						RaspberrySchedule schedule = new RaspberrySchedule(startTimeHour, startTimeMinute, endTimeHour, endTimeMinute);
						ScheduleList.add(schedule);
						
						startTime.add(Calendar.MINUTE, timeOn + timeOff);
					}
				}
				else
				{
					errorFound = true;
				}
			}
			else
			{
				errorFound = true;
			}
		}
		else
		{
			errorFound = true;
		}
		
		if(errorFound == false)
		{
			return ScheduleList;
		}
		
		return null;
	}
	
	private List<RaspberrySchedule> getScheduleFromStartTimeOnTimeOffRepetitions(String s)
	{
		List<RaspberrySchedule> ScheduleList = new ArrayList<>();
		boolean errorFound = false;
		
		s = s.trim();
		
		if(s.startsWith("[") && s.endsWith("]"))
		{
			s = s.substring(1, s.length()-1).trim();
			
			String[] parts = s.split(",");
		
			Calendar startTime = getHourAndMinutesFromString(parts[0]);

			int timeOn = getIntegerFromString(parts[1]);
			int timeOff = getIntegerFromString(parts[2]);
			int repetitions = getIntegerFromString(parts[3]);
			
			if(startTime != null && timeOn > 0 && timeOff > 0 && repetitions > 0)
			{
				Calendar newEndTime = Calendar.getInstance();
				
				while(repetitions > 0)
				{
					newEndTime.setTime(startTime.getTime());
					newEndTime.add(Calendar.MINUTE, timeOn);
					
					RaspberrySchedule schedule = new RaspberrySchedule(startTime.get(Calendar.HOUR_OF_DAY), startTime.get(Calendar.MINUTE), newEndTime.get(Calendar.HOUR_OF_DAY), newEndTime.get(Calendar.MINUTE));
					ScheduleList.add(schedule);
					
					startTime.add(Calendar.MINUTE, timeOn + timeOff);
					
					repetitions--;
				}
			}
			else
			{
				errorFound = true;
			}
		}
		else
		{
			errorFound = true;
		}
		
		if(errorFound == false)
		{
			return ScheduleList;
		}
		
		return null;
	}
	
	private int getDayIndexFromName(String s)
	{
		s = s.toLowerCase();
		
		if(RaspberrySchedulerSettings.DAYS_OF_WEEK.contains(s))
		{
			return RaspberrySchedulerSettings.DAYS_OF_WEEK.indexOf(s);
		}
		
		return -1;
	}
	
	private Calendar getHourAndMinutesFromString(String s)
	{
		try {
			SimpleDateFormat parser = new SimpleDateFormat("hh:mm");
			Date date = parser.parse(s);
			Calendar cal = Calendar.getInstance();
			cal.setTime(date);
			
			return cal;
		} catch (Exception e) {
		}	
		
		return null;
	}
}
