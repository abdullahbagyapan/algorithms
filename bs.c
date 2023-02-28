#include <stdio.h>
#include <stdbool.h>






bool binarySearch(int array[],int target) {
    int middle,startPoint = 0;
    int endPoint = sizeof(array) - 1; // length of array

    while (startPoint <= endPoint) {
        middle = (startPoint + endPoint) / 2;
        if (array[middle] == target) {
            return true;
        }
        else if (array[middle] > target) {
            endPoint = middle - 1 ;
        }
        else {
            startPoint = middle + 1;
        }
    }
    return false;
}




int main(void) {

    int array[] = {1,2,3,4,5,6,7,8,9};

    int target = 5;

    printf("%b", binarySearch(array,3));
    // return 1

    printf("%b", binarySearch(array,10));
    // return 0



}