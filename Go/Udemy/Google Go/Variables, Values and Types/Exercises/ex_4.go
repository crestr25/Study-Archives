package main

import "fmt"

type my_int int

func main() {
	var x my_int

	fmt.Printf("Variable x of type %T has value %v\n", x, x)

	x = 42

	fmt.Printf("Variable x of type %T has value %v\n", x, x)
}
