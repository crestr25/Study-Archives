// Package == Project == Workspace
// All files that belong to the same workspace are expected to have
// that {package "name"}

// main is the name designed to let go build and compile the file to create an 
// executable, if the name is different it will be considered a helper package and 
// the command {go build} would not return an executable file
package main

// Import external packages to use in our code, the name of the package must be
// enclosed in double quotes

// fmt implements i/o functions that are analogous to C's printf and scanf
import "fmt"

// We should always have a main function!, i.e this applies to the package main
// as it requires a main function to be present
func main() {
    fmt.Println("Hello World!!")
}
