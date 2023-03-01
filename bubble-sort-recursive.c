#include <stdio.h>
#include <stdbool.h>



void bubbleSorting(int *array) {
    bool isHasSwap = false;

    for (int i = 0 ; i < sizeof(array) -2 ; i++) { // size0f(array) - 2  -->> cause of array[i+1] out of range

        if (array[i] > array[i+1]) {
            int tmp = array[i];

            array[i] = array[i+1];
            array[i+1] = tmp;
            isHasSwap = true;
        }
    }

    if (isHasSwap) {
        bubbleSorting(array);
    }
    else {
        return;
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