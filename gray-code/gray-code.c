#include <stdint.h>
#include <stdio.h>


/*
 @brief:  Print given array in binary form

 @author  Abdullah Bagyapan

 @date    07/05/2024

 @param   uint8_t*  array buffer
 @param   uint8_t   size of array buffer

 @return  None
*/
void print_array(uint8_t *buffer, uint8_t size) {

    for (int i = 0; i < size; i++) {

        printf("%8b \n",buffer[i]);

    }

}


/*
 @brief:  Convert decimal to gray codes from 0 to given param[n]

 @author  Abdullah Bagyapan

 @date    07/05/2024

 @param   uint8_t   the limit point for generation
 @param   uint8_t   the array buffer to write graycodes into it

 @return  None
*/
uint8_t decimal_to_gray(uint8_t n, uint8_t *buffer) {

    int i = 0;
    
    for (int i = 0; i < n; i++) {
        
        buffer[i] = i ^ (i >> 1);
    }
}


int main() {

    uint8_t limit = 255;
    uint8_t buffer[limit];


    decimal_to_gray(limit, buffer);
    print_array(buffer, limit);

    return 0;
}