package raspberryScheduler;

public class RaspberryScheduler {

	private boolean isInitialized;
	
	public RaspberryScheduler() {

		
		this.isInitialized = readSettingsFile();
	}
	
	private boolean readSettingsFile()
	{
		return true;
	}
	
	public boolean isInitialized()
	{
		return this.isInitialized;
	}
	
	public void start()
	{
		
	}
}
