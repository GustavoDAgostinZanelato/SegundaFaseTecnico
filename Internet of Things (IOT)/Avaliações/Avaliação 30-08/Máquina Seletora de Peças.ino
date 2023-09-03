#include <Servo.h>

Servo myservo;  // Objeto do servo

const int trigPin = 9;    // Pino TRIG do sensor ultrassônico
const int echoPin = 10;   // Pino ECHO do sensor ultrassônico
int maxDistance = 30;     // Distância máxima para movimentar o servo
long duration, distance;  // Variáveis para calcular a distância

void setup() {
  myservo.attach(8);      // Pino do servo
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  myservo.write(90);      // Posição inicial do servo
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  
  Serial.print("Distancia: ");
  Serial.println(distance);
  
  if (distance < 30) {
    myservo.write(0);     // Gira o servo para a direita (menor distância)
  } else {
    myservo.write(90);    // Gira o servo para a posição central (maior distância)
  }
  
  delay(500);  // Aguarda um momento antes da próxima leitura
}