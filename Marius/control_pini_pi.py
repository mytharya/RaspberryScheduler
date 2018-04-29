import time
from datetime import datetime
import json

pin_settings = None
currentPinStatus = {}

#global functions
def setPinUP(pin_id):
    global currentPinStatus
    print(str(pin_id) + " is UP")
    currentPinStatus[pin_id] = True

def setPinDown(pin_id):
    global currentPinStatus
    print(str(pin_id) + " is DOWN")
    currentPinStatus[pin_id] = False

def getPinStatus(pin_id)
    global currentPinStatus
    
    return currentPinStatus

def readDataFromfile():
    global pin_settings

    with open('pinSettings.txt') as json_file:  
        pin_settings = json.load(json_file)
        '''
        pin = '0'
        for times in pin_settings[pin]:
            print('StartTime: ' + times['StartTime'])
            print('StopTime: ' + times['StopTime'])
            print('')
        '''
def saveDataToFile():
    with open('pinSettingsX.txt', 'w') as json_file:
        json.dump(pin_settings, json_file, indent=4)

#converts string time into integer minutes
def ConvertStringTimeToMinutes(timeInString):
        timeInStringArray = timeInString.split(":")
        timeInMin = int(timeInStringArray[0]) * 60 + int(timeInStringArray[1])
        return timeInMin

#start main program
print("\n"*20)

count = 0

readDataFromfile()

print("\n" + str(datetime.now().strftime("%H:%M")))
        
#setPinUP(count)
#time.sleep(1)
#setPinDown(count)

now = datetime.now().time()
nowInMinutes = now.hour * 60 + now.minute

for key in pin_settings.keys():
    print("\nWorking with pin no: " + key)

    isSetPinUp = False

    for orar in pin_settings[key]:
        
        timeStartMin = ConvertStringTimeToMinutes(orar["StartTime"])
        timeStopMin = ConvertStringTimeToMinutes(orar["StopTime"])

        if((timeStartMin <= nowInMinutes) and (nowInMinutes < timeStopMin)):
            isSetPinUp = True
            break

    if(isSetPinUp == True):
        if setPinUP = False:
            setPinUP(key)
    else:
        setPinDown(key)