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




//Project: Simulador de Sinal de Transito (Sem delay)
//Created by: Alexsandro Monteiro
//Date: 15/12/2021


int green_A = 13;
int yellow_A = 10;
int red_A = 7;

int green_B = 5;
int yellow_B = 4;
int red_B = 3;

byte sinal;

void setup()
{
  pinMode(green_A, OUTPUT);
  pinMode(yellow_A, OUTPUT);
  pinMode(red_A, OUTPUT);
  pinMode(green_B, OUTPUT);
  pinMode(yellow_B, OUTPUT);
  pinMode(red_B, OUTPUT);
  Serial.begin(9600);
}

void loop(){
	digitalWrite(green_A, HIGH);
    digitalWrite(red_B, HIGH);
  	digitalWrite(red_A, LOW);
  	digitalWrite(yellow_B, LOW);

  //for (int x=0; x<10; x++){
    for (int y=0; y<900; y++){
      //digitalWrite(pin[y], matriz[x][y]);
      //delay(1);
      Serial.println(" ");
      Serial.println(y);
      if (y > 400){
        digitalWrite(yellow_A, HIGH);
        digitalWrite(green_A, LOW);
      }
      if(y > 480){
        digitalWrite(red_A, HIGH);
        digitalWrite(yellow_A, LOW);
        digitalWrite(red_B, LOW);
        digitalWrite(green_B, HIGH);
      }
      if(y > 840){
        digitalWrite(yellow_B, HIGH);
        digitalWrite(green_B, LOW);
      }

}

