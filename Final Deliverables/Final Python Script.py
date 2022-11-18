import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#IBM WATSON Credentials
organization = "0mfbus"
deviceType = "ECU"
deviceId = "12345"
authMethord ="token"
authToken = "12345678"


def myCommandCallback(cmd):
    print("Command Received: %s" % cmd.data['command'])
    status = cmd.data['command']
    if status == "lighton":
        print("Led is on")
    elif status == "lightoff":
        print("Led is off")
    else:
        print("Proper command required")
        
try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method":authMethord,"auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("caught exception connecting device: %s" % str(e))
    sys.exit()
    
deviceCli.connect()


while True:
    
    turbidity = random.randint(1, 1000)
    temp=random.randint(-20,125)
    pH=random.randint(0,14)
    myData={'tur':turbidity,'temperature':temp, 'ph':pH}

        
    def myOnPublishCallback():
        print("Published pH= %s" % pH, "Turbidity:%s" % turbidity, "Temperature:%s" %temp)
    
    success = deviceCli.publishEvent("demo", "json", myData, qos=0,on_publish=myOnPublishCallback)
    
    if not success:
        print("Not Connected to ibmiot")
    time.sleep(5)
    
    deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
