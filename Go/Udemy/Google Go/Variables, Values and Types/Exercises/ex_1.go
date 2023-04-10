package main

import "fmt"

func main() {
	x := 42
	y := "James Bond"
	z := true

	fmt.Printf("Variable x of type %T has value %v\n", x, x)
	fmt.Printf("Variable x of type %T has value %v\n", y, y)
	fmt.Printf("Variable z of type %T has value %v\n", z, z)
}
