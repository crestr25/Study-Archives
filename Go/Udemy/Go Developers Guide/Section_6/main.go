package main

import (
	"fmt"
    "time"
	"net/http"
)

func main()  {
    links := []string {
        "http://google.com",
        "http://facebook.com",
        "http://stackoverflow.com",
        "http://golang.org",
        "http://amazon.com",
    }

    c := make(chan string)

    for _, link := range links {
        // go will tell to create a new go coroutine
        go checkLink(link, c)
    }
    
    for l := range c {
        // go checkLink(<-c, c)
        // range with a channel once it returns something
        // go checkLink(l, c)

        // Function literal -- Lambda function python
        go func(link string) {
            time.Sleep(5 * time.Second)
            checkLink(link, c)
        }(l)
    }
}

func checkLink(link string, c chan string) {
    _, err := http.Get(link)

    if err != nil {
        fmt.Println(link, "might be down!")
        c <- link
        return
    }
    fmt.Println(link, "is up and running!")
    c <- link

}
