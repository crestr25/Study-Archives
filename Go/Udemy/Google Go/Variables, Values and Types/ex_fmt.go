package main

import "fmt"

func main() {
	x := 42
	// we can use format printing.
	fmt.Printf("The value for x is %v\n", x)
	fmt.Printf("variable x is of type %T\n", x)
	fmt.Printf("variable x in binary %b\n", x)
	fmt.Printf("variable x in Hex %x\n", x)
	fmt.Printf("variable x in Hex with 0x %#x\n", x)

	generalPrinting()
	stringPrinting()
}

func generalPrinting() {
	x := 42
	// all three print to standard out

	// Print outputs without a new line
	fmt.Print(x)

	// Printf outputs the formatted version
	fmt.Printf("\n%d \t %x\n", x, x)

	// Println outputs with the new line
	fmt.Println(x)
}

func stringPrinting() {
	x := 42
	var y string

	// all three return the formatted string

	y = fmt.Sprint(x)
	fmt.Println(y)

	y = fmt.Sprintf("\n%d \t %x", x, x)
	fmt.Println(y)

	y = fmt.Sprintln(x)
	fmt.Println(y)
}
