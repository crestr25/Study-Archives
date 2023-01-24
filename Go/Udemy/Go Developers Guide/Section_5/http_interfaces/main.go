package main

import (
	"fmt"
	"net/http"
	"os"
    "io"
)

type logWriter struct{}

func main() {
    resp, err := http.Get("http://google.com")
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(1)
    }
    lg := logWriter{}
    io.Copy(lg, resp.Body)

    // copy to send from a reader interface to a writer
    // io.Copy(os.Stdout, resp.Body)
    // bs := make([]byte, 99999)// need to create with some empty values
    // resp.Body.Read(bs)
    // fmt.Println(string(bs))
}

func (logWriter) Write(bs []byte) (int, error){
    // here the logWriter struct is implementing the Writer interface since it has a 
    // Write function now
    fmt.Println(string(bs))
    fmt.Println("Just wrote this many Bytes: ", len(bs))
    return len(bs), nil
}
