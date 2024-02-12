/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Acionamento de Led RGB com Capacitor

Autor: Gustavo D'Agostin Zanelato
Data: 09/08/2023
Versão: 0.0

************************************************************************ */

int saida = 11;
int entrada = A5;
int pontos = 500;
int tempo = 1;
int valor = k;
float tensao;

const int pin_led1 = 7;  // S1
const int pin_led2 = 6;  // S2
const int pin_led3 = 5;  // S3

void setup() {
  pinMode(saida, OUTPUT);
  pinMode(entrada, INPUT);
  Serial.begin(9600);
  pinMode(pin_led1, OUTPUT);
}

void loop() {
  digitalWrite(saida, LOW);
  for (k=1; k<=pontos; k++) {
    valor = analogRead(entrada);
    tensao = float(valor)*5/1023;
    Serial.println(tensao);
    if (tensao<3.9){
    digitalWrite(pin_led1, LOW);
    delay(tempo);
  }
  }
  digitalWrite(saida, HIGH);
  for (k=1; k<=pontos; k++) {
    valor = analogRead(entrada);
    tensao = float(valor)*5/1023;
    Serial.println(tensao);
    
    if (tensao>4){
    digitalWrite(pin_led1, HIGH);
    delay(tempo);
  }
  }
}