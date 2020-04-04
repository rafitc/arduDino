
// Arduino Dino Game ! :)

int sensorPin = A0;    //Connect LDR on A0 
int sensorValue = 0;  // variable to store the value coming from LDR
int thresholdValue = 45; //this one depend on your trial and error method. 
void setup() {
  Serial.begin(9600);  //Serial begin on 9600
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin); //read sensor data 
  //Serial.println(sensorValue);  //uncomment this while first use and take your thresholdValue and set. 
  
  if(sensorValue <= thresholdValue){   //if condition to detect obstacle.
    Serial.println(1);                 //Serial printing if condition is true. 
  }
  delay(40);                         //delay 50ms
}
