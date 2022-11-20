package main


func main() {

    // var - we're about to create a new variable
    // card - name of the variable
    // string - only this type will ever be assigned to this variable, go can infer the type from the right hand side
    // Ace of Spades - value to assign
    // var card string = "Ace of Spades" 

    // We can make use of the := operator to tell go to initialize the var with the infered type, once it is initialized
    // card := "some value"
    // we can reassign just by the = operator
    // card = "new value", notice no :=


    // a data structure is a slice(which can contain objects of the same type, and it can grow or shrink in size)
    cards := newDeck()
    //cards.print()    
    _, remainingCards := deal(cards, 3)
    remainingCards.shuffle()
    remainingCards.print()
}
