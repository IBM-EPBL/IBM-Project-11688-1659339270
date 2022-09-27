//"https://www.tinkercad.com/things/eNBsdUr5O1O-smarthome-ibm-project/editel"
int lightIntensity;
#define lLED 7
#define mLED 9
#define pir 8
bool state = false;

 void setup()
{
  Serial.begin(9600);
  pinMode(A0,INPUT);
  pinMode(lLED,OUTPUT);
  pinMode(mLED,OUTPUT);
  pinMode(pir,INPUT);
  
}

void lightsensing(){
  lightIntensity = analogRead(A0);
  Serial.print("Intensity Of Light : ");
  Serial.println(lightIntensity);
  if(lightIntensity <800){
  digitalWrite(lLED,HIGH);
  }else{
  digitalWrite(lLED,LOW);
  }
}

void motionSensing(){
  int val = digitalRead(pir);
  if(val==HIGH){
    digitalWrite(mLED,HIGH);
    Serial.println("Motion Detected");
  }else{
  	digitalWrite(mLED,LOW);
  }
}

void loop()
{
  lightsensing();
  motionSensing();
  delay(500);
  
}