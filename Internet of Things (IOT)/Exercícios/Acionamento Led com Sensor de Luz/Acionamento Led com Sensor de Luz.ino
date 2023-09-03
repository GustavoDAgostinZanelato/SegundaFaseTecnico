/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Acionamento de Led com Sensor de Luz

Autor: Gustavo D'Agostin Zanelato
Data: 09/08/2023
Versão: 0.0

************************************************************************ */

int porta = A1;
int valor;
int ledG = 7;
int ledB = 4;
int ledR = 2;

void setup() {
  Serial.begin(9600);
  pinMode(porta, INPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledR, OUTPUT);
}

void loop() {
  valor = analogRead(porta);
  Serial.println(valor);

  if(valor <= 36){
    digitalWrite(ledG, HIGH);
    digitalWrite(ledB, HIGH);
    digitalWrite(ledR, HIGH);
    }
  if ((valor < 36 ) && (valor <= 72)){
    digitalWrite(ledG, HIGH);
    digitalWrite(ledB, HIGH);
    digitalWrite(ledR, LOW);
    }

  if (valor > 72){
    digitalWrite(ledG, HIGH);
    digitalWrite(ledB, LOW);
    digitalWrite(ledR, LOW);
    }


}
