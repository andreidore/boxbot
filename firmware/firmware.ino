
int const BUZZER = 4;

//  Motor A

int const ENA = 10;

int const INA = 12;

//  Motor B

int const ENB = 11;

int const INB = 13;


int const MIN_SPEED = 27;   // Set to minimum PWM value that will make motors turn

int const ACCEL_DELAY = 50; // delay between steps when ramping motor speed up or down.



void setup() {

  pinMode(LED_BUILTIN, OUTPUT);


  pinMode(ENA, OUTPUT);  // set all the motor control pins to outputs

  pinMode(ENB, OUTPUT);

  pinMode(INA, OUTPUT);

  pinMode(INB, OUTPUT);

  pinMode(BUZZER, OUTPUT);

  Serial.begin(9600);  // Set comm speed for serial monitor messages

  delay(5000);
}

void loop() {
  
    Motor('C', 'F', 2);   

  delay(3000);

  

  // Run both motors in Reverse at 75% power but sound beeper first

  Motor('C', 'F', 0);  // Stop motors

  delay(1000);

  digitalWrite(BUZZER,HIGH);delay(500);digitalWrite(BUZZER,LOW); 

  delay(500);

  digitalWrite(BUZZER,HIGH);delay(500);digitalWrite(BUZZER,LOW); 

  delay(1000);

  Motor('C', 'R', 2);  // Run motors forward at 75%

 delay(3000); 

  

  // now run motors in opposite directions at same time at 50% speed

  Motor('A', 'F', 2);

  Motor ('B', 'R', 2);

  delay(3000);

  

  // now turn off both motors

  Motor('C', 'F', 0);  

  delay(3000);


}



void Motor(char mot, char dir, int speed)

{

  // remap the speed from range 0-100 to 0-255

  int newspeed;

  if (speed == 0)

    newspeed = 0;  // Don't remap zero, but remap everything else.

  else

    newspeed = map(speed, 1, 100, MIN_SPEED, 255);



  switch (mot) {

    case 'A':  // Controlling Motor A

      if (dir == 'F') {

        digitalWrite(INA, HIGH);

      }

      else if (dir == 'R') {

        digitalWrite(INB, LOW);
      }

      analogWrite(ENA, newspeed);

      break;



    case 'B':  // Controlling Motor B

      if (dir == 'F') {

        digitalWrite(INB, HIGH);

      }

      else if (dir == 'R') {

        digitalWrite(INB, LOW);
      }

      analogWrite(ENB, newspeed);

      break;



    case 'C':  // Controlling Both Motors

      if (dir == 'F') {

        digitalWrite(INA, HIGH);

        digitalWrite(INB, HIGH);

      }

      else if (dir == 'R') {

        digitalWrite(INA, LOW);

        digitalWrite(INB, LOW);
      }

      analogWrite(ENA, newspeed);

      analogWrite(ENB, newspeed);

      break;
  }

  // Send what we are doing with the motors out to the Serial Monitor.



  Serial.print("Motor: ");

  if (mot == 'C')

    Serial.print("Both");

  else

    Serial.print(mot);

  Serial.print("t Direction: ");

  Serial.print(dir);

  Serial.print("t Speed: ");

  Serial.print(speed);

  Serial.print("t Mapped Speed: ");

  Serial.println(newspeed);
}
