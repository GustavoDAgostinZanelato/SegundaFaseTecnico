/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Cafeteira

Autor: Ferando Menna Barreto Nogueira e Gustavo D'Agostin Zanelato
Data: 13/09/2023

************************************************************************ */

// variáveis do NTC
const byte pin_led = 13;
const byte pin_interrupcao = 2;
volatile byte estado = LOW;
int ThermistorPin = 0;
int Vo;
float R1 = 10000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

// botoes e leds
int botao_agua = 13;
int botao_jarra = 12;
int estado_botao_jarra = 0;
int estado_botao_agua = 0;
int led_motor = 11;
int led_base_aquecedora = 10;

// Variáveis do sensor LDR
int porta = A1;
int valor;

// Variáveis do nivel de luminosidade do led da base aquecedora
int valor2;
int brilho;
int porta2 = 11;

//variáveis do buzzer
const int pin_entrada = A0;
const int buzzer = 2;


void setup() {
  // declarando o botao de ligar da cafeteira
  pinMode(pin_led, OUTPUT);
  pinMode(pin_interrupcao, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pin_interrupcao), funcao_agua, LOW);
  Serial.begin(9600);

  // Declarando o botao da presençça de jarra e água além dos leds
  pinMode(botao_agua, INPUT_PULLUP);
  pinMode(botao_jarra, INPUT_PULLUP);
  pinMode(led_motor, OUTPUT);
  pinMode(led_base_aquecedora, OUTPUT);

  //Variáveis do sensor LDR
  pinMode(porta, OUTPUT);

  //variáveis do buzzer
  pinMode(pin_entrada, INPUT);
  pinMode(buzzer, OUTPUT);
}


void loop() {

}

//Função que apresenta o funcionameto da cefeteira
void funcao_agua(){
  estado =! estado;

  //Sensor de Temperatura
  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0; 
  Serial.print("Temperature: "); 
  Serial.print(Tc);
  Serial.println(" C");   
  delay(500);

  //Botoes da água e da Jarra
  estado_botao_agua = digitalRead(botao_agua);
  estado_botao_jarra = digitalRead(botao_jarra);

  //Sensor de lumminosidade
  valor = analogRead(porta);

  //Caso os itens abaixo sejam verdadeiros, o motor de cafeteira liga e liga o buzzer para indicar que o café está pronto
  if ((Tc >= 30) && (estado_botao_agua == HIGH) && (estado_botao_jarra == HIGH) && (valor >= 10000)) {
    digitalWrite(led_motor, HIGH);
    digitalWrite(buzzer, HIGH);
  }

  //Caso exita água no reservatório, a base aquecedora liga com 100% de potencia
  if((estado_botao_agua == HIGH) && (valor >= 30)){
    digitalWrite(led_base_aquecedora, HIGH);
  }

  //Caso não haja água no reservatório, a base aquecedora liga com 50% de potencia
  if(estado_botao_agua == LOW){
    brilho = 50 * 2.55;
    analogWrite(porta2, brilho);
    digitalWrite(led_base_aquecedora, HIGH);
  }
}

