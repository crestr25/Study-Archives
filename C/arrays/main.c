#include <stdio.h>


int main() {
    // Initialize array (all values by default are garbage, DO NOT USE THEM)
    int A[3];
    // Populate array
    A[0] = 1;
    A[1] = 2;
    A[2] = 3;
    // print size of array A 
    printf("Size of array A: %lu\n", sizeof(A));
    // print element of array A
    printf("First element of array A: %d\n", A[0]);

    // Declare and initialize array
    int B[5] = {1, 2, 3, 4, 5};
    // Declare and initialize array without size (gets size by default elements)
    int C[] = {1, 2, 3, 4, 5};
    // Declare and initialize array with size but fewer elements (gets filled with 0 for all missing elements)
    int D[5] = {1, 2, 3};


    // print values
    for (int i=0;i<5;i++) {
        printf("Array B element -> %d\n", B[i]);
        printf("Array C element -> %d\n", C[i]);
        printf("Array D element -> %d\n", D[i]);
    }

    // for a dinamically size declaration of array (it can not be initialized)
    int num;
    printf("Enter size of the array: ");
    scanf("%d", &num);

    int E[num];
    int c = 0;

    // initialize
    for (int i=0; i<num; i++) {
        E[i] = c;
        c++;
    }
    // Print
    for (int i=0; i<num; i++) {
        printf("Array E element -> %d\n", D[i]);
    }

    return 0;
}
