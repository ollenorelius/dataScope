

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(500);
  initMessage();
}

void loop() {
  // put your main code here, to run repeatedly:
  long t = millis();
  Serial.print("D");
  Serial.print(" ");
  Serial.print(t);
  Serial.print(" ");
  Serial.print(sin(t/1000.0));
  Serial.print(" ");
  Serial.print(cos(t/1000.0));
  Serial.print(" ");
  Serial.print(analogRead(0)/1024.0);
  Serial.println();
  delay(10);
}

void initMessage()
{
  //!, number of channels, name1, name2, ...
  Serial.println("N sin(t) cos(t) analogRead");
  // y limits
  Serial.println("L -1.0 1.0");
  Serial.println("!");
}


