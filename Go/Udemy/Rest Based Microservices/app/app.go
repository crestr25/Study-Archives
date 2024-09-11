package app

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/crestr25/banking/domain"
	"github.com/crestr25/banking/service"
	"github.com/gorilla/mux"
)

func sanityCheck() {
    if os.Getenv("SERVER_ADDRESS") == "" || os.Getenv("SERVER_PORT") == "" {
        log.Fatal("Environment variable not defined...")
    }

}

func Start() {

    sanityCheck()

    router := mux.NewRouter()

    // Wiring
    // ch := CustomerHandler{service.NewCustomerService(domain.NewCustomerRepositoryStub())}
    ch := CustomerHandler{service.NewCustomerService(domain.NewCustomerRepositoryDb())}

    // Define routes
    router.HandleFunc("/customers", ch.getAllCustomers).Methods(http.MethodGet)
    router.HandleFunc("/customers/{customer_id:[0-9]+}", ch.getCustomer).Methods(http.MethodGet)

    // Starting Server
    address := os.Getenv("SERVER_ADDRESS")
    port := os.Getenv("SERVER_PORT")
    log.Fatal(http.ListenAndServe(fmt.Sprintf("%s:%s", address, port), router))
}
