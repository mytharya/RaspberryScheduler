package raspberryScheduler;

public class RaspberrySchedulerSettings {

	private final static boolean debug = true;
	private final static boolean printToLog = true;
	
	private final static String SETTINGS_FILE_NAME = "RaspberryScheduler.ini";
	private final static String LOG_FILE_NAME = "RaspberrySchedulerLog.ini";
	
	public static boolean isDebug()
	{
		return debug;
	}
	
	public static String getSettingsFileName()
	{
		return SETTINGS_FILE_NAME;
	}
	
	public static String getLogFileName()
	{
		return LOG_FILE_NAME;
	}
	
	public static boolean isPrintToLog()
	{
		return printToLog;
	}
}
