package main

import "fmt"

type my_var int

var x my_var
var y int

func main() {
	fmt.Printf("Variable x is of type %T and value %v\n", x, x)
	x = 42
	fmt.Printf("Variable x is of type %T and value %v\n", x, x)

	y = int(x)
	fmt.Printf("Variable x is of type %T and value %v\n", y, y)
}
