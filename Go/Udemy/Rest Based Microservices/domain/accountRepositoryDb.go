package domain

import (
	"database/sql"
	"strconv"

	"github.com/crestr25/banking/errs"
	"github.com/crestr25/banking/logger"
	"github.com/jmoiron/sqlx"
)

type AccountRepositoryDb struct {
	client *sqlx.DB
}


func (d AccountRepositoryDb) ById(id string) (*Account, *errs.AppError) {

	accountSql := "select account_id, customer_id, opening_date, account_type, amount from accounts where account_Id = ?"

	var account Account

	err := d.client.Get(&account, accountSql, id)

	if err != nil {
		logger.Error("Error scanning rows")
		if err == sql.ErrNoRows {
			return nil, errs.NewNotFoundError("Account not found")
		} else {
			return nil, errs.NewUnexpectedError("Unexpected Database error")
		}
	}

	return &account, nil

}

func (d AccountRepositoryDb) Save(a Account) (*Account, *errs.AppError) {
	sqlInsert := "INSERT INTO accounts (customer_id, opening_date, account_type, amount, status) VALUES (?, ?, ?, ?, ?)"

	result, err := d.client.Exec(sqlInsert, a.CustomerId, a.OpeningDate, a.AccountType, a.Amount, a.Status)

	if err != nil {
		logger.Error("Error while creating new account: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

	id, err := result.LastInsertId()

	if err != nil {
		logger.Error("Error while getting last insert id for new account: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

	a.AccountId = strconv.FormatInt(id, 10)

	return &a, nil

}

func (d AccountRepositoryDb) SaveTransaction(t Transaction) (*Transaction, *errs.AppError) {

    tx, err := d.client.Begin()
	if err != nil {
		logger.Error("Error while starting the transaction: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

	transactionInsert := "INSERT INTO transactions (account_id, amount, transaction_type, transaction_date) VALUES (?, ?, ?, ?)"

	result, err := d.client.Exec(transactionInsert, t.AccountId, t.Amount, t.TransactionType, t.TransactionDate)

	if err != nil {
		logger.Error("Error while creating new transaction: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

    if t.IsWithdrawal() {
        _, err = d.client.Exec("UPDATE transactions SET amount = amount - ? WHERE account_id = ?", t.Amount, t.AccountId)
    } else {
        _, err = d.client.Exec("UPDATE transactions SET amount = amount + ? WHERE account_id = ?", t.Amount, t.AccountId)
    }

	if err != nil {
        tx.Rollback()
		logger.Error("Error while updating account amount for account: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

    err = tx.Commit()

	if err != nil {
        tx.Rollback()
		logger.Error("Error while commiting transaction for account: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

    transactionId, err := result.LastInsertId()

	if err != nil {
		logger.Error("Error while getting last transaction id: " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected error from db")
	}

	t.TransactionId = strconv.FormatInt(transactionId, 10)

	return &t, nil

}

func NewAccountRepositoryDb(dbClient *sqlx.DB) AccountRepositoryDb {
    return AccountRepositoryDb{ client: dbClient }
}
