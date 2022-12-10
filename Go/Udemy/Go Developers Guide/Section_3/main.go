package main

import "fmt"

// Defining a new contactInfo struct
type contactInfo struct {
    email string
    zipCode int
}
// Defining a importantPerson struct
type importantPerson struct {
    firstName string
    lastName string
    contact contactInfo // We can ommit the naming and it just defaults to the name of the
    // struct
}
// Defining a new struct person
type person struct {
    firstName string
    lastName string
}

func main() {
    // Basic structs
    basicStructs()
    // Embedded Structs
    embeddedStructs()
}

func embeddedStructs() {
    // Declaring a person struct with embedded stuff 
    carlos := importantPerson{
        firstName: "Carlos",
        lastName: "Restrepo",
        contact: contactInfo{
            email: "crestrepo@mail.com",
            zipCode: 1,
        }, // must have a comma man!!!
    }
    fmt.Println(carlos)

    fmt.Printf("%+v", carlos) // print every value, we need to pass a string and format it 

    // Receiver functions
    carlosPointer := &carlos
    carlosPointer.updateName("Charlie")
    carlos.print()
}

func basicStructs() {
    // first way of defining a new structure
    luisa := person{"Luisa", "Fonseca"}
    // Secong way of declaring a structure
    carlos := person{firstName: "Carlos", lastName: "Restrepo"}
    // Third way of creating a variable
    var pia person // This way a Zero value gets assigned
    // "" - Strings
    // 0  - Int
    // 0  - Float
    // bool - false

    fmt.Println(carlos) 
    fmt.Println(luisa)
    fmt.Printf("%+v", pia) // print every value, we need to pass a string and format it 
    
    // add values to the fields of the structs
    pia.firstName = "Pia"
    pia.lastName = "Fonseca"
    fmt.Printf("\n%+v\n", pia) // print every value, we need to pass a string and format it 
}

// Receiver functions
func (p importantPerson) print() {
    fmt.Printf("\n%+v\n", p)
}

// To make receivers that actually modify the passed struct we have to pass by reference
// Go is by default a pass by value languaje which passes a copy instead of the original

// &variable -> give me the memory address of the value this variable is pointing at
// *pointer -> Give me the value this memory address is pointing at
// In the function *type means a type descriptor pointer to a importantPerson.
// In  the body we see the actual operator that gives the value
func (pointerToPerson *importantPerson) updateName(newFirstName string) {
    (*pointerToPerson).firstName = newFirstName
}
