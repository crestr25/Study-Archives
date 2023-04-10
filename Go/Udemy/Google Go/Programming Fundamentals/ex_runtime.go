package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("The runtime OS is", runtime.GOOS)
	fmt.Println("The runtime architecture is", runtime.GOARCH)
}
