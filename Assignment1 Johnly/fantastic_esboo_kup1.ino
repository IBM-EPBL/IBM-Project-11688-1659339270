// C++ code
//
int count =0;

void setup()
{
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  Serial.begin(9600);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(9,OUTPUT);
}

void loop()
{
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  
  if(sensorValue <=750)
  {
    digitalWrite(12,HIGH);
    if(count == 0) //after the light become dim the buzzer will go off 1 time
    {
      tone(11,1000);
      delay(1000);
      count = 1;
    }
    noTone(11);
  }
  else
  {
    digitalWrite(12,LOW);
  }
  
  
  int Temp = analogRead(A1);  
  float volts = (Temp / 965.0) * 5;  
  float celcius = (volts - 0.5) * 100; 
  Serial.println(celcius);
  
  if(celcius > 32.0)  //if temp is greater than 32 degree celcius fan will start to run in this case a DC Motor
  {
    digitalWrite(9,HIGH);
  }
  else
  {
   digitalWrite(9,LOW); 
  }
  
  if(celcius > 60.0)
  {
    tone(11,2000);
  }
  else
  {
    noTone(11);
  }
}