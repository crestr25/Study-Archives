package domain

import (
	"database/sql"
	"fmt"
	"os"
	"time"

	"github.com/crestr25/banking/errs"
	"github.com/crestr25/banking/logger"
	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
)

type CustomerRepositoryDb struct {
	client *sqlx.DB
}

func (d CustomerRepositoryDb) FindAll(status string) ([]Customer, *errs.AppError) {

	findAllsql := "select customer_id, name, city, zipcode, date_of_birth, status from customers"

	var err error

	customers := make([]Customer, 0)

	if status != "" {
		findAllsql = findAllsql + " where status = ?"
		err = d.client.Select(&customers, findAllsql, status)
	} else {

		err = d.client.Select(&customers, findAllsql)
	}

	if err != nil {
		logger.Error("Error executing query " + err.Error())
		return nil, errs.NewUnexpectedError("Unexpected Database error")
	}

	return customers, nil
}

func (d CustomerRepositoryDb) ById(id string) (*Customer, *errs.AppError) {

	customerSql := "select customer_id, name, city, zipcode, date_of_birth, status from customers where customer_id = ?"

	var customer Customer

	err := d.client.Get(&customer, customerSql, id)

	if err != nil {
		logger.Error("Error scanning rows")
		if err == sql.ErrNoRows {
			return nil, errs.NewNotFoundError("Customer not found")
		} else {
			return nil, errs.NewUnexpectedError("Unexpected Database error")
		}
	}

	return &customer, nil

}

func NewCustomerRepositoryDb(dbClient *sqlx.DB) CustomerRepositoryDb {
	return CustomerRepositoryDb{dbClient}
}
