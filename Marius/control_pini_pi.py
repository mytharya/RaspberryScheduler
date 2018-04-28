import time
from datetime import datetime
import json

pin_settings = None

#global functions
def setPinUP(pin_id):
    print(str(pin_id) + " is UP")

def setPinDown(pin_id):
    print(str(pin_id) + " is DOWN")

def readDataFromfile():
    with open('pinSettings.txt') as json_file:  
        pin_settings = json.load(json_file)
        print(type(pin_settings))
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
'''
functie care printeaza timpi pinilor start/stop
compare date-time
'''
'''
#create pin initial data
pin_settings = {}  
pin_settings['0'] = []  
pin_settings['0'].append({  
    'StartTime': '16:20',
    'StopTime': '16:30'
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

with open('pinSettings.txt', 'w') as outfile:  
    json.dump(pin_settings, outfile, indent=4)
'''
#start main program
print("\n"*20)

count = 0

readDataFromfile()

while True:
    print("\n" + str(datetime.now().time()))
    
    """
    Pin_Id
    [Timp_start, Timp_stop]
    """
    setPinUP(count)
    time.sleep(1)
    setPinDown(count)
    #pin_settings[count].append({'StartTime : {}'.format(str(datetime.now().time()),)})
    #pin_settings[count].append('is it working?')
    #print(pin_setting)
    print(type(pin_settings))

    #exit condition
    if count == 2:
        print("\nAm ajuns la:", count)
        #print(pin_settings(count))
        #print(pin_settings())

        #saveDataToFile()
        break
    else:
        count = count + 1