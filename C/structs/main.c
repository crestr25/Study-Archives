#include <stdio.h>

// Define structs, does not consume memory
struct Point {
    int x;
    int y;
} pointGlobal;

int main() {

    // Check the declaration of global variable
    printf("%d\n", pointGlobal.x);
    
    // Declare a new struct (values assigned to data members are trash DO NOT USE)
    struct Point pointA;

    // Declare and initialize a new struct
    struct Point pointB = {1, 2};

    // Check the size of the struct (int 4bytes -> 8bytes)
    printf("size of pointB -> %lu Bytes\n", sizeof(pointB));

    // Accessing members
    printf("%d\n", pointB.x);

    // Modify members
    pointB.x = 10;
    printf("%d\n", pointB.x);

    // Array of structs
    // Declare and initialize (partially)
    struct Point points[6] = {{30, 60}, {31, 61}};
    // Declare new points to add
    struct Point point1 = {32, 62};
    struct Point point2 = {33, 63};
    struct Point point3 = {34, 64};
    struct Point point4 = {35, 65};
    // Add the points to the array
    points[2] = point1;
    points[3] = point2;
    points[4] = point3;
    points[5] = point4;
    // Print points    
    for (int i=0;i<6;i++) {
        printf("point %d, x: %d y: %d\n", i, points[i].x, points[i].y);
    }
    return 0;
}

