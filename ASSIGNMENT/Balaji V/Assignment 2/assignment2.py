import random
temperature = random.random()*10
humidity = random.random()*10
while(temperature<9):
    print("Low Temperature: "+str(temperature) + " Humidity: "+str(humidity))
    temperature = random.random()*10
print("High Temperature alarm trigered: "+str(temperature))