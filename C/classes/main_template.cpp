#include <iostream>

using namespace std;

template <class T> class Arithmetic {
private:
  T a;
  T b;

public:
  Arithmetic(T a, T b);
  T add();
  T substract();
};

template <class T> Arithmetic<T>::Arithmetic(T a, T b) {
  this->a = a;
  this->b = b;
};

template <class T> T Arithmetic<T>::add() {
  T c;
  c = this->b + this->a;
  return c;
};

template <class T> T Arithmetic<T>::substract() {
  T c;
  c = this->b - this->a;
  return c;
};

int main() {
  Arithmetic<int> ar(1, 2);
  cout << "add from class: " << ar.add() << endl;
  cout << "substract from class: " << ar.substract() << endl;

  Arithmetic<int> ar2(1.0, 2.0);
  cout << "add from class: " << ar2.add() << endl;
  cout << "substract from class: " << ar2.substract() << endl;

  Arithmetic<char> ar3('A', 'B');
  // Type casting with (int)
  cout << "add from class: " << (int)ar3.add() << endl;
  cout << "substract from class: " << (int)ar3.substract() << endl;
  return 0;
}
