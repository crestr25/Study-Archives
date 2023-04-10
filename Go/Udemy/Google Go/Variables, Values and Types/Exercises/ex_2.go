package main

import "fmt"

var x int
var y string
var z bool

func main() {

	// all of the variables with default ZERO Value

	fmt.Printf("Var x of type %T has value %v\n", x, x)
	fmt.Printf("Var y of type %T has value %v\n", y, y)
	fmt.Printf("Var z of type %T has value %v\n", z, z)
}
