#include <stdio.h>
#include <stdbool.h>



void bubbleSorting(int *array) {
    int size = sizeof (array) - 1;


    while (true) {
        bool isSwap = false;

        for (int i = 0 ; i < size - 1 ; i++) {
            if (array[i] > array[i+1]) {

                int tmp = array[i];

                array[i] = array[i+1];
                array[i+1] = tmp;
                isSwap = true;
            }
        }

        if (isSwap) {
            continue;
        }
        else {
            break;
        }
    }
}


void printList(int array[]) {

    for (int i = 0 ; i < sizeof(array) -1; i++) {
        printf("%d\n",array[i]);
    }

}






int main(void) {
    int array[] = {4,7,9,3,17,10,11};
    bubbleSorting(array);
    printList(array);
}