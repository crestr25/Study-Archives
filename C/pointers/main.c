#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x;
    int y;
};

int main() {
    
    // Declare and initialize a DATA VARIABLE
    int data_var = 1;
    // Declare an ADDRESS VARIABLE (Pointer)
    // Will be the same size as the data address it will store | int (4 Bytes)
    // This does not point to the heap.
    int *addr_var;

    // Store DATA VARIABLE ADDRESS in ADDRESS VARIABLE (Initialize pointer)
    addr_var = &data_var;

    // Print value of DATA VARIABLE from its var
    printf("data_var value: %d\n", data_var);

    // Print value of Address for DATA VARIABLE from its var
    printf("data_var address: %p\n", &data_var);

    // Print ADDRESS VARIABLE value (the address of the DATA VARIABLE)
    printf("addr_var value: %p\n", addr_var);

    // Print ADDRESS VARIABLE value that the address points to (the address of the DATA VARIABLE)
    // Also called Dereferencing
    printf("addr_var value: %d\n", *addr_var);


    // Declare and initialize array
    int A[5] = {1,2,3,4,5};

    // an array variable stores the address of its first element
    printf("array A address: %p\n", A);

    // declare and initialize pointer to array (no need to use & since it is already an address)
    int *pnt_arr = A;
    printf("array A address from pnt_arr: %p\n", pnt_arr);
    printf("array A first value from pnt_arr: %d\n", pnt_arr[0]);


    // Allocate memory in heap
    // sizeof is used since we let the compiler fill the actual size of the data
    // the parenthesis are for type casting since malloc return a void pointer (generic pointer)
    int *pnt = (int *)malloc(2*sizeof(int));
    pnt[0] = 1;
    pnt[1] = 2;
    printf("pnt address value: %p\n", pnt);
    printf("pnt first value: %d\n", pnt[0]);

    // free allocated memory
    free(pnt);

    // Pointer to struct
    // declare and initialize struct
    struct Point pointA = {10, 20};
    // Declare and initialize pointer to struct
    struct Point *pnt_struct = &pointA;
    // Declare pointer to struct to use with malloc
    struct Point *pnt_dinamic;

    // instanciate a struct in heap
    pnt_dinamic = (struct Point *)malloc(sizeof(struct Point));
    
    // modify value from pointer (enclosed because . operations are higher precedence)
    (*pnt_struct).x = 100;
    (*pnt_dinamic).x = 1000;
    // modify value from pointer with arrow operator
    pnt_struct -> x = 200;
    pnt_dinamic -> x = 2000;
    printf("pnt_struct address value: %p\n", pnt_struct);
    printf("pnt_dinamic address value: %p\n", pnt_dinamic);
    printf("pointA value from pointer: %d\n", (*pnt_struct).x);
    printf("pnt_dinamic value from pointer: %d\n", (*pnt_dinamic).x);
    free(pnt_dinamic);
    return 0;
}
