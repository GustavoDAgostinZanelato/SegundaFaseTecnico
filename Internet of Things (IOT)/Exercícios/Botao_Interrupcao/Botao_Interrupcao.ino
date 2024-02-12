const byte pin_led = 13;
const byte pin_interrupcao = 2;
volatile byte estado = LOW;

void setup() {
  pinMode(pin_led, OUTPUT);
  pinMode(pin_interrupcao, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pin_interrupcao), funcao, LOW);
}

void loop() {
  digitalWrite(pin_led, estado);
}

void funcao(){
  estado =! estado;
}


