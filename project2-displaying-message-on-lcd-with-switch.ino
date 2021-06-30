#include<LiquidCrystal.h>
const int rs=2,en=3,d4=4,d5=5,d6=6,d7=7;
int logicstate = 8;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);
void setup() {
  lcd.begin(16,2);
  pinMode(logicstate,INPUT);
  lcd.print("GOOD");
  // put your setup code here, to run once:

}

void loop() {
  int data = digitalRead(logicstate);
  if(data==0)
  {
    lcd.setCursor(0,1);
    lcd.print("MORNING");
  }
  if(data==1)
  {
    
    lcd.setCursor(0,1);
    
    lcd.print("NIGHT");
  }  }
  
