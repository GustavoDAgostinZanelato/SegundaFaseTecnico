int porta = A1;
int led1 = 7;
int valor;

void setup() {
  Serial.begin(9600);
  pinMode(porta, INPUT);
}

void loop() {
  valor = analogRead(porta);
  Serial.println(valor);

  if(valor <= 50){
    digitalWrite(led1, HIGH);
  }
}
