#include <wiringPi.h>
#define LED_PIN_a 7    // LED_PIN_a 라는 변수.
#define LED_PIN_b 5
#define LED_PIN_c 3

int main(void) {
    wiringPiSetup();
    pinMode(LED_PIN_a, OUTPUT);
    pinMode(LED_PIN_b, OUTPUT);
    pinMode(LED_PIN_c, OUTPUT);
    for (int i=0; i<5; i++) {
        digitalWrite(LED_PIN_a, HIGH); delay(2000);
        digitalWrite(LED_PIN_a, LOW);

        digitalWrite(LED_PIN_b, HIGH); delay(2000);
        digitalWrite(LED_PIN_b, LOW);

        digitalWrite(LED_PIN_c, HIGH); delay(2000);
        digitalWrite(LED_PIN_c, LOW);
    }
    return 0;
}

// ls   - Led_blink.c

// gcc -Wall -o Led_blink Led_blink.c -lwiringPi
// ls    - Led_blink
// ./Led_blink