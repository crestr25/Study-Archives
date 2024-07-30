package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"net/http"
    "log"
    "github.com/gorilla/mux"
)

type Customer struct {
    Name    string `json:"full_name" xml:"full_name"`
    City    string `json:"city" xml:"city"`
    Zipcode string `json:"zip_code" xml:"zip_code"`
}

func main2() {
    muxMain()
}

func muxMain() {

    // create multiplexer with mux library
    router := mux.NewRouter()

    // define routes
	router.HandleFunc("/greet", greet).Methods(http.MethodGet) // specify which methods can be processed
	router.HandleFunc("/customers", getAllCustomers)
    router.HandleFunc("/customers/{customer_id:[0-9]+}", getCustomer) // regex passed to verify it is an int

    // starting server
    //log.Fatal(http.ListenAndServe("localhost:8080", nil)) // the nil value is to specify the default multiplexer
    log.Fatal(http.ListenAndServe("localhost:8080", router)) // the nil value is to specify the default multiplexer
}

func httpMain() {

    // create multiplexer with builtin http
    mux := http.NewServeMux()

    // define routes
	mux.HandleFunc("/greet", greet)
	mux.HandleFunc("/customers", getAllCustomers)

    // starting server
    //log.Fatal(http.ListenAndServe("localhost:8080", nil)) // the nil value is to specify the default multiplexer
    log.Fatal(http.ListenAndServe("localhost:8080", mux)) // the nil value is to specify the default multiplexer
}

func getCustomer(w http.ResponseWriter, r *http.Request) {
	// the w is the response writer which is sent back to the user.
	// the r is the request info parameters that are received in the request

    // Get the variables
    vars := mux.Vars(r)

	fmt.Fprint(w, vars["customer_id"])

}

func greet(w http.ResponseWriter, r *http.Request) {
	// the w is the response writer which is sent back to the user.
	// the r is the request info parameters that are received in the request
	fmt.Fprint(w, "hello world!!")
}


func getAllCustomers(w http.ResponseWriter, r *http.Request) {
	// the w is the response writer which is sent back to the user.
	// the r is the request info parameters that are received in the request
    customers := []Customer{
        {Name:"Carlos", City: "Medellin", Zipcode: "2100"},
        {Name:"Luisa", City: "Madrid", Zipcode: "420"},
        {Name:"Ferxxo", City: "Metrallo", Zipcode: "69"},
    }
    // we need to add the type of the response as json
    //w.Header().Add("Content-Type", "application/json")

    // we can send the content-type from the request to specify the type we want as response
    if r.Header.Get("Content-Type") == "application/json" {
        w.Header().Add("Content-Type", "application/json")
        json.NewEncoder(w).Encode(customers)
    } else if r.Header.Get("Content-Type") == "application/xml" {
        w.Header().Add("Content-Type", "application/xml")
        xml.NewEncoder(w).Encode(customers)
    }
    fmt.Fprint(w)
}
