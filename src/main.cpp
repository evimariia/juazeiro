#include <Arduino.h>
#include <MFRC522.h>
#include <SPI.h>

#define SS_PIN 5    // ESP32 pin D5 (GPIO5) para SDA (SS) do RC522
#define RST_PIN 22  // ESP32 pin D27 (GPIO27) para RST do RC522
#define LED_VERDE 21
#define LED_VERMELHO 26

MFRC522 mfrc522(SS_PIN, RST_PIN); // Cria uma instância do MFRC522

void setup() {
  Serial.begin(115200); // Inicializa a comunicação serial
  while (!Serial);
  SPI.begin();        // Inicializa o barramento SPI
  mfrc522.PCD_Init(); // Inicializa o MFRC522

  pinMode(LED_VERDE, OUTPUT); // Configura o pino do LED verde como saída
  pinMode(LED_VERMELHO, OUTPUT); // Configura o pino do LED vermelho como saída
  digitalWrite(LED_VERDE, LOW); // Liga o LED verde inicialmente (estado padrão)
  digitalWrite(LED_VERMELHO, HIGH); // Liga o LED vermelho inicialmente (estado padrão)

  Serial.println("Aproxime seu cartao RFID...");
  Serial.println();
}

void loop() {
  // Reset the loop if no new card present on the sensor/reader.
  // This saves the entire process when no card is present = performance
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    // Se não houver cartão, garante que o LED esteja ligado
    digitalWrite(LED_VERMELHO, HIGH);
    digitalWrite(LED_VERDE, LOW);
    return;
  }

  // Verify if the card has been read
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

    // Cartão detectado e lido com sucesso, desliga o LED
  digitalWrite(LED_VERDE, HIGH);
  digitalWrite(LED_VERMELHO, LOW);
  delay(3000);

  Serial.print("UID da Tag: ");
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();

  mfrc522.PICC_HaltA(); // Coloca a tag em estado de "parada"
}