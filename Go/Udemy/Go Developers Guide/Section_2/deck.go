package main

import "fmt"
// Create a new type of 'deck'
// which is a slice of strings
type deck []string

// To tell the compiler the type of variable we want to return we follow
// func funcName() type {}, where type is the return value type
func newDeck() deck {

    cards := deck{}

    // Different slices
    cardSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
    cardValues := []string{"Ace", "Two", "Three", "Four"}

    for _, suit := range cardSuits{
        for _, value := range cardValues {
            cards = append(cards, value+" of "+suit)
        }
    }

    return cards
}

// in here (d deck) is what is called a receiver, meaning any variable of type deck now
// gets access to the print method, here d is the actual copy of the deck we're working
// and that is available for us to use
// deck references that every variable of type deck can call this function
func (d deck) print() {
    // loop through the slice, and print
    // range takes the slice and loops over every element of it
    // we need to reinitialize every time (:=) since we are just dumping the i, card in every iteration
    for i, card := range d {
        fmt.Println(i, card)
    }
}

// We define parameters by the name of the variable and the type (name type, ...)
// To return multiple values we specify the type inside of parenthesis separated by a comma
func deal(d deck, handSize int) (deck, deck) {
    return d[:handSize], d[handSize:]
}
