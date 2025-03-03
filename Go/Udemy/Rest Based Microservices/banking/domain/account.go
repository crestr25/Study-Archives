package domain

import (
	"github.com/crestr25/banking/dto"
	"github.com/crestr25/banking/errs"
)

type Account struct {
    AccountId   string `db:"account_id"`
    CustomerId  string `db:"customer_id"`
    OpeningDate string `db:"opening_date"`
    AccountType string `db:"account_type"`
    Amount      float64 `db:"amount"`
    Status      string `db:"status"`
}

func (a Account) ToNewAccountResponse() dto.NewAccountResponse {
	return dto.NewAccountResponse{
		AccountId: a.AccountId,
	}

}

func (a Account) CanWithdraw(amount float64) bool {
    return a.Amount >= amount
}

type AccountRepository interface {
	Save(Account) (*Account, *errs.AppError)
    ById(string) (*Account, *errs.AppError)
    SaveTransaction(Transaction) (*Transaction, *errs.AppError)
}
