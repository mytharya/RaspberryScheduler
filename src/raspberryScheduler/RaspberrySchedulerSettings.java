package raspberryScheduler;

public class RaspberrySchedulerSettings {

	private final static boolean debug = true;
	
	private final static String SETTINGS = "RaspberryScheduler.ini";
	private final static String LOG = "RaspberrySchedulerLog.ini";
	
	public static boolean isDebug()
	{
		return debug;
	}
}
