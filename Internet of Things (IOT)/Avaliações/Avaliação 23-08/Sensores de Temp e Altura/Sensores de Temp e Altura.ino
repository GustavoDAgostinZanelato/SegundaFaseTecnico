//Declarando Variáveis do Sensor de Temperatura
int ThermistorPin = 0;
int Vo;
float R1 = 10000;
float logR2, R2, T, Tc, Tf;
float c1 = 2.108508173e-3, c2 = 0.7979204727e-4, c3 = 6.535076315e-7;

//Declarando Variáveis do Sensor de Altura
#include <Ultrasonic.h>

Ultrasonic ultrasonic1(12, 13);	// An ultrasonic sensor HC-04
Ultrasonic ultrasonic2(10);		// An ultrasonic sensor PING)))
Ultrasonic ultrasonic3(8);		// An Seeed Studio ultrasonic sensor

//Declarando Leds e Variáveis Auxiliáres
int led_temperatura = 7;
int led_nivellogico = 6;
int led_alarme1 = 3;
int led_alarme2 = 2;
int aux_nivellogico = 0;

//Indicando os leds como variáveis de Saída
void setup() {
Serial.begin(9600);
pinMode(led_temperatura, OUTPUT);
pinMode(led_nivellogico, OUTPUT);
pinMode(led_alarme1, OUTPUT);
pinMode(led_alarme2, OUTPUT);
}

void loop() {

//Biblioteca do sensor de Temperatura
  Vo = analogRead(ThermistorPin);
  Serial.print(Vo);
  Serial.print("-");
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  Serial.print(R2);
  Serial.print("-");
  logR2 = log(R2);
  Serial.print(logR2);
  Serial.print("-");
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0; 
  Serial.print("Temperature: "); 
  Serial.print(Tc);
  Serial.println(" C");   
  delay(500);


//Biblioteca do sensor de Altura
Serial.print("Sensor 01: ");
Serial.print(ultrasonic1.read()); // Prints the distance on the default unit (centimeters)
Serial.println("cm");
delay(1000);


//Sistema de Acionamento do Aquecedor e Verificaçao do Nivel Lógico igual a 1
if (((Tc >= 25) && (Tc <= 27) && ("ultrasonic1" > 40))){
  digitalWrite(led_nivellogico, HIGH);
  aux_nivellogico++;
}else{
  digitalWrite(led_nivellogico, LOW);
}
  if((nivel_logico == 1) && ("ultrasonic1" > 10)) {
    digitalWrite(led_temperatura, HIGH);
  }else{
    digitalWrite(led_temperatura, LOW);
  }


//Sistema de Acionamento dos Alarmes
  if("ultrasonic1" < 20){
    digitalWrite(led_alarme1, HIGH);
  }else{
    digitalWrite(led_alarme1, LOW);
  }

  if("ultrasonic1" < 10){
    digitalWrite(led_alarme2, HIGH);
  }else{
    digitalWrite(led_alarme2, LOW);
  }
}



