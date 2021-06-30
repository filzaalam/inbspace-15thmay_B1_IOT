#include<LiquidCrystal.h>
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
unsigned long x = 0;
byte sec = 20;
byte minute = 10;
byte hr = 8;
int p2 = 3;
int p3 = 4;
byte hourupg = 8;
byte minupg = 11;
byte secong = 25;
int mode = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode(p2, INPUT_PULLUP);
  pinMode(p3, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
  pinMode(5, OUTPUT);
  lcd.begin(16, 2);
  DisplayTime();
}
//getting error sir
// just make a prototye in such cases
void DisplaySetHour()
{ // this is okay
  lcd.setCursor(0,0);
  lcd.print("Hour Change         ");
  lcd.setCursor(0,1);
  lcd.print(hourupg);
  lcd.print("                   ");
  if (digitalRead(p2) == LOW)
  { while (digitalRead(p2) == LOW);
    if (hourupg == 23)
    {
      hourupg = 0;
    }
    else
    {
      hourupg = hourupg + 1;
    }
  }


  if (digitalRead(p3) == LOW)
  {
    while (digitalRead(p3) == LOW);
    if (hourupg == 0)
    {
      hourupg = 23;
    }
    else
    {
      hourupg = hourupg - 1;
    }
  }
