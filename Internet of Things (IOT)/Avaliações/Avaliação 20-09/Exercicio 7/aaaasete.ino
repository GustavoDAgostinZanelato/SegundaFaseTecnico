/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Exercício 7

Autor: Gustavo D'Agostin Zanelato
Data: 20/09/2023

************************************************************************ */

#include <Servo.h>
#include <TimerOne.h>
#include <Ultrasonic.h>

//Definindo o objeto do servo
Servo myservo; 

//Variáveis do sersor de distância
Ultrasonic ultrasonic(12, 13);

//Declarando as variáveis dos botões e leds do sistema
int distance;
int botao_liberacao = 10; 
int botao_alarme = 9;
int led_alarme = 2;
int led_liberacao = 3;
int estado_botao_liberacao = 0;
int estado_botao_alarme = 0;


void setup() {
  myservo.attach(8); // Indicando a porta de coneção do servo
  myservo.write(0);  // Posição inicial do servo
  Timer1.initialize(10000); //Tempo de espera de 10 segundos
  Serial.begin(9600); //comunicação com o monitor serial
  pinMode(3, INPUT);  //Indicando botoes como entradas e botoes como saidas nas linhas a seguir
  pinMode(9, INPUT);
  pinMode(2, OUTPUT);
  pinMode(10, OUTPUT);
}


void loop() {
  //variáveis para leitura dos botoes
  estado_botao_liberacao = digitalRead(botao_liberacao);
  estado_botao_alarme = digitalRead(botao_alarme);

  //configuração do sensor de distancia
  distance = ultrasonic.read();
  Serial.print("Distance in CM: ");
  Serial.println(distance);

  //Caso a distancia seja menor que 20cm, a led que indica a lieracao do veículo irá ativar
  if (distance < 20){
    digitalWrite(led_liberacao, HIGH);
  }else{
    digitalWrite(led_liberacao, LOW);
  }
  
  //Caso a distancia seja meno que 20 e o botao para liberar a cancela estiver presionado, o servo ativa
  if ((distance < 20) && (estado_botao_liberacao == HIGH)) {
    myservo.write(90);  //Movimenta o servo em um angulo de 90 graus
    Timer1.initialize(10000); //Tempo que a cancela fica aberta

    if(estado_botao_alarme == HIGH){ //Se durante a cancela aberta o botão do alarme for ativado
      digitalWrite(led_alarme, HIGH);//O led do alarme irá ativar
    }else{
      digitalWrite(led_alarme, LOW);
    }

    myservo.write(0); //Volta o servo para a posição inicial

  } else {
    myservo.write(0);  //Mantém o servo na posição inicial
  }
}
