package dto

import (
	"strings"

	"github.com/crestr25/banking/errs"
)

type NewTransactionRequest struct {
    CustomerId      string  `json:"-"`
	AccountId       string  `json:"account_id"`
	TransactionType string  `json:"transaction_type"`
	Amount          float64 `json:"amount"`
}

func (r NewTransactionRequest) IsTransactionTypeWithdrawal() bool {
    return strings.ToLower(r.TransactionType) == "withdrawal"
}

func (r NewTransactionRequest) Validate() *errs.AppError {
    if r.Amount < 0 {
        return errs.NewValidationError("Amount can not be negative")
    }
    
    if strings.ToLower(r.TransactionType) != "withdrawal" && strings.ToLower(r.TransactionType) != "deposit" {
        return errs.NewValidationError("Type must be withdrawal or deposit")
    }


    return nil
}
