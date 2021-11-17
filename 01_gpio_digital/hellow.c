#include <wiringPi.h>
#define LED_Blink_a 7
#define LED_Blink_b 5
#define LED_Blink_c 3

int main(void) {
    wiringPiSetup();
    pinMode(LED_Blink_a, OUTPUT);
    pinMode(LED_Blink_b, OUTPUT);
    pinMode(LED_Blink_c, OUTPUT);
    for(int i=0; i<5; i++){
        digitalWrite(LED_Blink_a, HIGH); delay(2000);
        digitalWrite(LED_Blink_a, LOW);

        digitalWrite(LED_Blink_b, HIGH); delay(2000);
        digitalWrite(LED_Blink_b, LOW);

        digitalWrite(LED_Blink_c, HIGH); delay(2000);
        digitalWrite(LED_Blink_c, LOW);
    
    }


return 0;

}
gcc -Wall -o file_name file_name.c -lwiringPi

ls   - file_name

