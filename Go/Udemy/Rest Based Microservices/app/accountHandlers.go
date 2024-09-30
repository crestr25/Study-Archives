package app

import (
	"encoding/json"
	"net/http"

	"github.com/crestr25/banking/dto"
	"github.com/crestr25/banking/service"
	"github.com/gorilla/mux"
)

type AccountHandler struct {
	service service.AccountService
}

func (ah *AccountHandler) newAccount(w http.ResponseWriter, r *http.Request) {

	var request dto.NewAccountRequest
    vars := mux.Vars(r)

	err := json.NewDecoder(r.Body).Decode(&request)

	if err != nil {
		writeResponse(w, http.StatusBadRequest, err.Error())
	} else {
        request.CustomerId = vars["customer_id"]
		newAccount, err := ah.service.NewAccount(request)

		if err != nil {
			writeResponse(w, err.Code, err.AsMessage())

		} else {
			writeResponse(w, http.StatusCreated, newAccount)
		}

	}
}


func (ah *AccountHandler) makeTransaction(w http.ResponseWriter, r *http.Request) {

    vars := mux.Vars(r)
    customerId := vars["customer_id"]
    accountId := vars["account_id"]

    var request dto.NewTransactionRequest

    if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		writeResponse(w, http.StatusBadRequest, err.Error())
    } else {
        request.AccountId = accountId
        request.CustomerId = customerId

        account, err := ah.service.MakeTransaction(request)

		if err != nil {
			writeResponse(w, err.Code, err.AsMessage())

		} else {
			writeResponse(w, http.StatusOK, account)
		}
    }

}
