package service

import (
	"github.com/crestr25/banking/domain"
	"github.com/crestr25/banking/dto"
	"github.com/crestr25/banking/errs"
)

type CustomerService interface {
	GetAllCustomer(status string) ([]dto.CustomerResponse, *errs.AppError)
	GetCustomer(string) (*dto.CustomerResponse, *errs.AppError)
}

type DefaultCustomerService struct {
	repo domain.CustomerRepository
}

func (s DefaultCustomerService) GetAllCustomer(status string) ([]dto.CustomerResponse, *errs.AppError) {

	if status == "active" {
		status = "1"
	} else if status == "inactive" {
		status = "0"
	} else {
		status = ""
	}
	c, err := s.repo.FindAll(status)

	if err != nil {
		return nil, err
	}

	var response []dto.CustomerResponse

	for _, customer := range c {

		dtoCustomer := customer.ToDto()
		response = append(response, dtoCustomer)
	}

	return response, nil

}

func (s DefaultCustomerService) GetCustomer(id string) (*dto.CustomerResponse, *errs.AppError) {

	c, err := s.repo.ById(id)

	if err != nil {
		return nil, err
	}

	response := c.ToDto()

	return &response, nil

}

func NewCustomerService(repository domain.CustomerRepository) DefaultCustomerService {
	return DefaultCustomerService{repo: repository}
}
