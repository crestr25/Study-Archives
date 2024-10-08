package dto

import (
	"strings"

	"github.com/crestr25/banking/errs"
)

type NewAccountRequest struct {
	CustomerId  string  `json:"customer_id"`
	AccountType string  `json:"account_type"`
	Amount      float64 `json:"amount"`
}

func (r NewAccountRequest) Validate() *errs.AppError {

    if r.Amount < 5000 {
        return errs.NewValidationError("To open a new account you need to deposit at least 5000 dolars")
    }

    if strings.ToLower(r.AccountType) != "saving" && strings.ToLower(r.AccountType) != "checking" {
        return errs.NewValidationError("Account must be one of saving or checking")
    }

    return nil

}
