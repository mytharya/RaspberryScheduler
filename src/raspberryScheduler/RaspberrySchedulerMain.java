package raspberryScheduler;

public class RaspberrySchedulerMain {

	public static void main(String[] args) {

		RaspberryScheduler scheduler  = new RaspberryScheduler();
		
		if(scheduler.isInitialized())
		{
			scheduler.start();
		}
	}
}
