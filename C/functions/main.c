#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x;
    int y;
};

// Function declaration or prototype
// if not present the compiler will complain that the main function calls an undeclared function
int add(int x, int y);
void swap_value(int x, int y);
void swap_address(int *x, int *y);
void array_param(int A[], int n);
int *array_return(int n);
int struct_param_value(struct Point p);
int struct_param_address(struct Point *p);
struct Point *struct_return(int x, int y);

int main(){
    // declare and initialize a,b and declare c
    int a=10, b=20, c;
    // call function
    c = add(a, b);
    printf("the sum of %d + %d = %d\n", a, b, c);

    // parameter passing
    //
    // by value, the parameters are copied to the function's formal parameters
    int a2=10, b2=20;
    swap_value(a2, b2);
    printf("a: %d, b: %d\n", a2, b2);
    // by address, the address of the original variables are passed to the function
    int a3=10, b3=20;
    swap_address(&a3, &b3);
    printf("a: %d, b: %d\n", a3, b3);

    // Array as parameter
    int A[5] = {1, 2, 3, 4, 5};
    // the parameter A is passed as a pointer to an array (passed as address)
    // arrays CANNOT be passed by value
    array_param(A, 5);
    // Array return from function
    // pointer that will store the address to the first element
    int * arr;
    arr = array_return(5);
    printf("Array returned from function %p\n", arr);
    array_param(arr, 5);

    // Struct as parameter
    struct Point p1 = { 10, 20 };
    printf("The area of point 1 is: %d\n", struct_param_value(p1));
    printf("The area of modified point 1 is: %d\n", struct_param_address(&p1));
    // Struct returned
    struct Point *p2;
    p2 = struct_return(100, 200);
    printf("Point returned from function x: %d, y: %d\n", p2 -> x, p2 -> y);
 
    return 0;
}

// function definition
int add(int x, int y) {
    int c;

    c = x + y;

    return c;
}

void swap_value(int x, int y) {
    int temp;
    temp = x;
    x = y;
    y = temp;
}

void swap_address(int *x, int *y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void array_param(int A[], int n) {
    // the array can also be passed as int *A, a pointer to an int
    // int A[], means a pointer to an array only (it is treated as an array, be cautious with sizeof or foreach(c++))
    // leaving the int *A is more general, int A[] is specific
    printf("Array param function...\n");
    for (int i = 0; i<n; i++) {
        printf("%d\n", A[i]);
    }
}

int *array_return(int n) {
    printf("Array return function...\n");
    int *P;
    P = (int *)malloc(n*sizeof(int));

    for (int i = 0; i<n; i++) {
        P[i] = i;
    }
    return P;
}

int struct_param_value(struct Point p) {
    // a new struct is created and the values are copied
    return p.x * p.y;
}

int struct_param_address(struct Point *p) {
    // a pointer to the struct is passed as parameter
    p -> x = 100;
    p -> y = 200;
    /* return (*p).x * (*p).y; */
    return p -> x * p -> y;
}

struct Point *struct_return(int x, int y) {
    // a pointer to the struct is passed as parameter
    struct Point *p;

    p = (struct Point *)malloc(sizeof(struct Point));
    p -> x = 100;
    p -> y = 200;
    return p;
}
