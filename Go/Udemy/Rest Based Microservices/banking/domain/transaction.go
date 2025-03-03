package domain

import (
	"strings"

	"github.com/crestr25/banking/dto"
)

type Transaction struct {
	TransactionId   string
	AccountId       string
	Amount          float64
	TransactionType string
	TransactionDate string
}

func (t Transaction) IsWithdrawal() bool {
    return strings.ToLower(t.TransactionType) == "withdrawal"
}

func (t Transaction) ToDto() dto.NewTransactionResponse {
    return dto.NewTransactionResponse{
        TransactionId: t.TransactionId,
        Amount: t.Amount,
    }

}
