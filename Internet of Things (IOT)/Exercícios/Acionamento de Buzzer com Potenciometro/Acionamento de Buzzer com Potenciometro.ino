/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Título

Autor: Gustavo D'Agostin Zanelato
Data: 09/08/2023
Versão: 0.0

************************************************************************ */
const int pin_entrada = A0;
   
int valor;
float tensao;
int pin_l;

void setup() {
  Serial.begin(9600);
    pinMode(pin_entrada, INPUT);
}

void loop() {
  valor = analogRead(pin_entrada);
  tensao = float(valor)*5/1023;
  Serial.print("Tesao = ");
  Serial.print(tensao);
  Serial.println(" V");

}
