
#include <Wire.h>
#include "MAX30105.h"
#include<LiquidCrystal.h>
#include "heartRate.h"

MAX30105 particleSensor;
LiquidCrystal lcd(8,9,10,11,12,13);

const byte RATE_SIZE = 4; //Increase this for more averaging. 4 is good.
byte rates[RATE_SIZE]; //Array of heart rates
byte rateSpot = 0;
long lastBeat = 0; //Time at which the last beat occurred

const unsigned long eventInterval= 1000;
unsigned long prevTime = 0;

float beatsPerMinute;
int beatAvg;

byte degree[8] =
{
0b00011,
0b00011,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000
};

void setup()
{
  Serial.begin(9600);
  pinMode(7, INPUT); // Setup for leads off detection LO +
  pinMode(6, INPUT); // Setup for leads off detection LO -
  lcd.begin(16,2);
  lcd.createChar(1, degree);
  lcd.setCursor(0,0);
  lcd.print("Healthcare");
  lcd.setCursor(0,1);
  lcd.print(" Monitoring");
  delay(1000);
  lcd.clear();
  
  Serial.println("Initializing...");

  // Initialize sensor
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
  {
    Serial.println("MAX30105 was not found. Please check wiring/power. ");
    while (1);
  }
  //Serial.println("Place your index finger on the sensor with steady pressure.");

  particleSensor.setup(); //Configure sensor with default settings
  particleSensor.setPulseAmplitudeRed(0x0A); //Turn Red LED to low to indicate sensor is running
  particleSensor.setPulseAmplitudeGreen(0); //Turn off Green LED
  particleSensor.enableDIETEMPRDY(); //Enable the temp ready interrupt. This is required.
  
  
}

void loop()
{
  long irValue = particleSensor.getIR();
  float temperature = particleSensor.readTemperature();
  int ECG = analogRead(0);

  if (checkForBeat(irValue) == true)
  {
    //We sensed a beat!
    long delta = millis() - lastBeat;
    lastBeat = millis();

    beatsPerMinute = 60 / (delta / 1000.0);

    if (beatsPerMinute < 255 && beatsPerMinute > 20)
    {
      rates[rateSpot++] = (byte)beatsPerMinute; //Store this reading in the array
      rateSpot %= RATE_SIZE; //Wrap variable

      //Take average of readings
      beatAvg = 0;
      for (byte x = 0 ; x < RATE_SIZE ; x++)
        beatAvg += rates[x];
      beatAvg /= RATE_SIZE;
    }
  }

  //Code for AD8232
  if((digitalRead(7) == 1)||(digitalRead(6) == 1)){
  Serial.println('!');
  }
  else{
  // send the value of analog input 0:
  Serial.println(analogRead(A0));
  }
  //Wait for a bit to keep serial data from saturating
  delay(1);
  
  Serial.print("IR=");
  Serial.print(irValue);
  Serial.print(", BPM=");
  Serial.println(beatsPerMinute);
  Serial.print(", TemperatureC=");
  Serial.println(temperature, 2);
  
  /*------Display Result------*/
  unsigned long currentTime1 = millis();
  
  if (currentTime1 - prevTime >= eventInterval){
  
    lcd.clear();
    lcd.print("Temp=    BPM= ");
    lcd.setCursor(0,1);
    lcd.print(temperature, 2); 
    lcd.write(1);
    lcd.print("C");
    lcd.setCursor(9,1);
    lcd.print(beatsPerMinute);
    
    prevTime += eventInterval;
  }
  
}
