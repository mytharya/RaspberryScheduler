import time
from datetime import datetime
import json

#globla functions
def setPinUP(pin_id):
    print(str(pin_id) + " is UP")

def setPinDown(pin_id):
    print(str(pin_id) + " is DOWN")

def readDataFromfile():
    with open('pinSettings.txt') as json_file:  
        pin_settings = json.load(json_file)
        print(pin_settings)
    '''
    for pin in pin_settings:
        print('StartTime: ' + pin['StartTime'])
        print('StopTime: ' + pin['StopTime'])
        print('')
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
while True:
    print(datetime.now().time())
    
    """
    Pin_Id
    [Timp_start, Timp_stop]
    """
    readDataFromfile()
    setPinUP(count)
    time.sleep(1)
    setPinDown(count)

    #exit condition
    if count == 1:
        print("Am ajuns la:", count)
        break
    else:
        count = count + 1