package domain

import "github.com/crestr25/banking/errs"

type Account struct {
	AccountId   string
	CustomerId  string
	OpeningDate string
	AccountType string
	Amount      string
	Status      string
}

type AccountRepository interface {
    Save(Account) (*Account, *errs.AppError)
}
