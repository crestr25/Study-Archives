#include <stdio.h>

// C struct
struct Point {
  int x;
  int y;
};

// definition of C struct functions
void initializePoint(struct Point *p, int x, int y);
int slope(struct Point p1, struct Point p2);
void changeX(struct Point *p1, int x);

// Class (C++)
class PointClass {
private:
  int x;
  int y;

public:
  // Constructor overloading
  PointClass() { // default constructor
    x = 1;
    y = 2;
  }
  PointClass(int valx, int valy) { // overloaded constructor
    x = valx;
    y = valy;
  };

  int slope(PointClass p2) { return (p2.getY() - y) / (p2.getX() - x); }
  void changeX(int valx) { x = valx; }
  void changeY(int valy) { y = valy; }
  int getX() { return x; }
  int getY() { return y; }
  ~PointClass() { printf("Good bye cruel world!!\n"); }
};

int main() {
  // C: struct with functions
  struct Point p1;
  struct Point p2;
  initializePoint(&p1, 10, 20);
  initializePoint(&p2, 20, 30);
  printf("slope between p1 and p2: %d\n", slope(p1, p2));
  changeX(&p1, 20);
  printf("Point1 x: %d, y: %d\n", p1.x, p1.y);

  // C++: Classes
  PointClass pc1(10, 20);
  PointClass pc2(20, 30);
  PointClass pc3;
  printf("slope between pc1 and pc2: %d\n", pc1.slope(pc2));
  pc1.changeX(20);
  printf("PointClass1 x: %d, y: %d\n", pc1.getX(), pc1.getY());
  printf("PointClass2 x: %d, y: %d\n", pc2.getX(), pc2.getY());
  printf("PointClass3 x: %d, y: %d\n", pc3.getX(), pc3.getY());

  return 0;
}

// C struct functions
void initializePoint(struct Point *p, int x, int y) {
  p->x = x;
  p->y = y;
}

int slope(struct Point p1, struct Point p2) {
  return (p2.y - p1.y) / (p2.x - p1.x);
}

void changeX(struct Point *p1, int x) { p1->x = x; }

void changeY(struct Point *p1, int y) { p1->y = y; }
