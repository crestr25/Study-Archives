package main

import "fmt"

const (
	a        = 1
	b        = 2.0
	c string = "Hello"
)

func main() {
	// Bool examples
	boolType()

	// Numeric examples
	numericType()

	// String examples
	stringType()

	// Const examples
	constants()
}

func boolType() {
	// Initialize variable of type bool, ZERO value (false) gets assigned
	var x bool

	fmt.Printf("Variable x is of type %T and value %v\n", x, x)
	x = true
	fmt.Printf("Variable x is of type %T and value %v\n", x, x)

	// Comparison
	a := 7
	b := 8
	fmt.Println("a < b ->", a < b)
	fmt.Println("a > b ->", a > b)
	fmt.Println("a == b ->", a == b)
}

func numericType() {
	// Initialize variable of type bool, ZERO value (false) gets assigned
	var x int
	var y float64

	fmt.Printf("Variable x is of type %T and value %v\n", x, x)
	fmt.Printf("Variable y is of type %T and value %v\n", y, y)

	// fmt.Println("a < b ->", a < b)
	// fmt.Println("a > b ->", a > b)
	// fmt.Println("a == b ->", a == b)
}

func stringType() {
	// Initialize variable of type string, ZERO value "" gets assigned
	var x string

	fmt.Printf("Variable x is of type %T and value %q\n", x, x) // %q gives a double quoted string
	x = "Hello World!"
	fmt.Printf("Variable x is of type %T and value %v\n", x, x)

	// They are slice of bytes
	bs := []byte(x)
	fmt.Printf("Variable bs is of type %T and value %v\n", bs, bs)

	// Common verbs
	fmt.Printf("String: %v, Bytes: %v \n", x, bs)
	fmt.Printf("String: %s, Bytes: %s \n", x, bs)
	fmt.Printf("String: %q, Bytes: %q \n", x, bs)
	fmt.Printf("String: %x, Bytes: %x \n", x, bs)
	fmt.Printf("String: %X, Bytes: %X \n", x, bs)

	fmt.Printf("Bytes: %#U \n", bs)

	for i, v := range x {
		fmt.Printf("at index position %d we have hex %#X\n", i, v)
	}

}

func constants() {
	fmt.Printf("constant a of type %T has value %v \n", a, a)
	fmt.Printf("constant b of type %T has value %v \n", b, b)
	fmt.Printf("constant c of type %T has value %v \n", c, c)
}
