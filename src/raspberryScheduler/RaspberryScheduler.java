package raspberryScheduler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class RaspberryScheduler {

	private boolean isInitialized;
	
	private File settingsFile;
	
	private long settingsFileTimeStamp;
	
	private static DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
	
	public RaspberryScheduler() {

		boolean errorFound = false;
		
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
			
		    String line = br.readLine();
		    while (line != null) {
		    	
		    	//TODO read schedule
		    	
		        line = br.readLine();
		    }
		    
		} catch (Exception e) {
			printMessage("Could not open settings file(" + RaspberrySchedulerSettings.getSettingsFileName() + ").");
			errorFound = true;
		} finally {
			if(br != null)
			{
				try {
					br.close();
				} catch (Exception e2) {
					errorFound = true;
					printMessage("Could not close settings file(" + RaspberrySchedulerSettings.getSettingsFileName() + ").");
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
		}
	}
	
	private boolean createFiles()
	{
		settingsFile = new File(RaspberrySchedulerSettings.getSettingsFileName());

		if(!settingsFile.exists())
		{
			printMessage("Could not find settings file(" + RaspberrySchedulerSettings.getSettingsFileName() + ").");
			return false;
		}
		
		return true;
	}
	
	private void printMessage(String message)
	{
		Calendar cal = Calendar.getInstance();
		String dateAndTime = dateFormat.format(cal.getTime());

		message = "["+dateAndTime+"] " + message;
		
		System.out.println(message);
		
		if(RaspberrySchedulerSettings.isPrintToLog())
		{
			appendToLog(message);
		}
	}
	
	private void appendToLog(String message)
	{
		try {
		    Files.write(Paths.get(RaspberrySchedulerSettings.getLogFileName()), message.getBytes(), StandardOpenOption.APPEND);
		}catch (IOException e) {
		}
	}
	
}
