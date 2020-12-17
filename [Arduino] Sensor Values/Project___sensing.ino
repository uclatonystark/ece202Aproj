#define thumb  A7
#define index  A6
#define middle  A5
#define ring  A4
#define pinky  A3

#include <Arduino_LSM9DS1.h>
float ax, ay, az, gx, gy, gz, mx, my, mz;

void setup() {
  Serial.begin(9600);
  pinMode(thumb,INPUT);
  pinMode(index,INPUT);
  pinMode(middle,INPUT);
  pinMode(ring,INPUT);
  pinMode(pinky,INPUT);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

float f1,f2,f3,f4,f5;
void loop() {
  f1 = analogRead(thumb);
  f2 = analogRead(index);
  f3 = analogRead(middle);
  f4 = analogRead(ring);
  f5 = analogRead(pinky);
  if(f1<850) f1=1; else f1=0;
  if(f2<880) f2=1; else f2=0;
  if(f3<880) f3=1; else f3=0;
  if(f4<880) f4=1; else f4=0;
  if(f5<850) f5=1; else f5=0;
  
  IMU.readAcceleration(ax, ay, az); 
  IMU.readGyroscope(gx, gy, gz); 
  IMU.readMagneticField(mx, my, mz); 
  
  Serial.print(f1);
  Serial.print('\t');
  Serial.print(f2);
  Serial.print('\t');
  Serial.print(f3);
  Serial.print('\t');
  Serial.print(f4);
  Serial.print('\t');
  Serial.print(f5);
  Serial.print('\t');
  Serial.print(ax);
  Serial.print('\t');
  Serial.print(ay);
  Serial.print('\t');
  Serial.print(az);
  Serial.print('\t');
  Serial.print(gx);
  Serial.print('\t');
  Serial.print(gy);
  Serial.print('\t');
  Serial.print(gz);
  Serial.print('\t');
  Serial.print(mx);
  Serial.print('\t');
  Serial.print(my);
  Serial.print('\t');
  Serial.println(mz);
  
  delay(100);
}
