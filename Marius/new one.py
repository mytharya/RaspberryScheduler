import json

#create pin initial data
pin_settings = {}  
pin_settings['0'] = []  
pin_settings['0'].append({  
    'StartTime': '16:20',
    'StopTime': '16:30'
})
pin_settings['0'].append({  
    'StartTime': '15:00',
    'StopTime': '16:00'
})
pin_settings['0'].append({  
    'StartTime': '20:00',
    'StopTime': '21:00'
})
pin_settings['1'] = []  
pin_settings['1'].append({  
    'StartTime': '16:40',
    'StopTime': '16:50'
})
pin_settings['2'] = []  
pin_settings['2'].append({  
    'StartTime': '15:20',
    'StopTime': '16:30'
})

print("\n"*20)

now = '16:25'
print(now)

def ConvertStringTimeToMinutes(timeInString):
        timeInStringArray = timeInString.split(":")
        timeInMin = int(timeInStringArray[0]) * 60 + int(timeInStringArray[1])
        return timeInMin

for key in pin_settings.keys():
    print("Working with PIN: " + key)

    #use a variable to store if there is at least one active interval
    setPinToUp = False

    #searching in each interval defined for the PIN
    #if we find at least one interval which is active(starttime <= now < stoptime)
    #set the intermediate varible to true
    for orar in pin_settings[key]:
        print(orar)
        #if the now is between start and stop, set the variable to true and exit the loop 
        #because we found at least one interval which is active
        if((ConvertStringTimeToMinutes(orar["StartTime"]) <= ConvertStringTimeToMinutes(now)) and (ConvertStringTimeToMinutes(now) < ConvertStringTimeToMinutes(orar["StopTime"]))):
            setPinToUp = True
            break
    
    #check now if the variable was set to True
    if(setPinToUp == True):
        #set pin up
        print("Pin " + key + " set to ACTIVE")
    else:
        #set pin down
        print("Pin " + key + " set to DISABLED")

