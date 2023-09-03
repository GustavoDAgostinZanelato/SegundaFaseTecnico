/* ************************************************************************

Colégio SATC
Curso Técnico de Informática
Disciplina: IoT
Turma: 2190
Professor: Marcos Antonio Jeremias Coelho

Programa: Calibrando Sensor de Luz com Led RGB

Autor: Gustavo D'Agostin Zanelato
Data: 17/08/23
Versão: 0.0

************************************************************************ */

// Matriz com os pinos onde o LED RGB vai ser conectado
int matrizPinodosLEDS[] = {11,10,9};

// Uma variável booleana para indicar se o sensor foi calibrado
bool balanco = false;

//Matriz de floats para armazenar o valor das cores
float matrizCores[] = {0,0,0};
float matrizBranco[] = {0,0,0};
float matrizPreto[] = {0,0,0};

//Variável para armazenar a média das leitura
int mediaLeituras;
const int ledR = 11;
const int ledG = 10;
const int ledB = 9;

void setup() {   
  //Declaração dos pinos como de saída   
  pinMode(ledR,OUTPUT);//LED VERMELHO   
  pinMode(ledG,OUTPUT);//LED GREEN 
  pinMode(ledB,OUTPUT);//LED BLUE   
  Serial.begin(9600);//Inicia a comunicação serial   
}

void loop() {   
  // Verifica se o Balanco de branco foi calibrado   
  checaBalanco();    
  //Checa qual é a cor   
  checaCores();   
  // Imprime na Serial o valor das cores   
  mostraCores();
}

// Verifica se o Balanco de branco foi calibrado
void checaBalanco() {   
  //checa se o balanço de branco foi feito   
  if(balanco == false){     
    confBalanco();   
  }
}

//Configura o balanco de Branco
void confBalanco() {   
  //Calibrando o branco!   
  Serial.println("Calibrando o branco");   
  delay(5000);   

  for(int i = 0;i<=2;i++){     
    digitalWrite(matrizPinodosLEDS[i],HIGH);     
    delay(100);     
    mediaSensor(5);               
    matrizBranco[i] = mediaLeituras;     
    digitalWrite(matrizPinodosLEDS[i],LOW);     
    delay(100);   
  }   

  //Calibrando o preto!   
  Serial.println("Calibrando o preto");   
  delay(5000);   
  for(int i = 0;i<=2;i++){     
    digitalWrite(matrizPinodosLEDS[i],HIGH);     
    delay(100);     
    mediaSensor(5);     
    matrizPreto[i] = mediaLeituras;     
    digitalWrite(matrizPinodosLEDS[i],LOW);     
    delay(100);   
  }   

  //Avisa que a calibragem foi feita   
  Serial.println("Sensor Calibrado");   
  balanco = true;   
  delay(3000); 
}

//Checa a cor
void checaCores(){   
  for(int i = 0;i<=2;i++){     
    digitalWrite(matrizPinodosLEDS[i],HIGH);     
    delay(100);     
    mediaSensor(5);                       
    matrizCores[i] = mediaLeituras;             
    float cinzaDif = matrizBranco[i] - matrizPreto[i];     
    matrizCores[i] = (matrizCores[i] - matrizPreto[i])/(cinzaDif)*255;      
    digitalWrite(matrizPinodosLEDS[i],LOW);     
    delay(100);   
  }
}


void mediaSensor(int vezes){   
  int leituras;   
  int somatorio=0;   
  for(int i = 0;i < vezes;i++){     
    leituras = analogRead(A1);     
    somatorio = leituras + somatorio;     
    delay(10);   
  }   
  mediaLeituras = (somatorio)/vezes;
}

void mostraCores(){   
  Serial.print("R = ");   
  Serial.println(int(matrizCores[0]));   
  Serial.print("G = ");   
  Serial.println(int(matrizCores[1]));   
  Serial.print("B = ");   
  Serial.println(int(matrizCores[2]));
}

 