package raspberryScheduler;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.HashMap;
import java.util.List;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class RaspberryGPIO {

	private HashMap<Integer, List<RaspberrySchedule>> DayToScheduleMap = new HashMap<>();

	private final GpioPinDigitalOutput pin;
	private final Integer pinId;
	
	private boolean debugLevel = false;
	
	public RaspberryGPIO(int pinId, GpioController controller)
	{
		this.pinId = pinId;
		
		String pinIdString = String.valueOf(pinId);

		pinIdString  = "GPIO " + pinIdString;
		
		if(RaspberrySchedulerSettings.DEBUG == false)
		{
			pin = controller.provisionDigitalOutputPin(RaspiPin.getPinByName(pinIdString), "MyLED " + pinIdString, PinState.LOW);
	        pin.setShutdownOptions(true, PinState.LOW);
		}
		else
		{
			debugLevel = false;
			pin = null;
		}
	}
	
	public void setSchedule(HashMap<Integer, List<RaspberrySchedule>> map)
	{
		DayToScheduleMap = new HashMap<>(map);
	}
	
	public boolean addDaySchedule(int day, List<RaspberrySchedule> ScheduleList)
	{
		if(DayToScheduleMap.get(day) == null)
		{
			DayToScheduleMap.put(day, ScheduleList);
			
			return true;
		}
		
		return false;
	}
	
	public void checkSchedule()
	{
		Calendar cal = Calendar.getInstance();
		cal.setTime(cal.getTime());
		Integer day = cal.get(Calendar.DAY_OF_WEEK);

		List<RaspberrySchedule> ScheduleList = DayToScheduleMap.get(day);
		if(ScheduleList != null)
		{
			boolean isHigh = checkPinStatus();
			boolean isScheduleHigh = false;
			
			for (RaspberrySchedule raspberrySchedule : ScheduleList) 
			{
				if(raspberrySchedule.isActive(cal))
				{
					isScheduleHigh = true;
					break;
				}
			}
			
			if(isHigh != isScheduleHigh)
			{
				setPin(isScheduleHigh);
			}
		}
	}
	
	private void setPin(boolean isHigh)
	{
		if(RaspberrySchedulerSettings.DEBUG == false)
		{
			Calendar cal = Calendar.getInstance();
			SimpleDateFormat sdf = new SimpleDateFormat("dd-M-yyyy hh:mm:ss");
			
			System.out.println("["+sdf.format(cal.getTime())+"] Pin: " + pinId + "[" + ((isHigh)?"ENABLED":"DISABLED") +"]");
			
			pin.setState(isHigh);;
		}
		else
		{
			Calendar cal = Calendar.getInstance();
			SimpleDateFormat sdf = new SimpleDateFormat("dd-M-yyyy hh:mm:ss");
			
			System.out.println("["+sdf.format(cal.getTime())+"] Pin: " + pinId + "[" + ((isHigh)?"ENABLED":"DISABLED") +"]");
			debugLevel = isHigh;
		}
	}
	
	private boolean checkPinStatus()
	{
		if(RaspberrySchedulerSettings.DEBUG == false)
		{
			return pin.isHigh();
		}
		else
		{
			return debugLevel;
		}
	}
	
	public void unInitPin(GpioController controller)
	{
		if(RaspberrySchedulerSettings.DEBUG == false)
		{
			pin.low();
			controller.unprovisionPin(this.pin);
		}
		else
		{
			Calendar cal = Calendar.getInstance();
			SimpleDateFormat sdf = new SimpleDateFormat("dd-M-yyyy hh:mm:ss");
			
			System.out.println("["+sdf.format(cal.getTime())+"] Pin: " + pinId + "[DISABLED]");
		}
	}
	
	public void printSchedules()
	{
		for (Integer val : DayToScheduleMap.keySet()) {
			
			System.out.println("\n["+ RaspberrySchedulerSettings.DAYS_OF_WEEK.get(val) +"]");
			
			List<RaspberrySchedule> ScheduleList = DayToScheduleMap.get(val);

			int itemsPerLine = 10;
			
			for (RaspberrySchedule raspberrySchedule : ScheduleList) {
				System.out.print("["+(raspberrySchedule.getStartHour()*100 + raspberrySchedule.getStartMinute()) + "-" + (raspberrySchedule.getEndHour()*100 + raspberrySchedule.getEndMinute()) + "]");
				itemsPerLine--;
				
				if(itemsPerLine == 0)
				{
					itemsPerLine = 10;
					System.out.println();
				}
			}
		}
	}
}
