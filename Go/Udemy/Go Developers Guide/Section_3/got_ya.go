package main

import "fmt"

// Slice objects get passed by reference, so they are mutable
// To achieve this with a pass by value language a slice gets copied in the parameter
// however the element in the slice that points to the head of the underlying array 
// is a pointer so it's the same for both

// this are called reference types and there are some:
// slices, maps, channels, pointers, functions

// The immutable ones are the value types:
// int, float, string, bool, structs
func main() {
    mySlice := []string{"Hi", "There", "How", "Are", "You"}
    // When we call this one the slice actually gets modified
    updateSlice(mySlice)

    fmt.Println(mySlice)
}

func updateSlice(s []string) {
    s[0] = "Bye"
}
