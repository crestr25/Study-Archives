package main

import "fmt"

// In order to "reuse" the same function for different argument types we can declare
// an interface
// Interfaces are what is called an interface type in contrast to the concrete types such
// as map, struct, int, string
type bot interface {
    // if there is a type in this program that has a getGreeting function and it returns a 
    // string then you are member of the new interface bot (it means that interfaces are implicit)
    
    // This means that any type that has associated (Receiver function) functions called
    // getGreeting will be passed along this interface
    getGreeting() string
}
type englishBot struct {}
type spanishBot struct {}

func main() {
    eb := englishBot{} 
    sb := spanishBot{}

    printGreeting(eb)
    printGreeting(sb)
}
// we want to make an interface off of these two functions
func printGreeting(b bot) {
    fmt.Println(b.getGreeting())
}
// func printGreeting(eb englishBot) {
//     fmt.Println(eb.getGreeting())
// }
//
// func printGreeting(sb spanishBot) {
//     fmt.Println(sb.getGreeting())
// }

// Receiver functions
func (englishBot) getGreeting() string {
    return "Hi there!"
}

func (spanishBot) getGreeting() string {
    return "Hola!"
}
