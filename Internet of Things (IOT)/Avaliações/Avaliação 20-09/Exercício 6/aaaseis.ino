/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Exercício 6

Autor: Gustavo D'Agostin Zanelato
Data: 20/09/2023

************************************************************************ */

// Declarando as  vaiáveis a serem utilizadas
int porta = A1;
int valor;


void setup() {
  Serial.begin(9600); // Definindo o monitor serial
  pinMode(porta, INPUT); // Declarando a variavel porta como saída
}

void loop() {
  
  valor = analogRead(porta); //varipavel valor recebe a informação da porta
  Serial.println(valor); //exibindo a valor da luminosidade no monitor serial

}
