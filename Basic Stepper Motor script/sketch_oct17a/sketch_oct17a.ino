/*     Simple Stepper Motor Control Exaple Code

    by Dejan Nedelkovski, www.HowToMechatronics.com

*/
// defines pins numbers
const int stepPin = 13;
const int dirPin = 12;
const int stepPin1 = 11;
const int dirPin1 = 10;
const int stepPin2 = 9;
const int dirPin2 = 8;
const int stepPin3 = 7;
const int dirPin3 = 6;
const int stepPin4 = 5;
const int dirPin4 = 4;
const int stepPin5 = 3;
const int dirPin5 = 2;
const int stepDelay = 700;
const int dirDelay = 500;    

void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  pinMode(stepPin4, OUTPUT);
  pinMode(dirPin4, OUTPUT);
  pinMode(stepPin5, OUTPUT);
  pinMode(dirPin5, OUTPUT);
}
void loop() {
  digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
//  digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
//  digitalWrite(dirPin2, HIGH); // Enables the motor to move in a particular direction
//  digitalWrite(dirPin3, HIGH); // Enables the motor to move in a particular direction
//  digitalWrite(dirPin4, HIGH); // Enables the motor to move in a particular direction
//  digitalWrite(dirPin5, HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for (int x = 0; x < 50; x++) {
    digitalWrite(stepPin, HIGH);
//    digitalWrite(stepPin1, HIGH);
//    digitalWrite(stepPin2, HIGH);
//    digitalWrite(stepPin3, HIGH);
//    digitalWrite(stepPin4, HIGH);
//    digitalWrite(stepPin5, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(stepPin, LOW);
//    digitalWrite(stepPin1, LOW);
//    digitalWrite(stepPin2, LOW);
//    digitalWrite(stepPin3, LOW);
//    digitalWrite(stepPin4, LOW);
//    digitalWrite(stepPin5, LOW);
    delayMicroseconds(stepDelay);
  }
  delay(dirDelay); // One second delay

  digitalWrite(dirPin, LOW); //Changes the rotations direction
//  digitalWrite(dirPin1, LOW); //Changes the rotations direction
//  digitalWrite(dirPin2, LOW); //Changes the rotations direction
//  digitalWrite(dirPin3, LOW); //Changes the rotations direction
//  digitalWrite(dirPin4, LOW); //Changes the rotations direction
//  digitalWrite(dirPin5, LOW); //Changes the rotations direction
  // Makes 400 pulses for making two full cycle rotation
  for (int x = 0; x < 50; x++) {
    digitalWrite(stepPin, HIGH);
//    digitalWrite(stepPin1, HIGH);
//    digitalWrite(stepPin2, HIGH);
//    digitalWrite(stepPin3, HIGH);
//    digitalWrite(stepPin4, HIGH);
//    digitalWrite(stepPin5, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(stepPin, LOW);
//    digitalWrite(stepPin1, LOW);
//    digitalWrite(stepPin2, LOW);
//    digitalWrite(stepPin3, LOW);
//    digitalWrite(stepPin4, LOW);
//    digitalWrite(stepPin5, LOW);
    delayMicroseconds(stepDelay);
  }
  delay(dirDelay);
}


