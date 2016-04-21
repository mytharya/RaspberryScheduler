package raspberryScheduler;

import java.util.Calendar;

public class RaspberrySchedule {

	private int startHour;
	private int startMinute;
	
	private int endHour;
	private int endMinute;
	
	public RaspberrySchedule(int startHour, int startMinute, int endHour, int endMinute) {

		this.startHour = startHour;
		this.startMinute = startMinute;
		this.endHour = endHour;
		this.endMinute = endMinute;
	}
	
	public boolean isActive(Calendar cal)
	{
		int hour = cal.get(Calendar.HOUR_OF_DAY);
		int minute = cal.get(Calendar.MINUTE);
		
		if((this.startHour <= hour && this.startMinute <= minute) && (hour <= this.endHour && minute < this.endMinute))
		{
			return true;
		}
		
		return false;
	}
	
	public int getStartHour()
	{
		return this.startHour;
	}
	
	public int getStartMinute()
	{
		return this.startMinute;
	}
	
	public int getEndHour()
	{
		return this.endHour;
	}
	
	public int getEndMinute()
	{
		return this.endMinute;
	}
}
