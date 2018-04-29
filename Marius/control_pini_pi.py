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
    for orar in pin_settings[key]:
        for t in orar:
            print(t," :", orar[t])
            split = orar[t].split(":")
            then = int(split[0]) * 60 + int(split[1])
            
            if nowInMinutes > then:
                if t == 'StartTime':
                    print("nowInMinutes: ", nowInMinutes, "is > then: ", then)
                    print("Your {}: {} is smaller than {}.".format(t,orar[t],datetime.now().strftime("%H:%M")))
                    setPinUP(key)
                    #print("setPinDown({})".format(key))
                if t == 'StopTime':
                    print("nowInMinutes: ", nowInMinutes, "is > then: ", then)
                    print("Your {}: {} is smaller than {}.".format(t,orar[t],datetime.now().strftime("%H:%M")))
                    setPinDown(key)
                    #print("setPinDown({})".format(key))

            elif nowInMinutes < then:
                if t == 'StartTime':
                    print("nowInMinutes: ", nowInMinutes, "is < then: ", then)
                    print("Your {}: {} is greater than {}.".format(t,orar[t],datetime.now().strftime("%H:%M")))
                    #setPinUP(key)
                    #print("setPinDown({})".format(key))
                if t == 'StopTime':
                    print("nowInMinutes: ", nowInMinutes, "is < then: ", then)
                    print("Your {}: {} is greater than {}.".format(t,orar[t],datetime.now().strftime("%H:%M")))
                    setPinDown(key)
                    #print("setPinDown({})".format(key))

            else:
                print("nowInMinutes: ", nowInMinutes, "is = then: ", then)
                print("Your {}: {} is equal than {}.".format(t,orar[t],datetime.now().strftime("%H:%M")))