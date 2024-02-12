int led = 11;
int maximo = 255;
int minimo = 0;
int tempo = 100;
int i = 0;

void setup(){
  pinMode(led, OUTPUT);
}

void loop(){
  for(int i = minimo;i < maximo;i++){
  	analogWrite(led, i);
    delay(tempo);
  }
   for(i = maximo; i > minimo; i--){
     analogWrite(led, i);
     delay(tempo);
   }
}