#include <stdio.h>



void selectionSorting(int *array) {
    int smallest,i,j;

    for (i = 0 ; i < sizeof(array) -1 ; i++) {
        smallest = array[i];
        int index;

        for (j = i + 1; j < sizeof(array) ; j++) {

            if (smallest > array[j]) {
                smallest = array[j];
                index = j;
            }


        }
        int tmp = array[i];

        array[i] = smallest;
        array[index] = tmp;
    }
}

void printList(int array[]) {

    for (int i = 0 ; i < sizeof(array) -1; i++) {
        printf("%d\n",array[i]);
    }

}






int main(void) {

    int array[] = {4,7,9,3,17,10,11};
    selectionSorting(array);
    printList(array);


}