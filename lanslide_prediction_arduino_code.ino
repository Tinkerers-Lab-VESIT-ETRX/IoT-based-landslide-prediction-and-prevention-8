#include<LiquidCrystal.h>
#include<DHT.h>
LiquidCrystal lcd(2,3,4,5,6,7);
int SensorPin=A0;
#define dht_1 A1
#define DHTTYPE DHT11
DHT dht(dht_1,DHTTYPE);


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second: 
  lcd.begin(16,2);
  lcd.print("------------Welcome to----------");
  lcd.setCursor(0,1);
  lcd.print("  *Landslide Prevention system* ");
  Serial.begin(9600);
  dht.begin();
}

// the loop routine runs over and over again forever:
void loop() {
  for(int PositionCount=0;PositionCount<13; PositionCount++)//loop for scrolling the LCD text
  {
    lcd.scrollDisplayLeft();//builtin command to scroll left the text
    delay(150);// delay of 150 msec
    }
{
  int SensorValue = analogRead(SensorPin);   
  float SensorVolts = analogRead(SensorPin)*0.0048828125;
  float temp =dht.readTemperature();
  float Humid = dht.readHumidity();
  Serial.print("Moisture = ");Serial.print((int)SensorVolts);Serial.print("v,");
  Serial.print("Temp = ");Serial.print((int)temp);Serial.print("v,");
  Serial.print("Humid = ");Serial.print((int)Humid);
   // Serial.print("    |    ");
  // Serial.print("moisture = "); // Displaying moisture // Serial.print(SensorValue);// Serial.print("v");
  Serial.println();
  delay(1000);
}
}

  
