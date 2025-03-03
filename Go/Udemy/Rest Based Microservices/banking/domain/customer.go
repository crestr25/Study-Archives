package domain

import (
	"github.com/crestr25/banking/dto"
	"github.com/crestr25/banking/errs"
)

type Customer struct {
	Id          string `db:"customer_id"`
	Name        string
	City        string
	Zipcode     string
	DateofBirth string `db:"date_of_birth"`
	Status      string
}

func (c Customer) statusAsText() string {

    statusAsText := "active"

    if c.Status == "0" {
        statusAsText = "inactive"
    }

    return statusAsText
}

func (c Customer) ToDto() dto.CustomerResponse {

    return dto.CustomerResponse{
        Id: c.Id,
        Name: c.Name,
        City: c.City,
        Zipcode: c.Zipcode,
        DateofBirth: c.DateofBirth,
        Status: c.statusAsText(),
    }
}

// Secondary Port / Server side interface to communicate with any adapter that implements
// the interface.
type CustomerRepository interface {
	// status == 1 | status == 2 | status == ""
	FindAll(status string) ([]Customer, *errs.AppError)
	ById(string) (*Customer, *errs.AppError) // Returns a pointer so we can return a nil if it does not exist
}
