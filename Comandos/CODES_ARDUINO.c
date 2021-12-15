#include <LiquidCrystal.h>

LiquidCrystal lcd (12, 11, 5, 4, 3, 2);
int ligatela = 8;

void setup() {
  
  pinMode(ligatela, OUTPUT);
  lcd.begin(16, 2);
  Serial.begin(9600);
 
}

void loop() {
  
digitalWrite(ligatela, HIGH);
  
for (int min=0; min<60; min++){
      for (int seg=0; seg<60; seg++){
           for (int msg=0; msg<60; msg++){
             	
                if(msg > 59) {
                  seg++;
                  msg=60;
                }
                if(seg > 59) {
                  min++; 
                  seg=60;
                }
                if(min > 59) {
                  min=60;
                }
                
             	// ---------------------------
             	if(seg%2== 0) {
                  digitalWrite(ligatela, HIGH);                
                }
             	else{
                	digitalWrite(ligatela, LOW); 
                }
				// ----------------------------
             	//LCD Display
                lcd.setCursor(0, 0);
                lcd.print("  AULA ARDUINO");
                lcd.setCursor(0, 1);
                lcd.print("     ");
                lcd.print(min);
             	lcd.print(":");
                lcd.print(seg);
                lcd.print(":");
                lcd.print(msg);
             	
             	//Serial Door
             	Serial.print(min);
                Serial.print(":");
                Serial.print(seg);
                Serial.print(":");
                Serial.print(msg);
                Serial.println();

                      }
                   }
                }	
 		 	 }
