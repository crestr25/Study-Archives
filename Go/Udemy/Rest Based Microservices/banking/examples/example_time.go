package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strings"
	"time"

	"github.com/gorilla/mux"
)

func main() {
	app()
}

func app() {
	// Create multiplexer with mux library
	router := mux.NewRouter()

	// define routes
	router.HandleFunc("/api/time", getTime).Methods(http.MethodGet)

	// Start server
	log.Fatal(http.ListenAndServe("localhost:8080", router))

}

func getTime(w http.ResponseWriter, r *http.Request) {

	// get the timezone if exists
	tz := r.URL.Query().Get("tz")

	var current_time time.Time
    res := make(map[string]interface{})

	if tz != "" {
		tzs := strings.Split(tz, ",")
	    fmt.Println(tzs)
		for _, timezone := range tzs {
			loc, err := time.LoadLocation(timezone)
			if err != nil {
				w.WriteHeader(404)
				return
			}
			current_time = time.Now().In(loc)
			res[timezone] = current_time.String()
		}
	} else {
		current_time = time.Now().UTC()
		res["current_time"] = current_time.String()
	}
	w.Header().Add("Content-Type", "application/json")
	json.NewEncoder(w).Encode(res)
}


func getTime2(w http.ResponseWriter, r *http.Request) {
    response := make(map[string]string, 0)
    tz := r.URL.Query().Get("tz")
    timezones := strings.Split(tz, ",")

    if len(timezones) <= 1 {
        loc, err := time.LoadLocation(tz)
        if err != nil {
            w.WriteHeader(http.StatusNotFound)
            w.Write([]byte(fmt.Sprintf("invalid timezone %s", tz)))
        } else {
            response["current_time"] = time.Now().In(loc).String()
            w.Header().Add("Content-Type", "application/json")
            json.NewEncoder(w).Encode(response)
        }
     } else {
        for _, tzdb := range timezones {
            loc, err := time.LoadLocation(tzdb)
            if err != nil {
                w.WriteHeader(http.StatusNotFound)
                w.Write([]byte(fmt.Sprintf("invalid timezone %s in input", tzdb)))
                return
             }
             now := time.Now().In(loc)
             response[tzdb] = now.String()
        }
        w.Header().Add("Content-Type", "application/json")
        json.NewEncoder(w).Encode(response)
     }
}
