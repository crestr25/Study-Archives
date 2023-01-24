package main

import "fmt"

// in Go, maps have the following properties
// Keys are indexed so we can iterate over them
// We don't need to know all the keys at compile time, structs do.
// all keys and values must be of the same type (keys and values can be different types)
// They are reference values, meaning we pass a reference to the underlying data.

func main() {

    // We have some different ways of creating maps in go

    // 1st - Create a map of keys type string and values type string
    colors := map[string]string {
        "red": "#ff0000",
        "white": "#ffffff",
    }
    fmt.Println(colors)

    // 2nd - initialize an empty map
    var colors_2 map[string]string
    fmt.Println(colors_2)

    // 3rd - Use a built-in function
    colors_3 := make(map[string]string)
    colors_3["black"] = "#000000"
    colors_3["red"] = "#ff0000"
    // Delete an entry
    delete(colors_3, "red")
    fmt.Println(colors_3)
    
    // functions on maps
    printMap(colors)
}

func printMap(c map[string]string) {
    for color, hex := range c {
        fmt.Println(color, "->", hex)
    }
}
