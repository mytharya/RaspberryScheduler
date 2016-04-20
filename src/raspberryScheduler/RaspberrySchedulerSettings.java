package raspberryScheduler;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.List;

public class RaspberrySchedulerSettings {

	final static boolean DEBUG = true;
	final static boolean PRINT_TO_LOG = true;
	
	public final static String SETTINGS_FILE_NAME = "RaspberryScheduler.ini";
	public final static String LOG_FILE_NAME = "RaspberrySchedulerLog.ini";
	public static DateFormat DATE_FORMAT = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
	public static List<String> DAYS_OF_WEEK = Arrays.asList("not_used", "su", "mo", "tu", "we", "th", "fr", "sa");
	
}
