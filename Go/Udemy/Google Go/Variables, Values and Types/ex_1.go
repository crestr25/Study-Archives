package main

import "fmt"

func main() {
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
