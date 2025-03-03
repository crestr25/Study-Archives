package app

import (
	"encoding/json"
	"net/http"

	"github.com/crestr25/banking/service"
	"github.com/gorilla/mux"
)

type CustomerHandler struct {
	service service.CustomerService
}

func (ch *CustomerHandler) getAllCustomers(w http.ResponseWriter, r *http.Request) {

    status := r.URL.Query().Get("status")

	customers, err := ch.service.GetAllCustomer(status)


	if err != nil {
		writeResponse(w, err.Code, err.AsMessage())
	} else {
		writeResponse(w, http.StatusOK, customers)
	}

}

func (ch *CustomerHandler) getCustomer(w http.ResponseWriter, r *http.Request) {

	vars := mux.Vars(r)

	customer_id := vars["customer_id"]

	customer, err := ch.service.GetCustomer(customer_id)

	if err != nil {
		// fmt.Fprintf(w, err.Message) it is better to encode in json as all other responses are the same
		writeResponse(w, err.Code, err.AsMessage())
	} else {
		writeResponse(w, http.StatusOK, customer)
	}

}

func writeResponse(w http.ResponseWriter, code int, data interface{}) {
	// content type should ALWAYS come FIRST
	w.Header().Add("Content-Type", "application/json")
	w.WriteHeader(code)
	err := json.NewEncoder(w).Encode(data)

	if err != nil {
		panic(err)
	}
}
