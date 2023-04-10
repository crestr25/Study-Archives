package main

import "fmt"

func main() {
	varDeclareZeroValues()
	shortDeclare()
	customTypes()
	fmt.Println("Global scope var variable", X)
}

// allows for declarations outside a function scope
var X = "hello"

func customTypes() {
	// We can declare a new type
	type myVar int         // int is the undelying type
	type myOtherVar string // string is the undelying type

	var x myVar
	var y myOtherVar
	var z int

	x = 42
	y = "hello"

	fmt.Printf("x has value %v\n", x)
	fmt.Printf("variable x is of type %T\n", x)

	fmt.Printf("y has value %v\n", y)
	fmt.Printf("variable y is of type %T\n", y)

	// we can convert myVar to it's underlying type int
	z = int(x)
	fmt.Printf("z has value %v\n", z)
	fmt.Printf("variable z is of type %T\n", z)
}

func varDeclareZeroValues() {
	// var keyword helps declare a variable an provides two options
	// provide the type and assign its ZERO value.
	// or just assign the value and it will deduce the type. (global scope example)
	var x int
	var y float32

	var z string
	var w *int
	var v []int

	fmt.Println("Zero value for int", x)
	fmt.Printf("variable x is of type %T\n", x)

	fmt.Println("Zero value for float32", y)
	fmt.Printf("variable y is of type %T\n", y)

	fmt.Println("Zero value for string", z)
	fmt.Printf("variable z is of type %T\n", z)

	fmt.Println("Zero value for pointer", w)
	fmt.Printf("variable w is of type %T\n", w)

	fmt.Println("Zero value for slice", v)
	fmt.Printf("variable v is of type %T\n", v)
}

func shortDeclare() {
	// Short declaration allows to declare and assign in the same line
	x := 42
	fmt.Println(x)
	// since x already exists we can re assign without declaring
	x = 32
	fmt.Println(x)
	// statements are each of the actions which are made of expressions
	// We can think of statements as each action (6 lines in the program)
	// We evaluate expressions and assign the result.
	x = 32 + 42 // this 32 + 42 is the expression that evaluates to 74.
	fmt.Println(x)
}
