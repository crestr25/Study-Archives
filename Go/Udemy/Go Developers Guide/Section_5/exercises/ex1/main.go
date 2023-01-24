package main

import "fmt"

type shape interface {
    area() float64
}

type triangle struct{
    height float64
    base float64
}
type square struct{
    sideLength float64
}


func main() {
    t := triangle{height: 2, base: 3}
    s := square{sideLength: 3}

    printArea(t)
    printArea(s)
}

func printArea(s shape) {
    area := s.area()
    fmt.Println(area)
}

func (s square) area() (float64) {
    return 2 * s.sideLength
}

func (t triangle) area() (float64) {
    return 0.5 * t.base * t.height
}
