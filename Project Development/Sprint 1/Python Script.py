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

account_sid ='ACc252f0d0b6965872c1c06e77dda760d2'
auth_token ='1ff874b334a0949b327b4d1ec14d7a37'
twilio_number ='+15133275826'
target_number ='+919600680245'

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

def SMS():
    message = Client.messages.create(body="ALERT!! THE WATER QUALITY IS DEGRADED",from_=keys.twilio_number,to = keys.target_number)
print(message.body)

while True:
    
    turbidity = random.randint(1, 1000)
    temp=random.randint(-20,125)
    pH=random.randint(0,100)
    myData={'tur':turbidity,'temperature':temp, 'humidity':pH}

    if temperature>70 or pH<6 or turbidity>500:
        SMS()
        
    def myOnPublishCallback():
        print("Published pH= %s" % pH, "Turbidity:%s" % turbidity, "Temperature:%s" %temp)
    
    success = deviceCli.publishEvent("demo", "json", myData, qos=0,on_publish=myOnPublishCallback)
    
    if not success:
        print("Not Connected to ibmiot")
    time.sleep(5)
    
    deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
