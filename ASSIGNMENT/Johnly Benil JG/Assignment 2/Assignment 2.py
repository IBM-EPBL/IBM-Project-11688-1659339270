import random

temperature = round(random.random() * 50,2)
humidity = round(random.random() * 100,2)

if temperature >= 35:
    print("The temperature is: " + str(temperature))
    print("The humidity in air is " + str(humidity) +"%")
    print("It is hot ALARM!")
elif temperature >20 and temperature < 35:
    if temperature >= 30 and humidity >50:
        print("The temperature is: " + str(temperature))
        print("The humidity in air is " + str(humidity) +"%")
        print("It feels hot because of humidity ALARM!")
    elif temperature >= 25 and humidity >80:
        print("The temperature is: " + str(temperature))
        print("The humidity in air is " + str(humidity) +"%")
        print("It feels hot because of humidity ALARM!")
    else:
        print("The temperature is: " + str(temperature))
        print("The humidity in air is " + str(humidity) +"%")
        print("The weather is great today!")
else:
    print("The temperature is: " + str(temperature))
    print("The humidity in air is " + str(humidity) +"%")
    print("It is cold outside ALARM!")