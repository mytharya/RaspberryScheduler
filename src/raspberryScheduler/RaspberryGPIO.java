package raspberryScheduler;

import java.util.Calendar;
import java.util.HashMap;
import java.util.List;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class RaspberryGPIO {

	HashMap<Integer, List<RaspberrySchedule>> DayToScheduleMap = new HashMap<>();

	final GpioPinDigitalOutput pin;
	
	private boolean debugLevel = false;
	
	public RaspberryGPIO(int pinId, GpioController controller)
	{
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
		int day = cal.get(Calendar.DAY_OF_WEEK);

		List<RaspberrySchedule> ScheduleList = DayToScheduleMap.get(day);
		if(ScheduleList != null)
		{
			for (RaspberrySchedule raspberrySchedule : ScheduleList) {
				
				setPin(raspberrySchedule.isActive(cal));
			}
		}
	}
	
	private void setPin(boolean isHigh)
	{
		if(checkPinStatus() != isHigh)
		{
			if(RaspberrySchedulerSettings.DEBUG == false)
			{
				pin.setState(isHigh);;
			}
			else
			{
				debugLevel = isHigh;
			}
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
}
