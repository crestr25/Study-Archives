package service

import (
	"github.com/crestr25/banking/domain"
	"github.com/crestr25/banking/dto"
	"github.com/crestr25/banking/errs"
	"time"
)

type AccountService interface {
	NewAccount(dto.NewAccountRequest) (*dto.NewAccountResponse, *errs.AppError)
	MakeTransaction(dto.NewTransactionRequest) (*dto.NewTransactionResponse, *errs.AppError)
}

type DefaultAccountService struct {
	repo domain.AccountRepository
}

func (s DefaultAccountService) NewAccount(req dto.NewAccountRequest) (*dto.NewAccountResponse, *errs.AppError) {

	err := req.Validate()

	if err != nil {
		return nil, err
	}

	a := domain.Account{
		AccountId:   "",
		CustomerId:  req.CustomerId,
		OpeningDate: time.Now().Format("2006-01-02 15:04:05"),
		AccountType: req.AccountType,
		Amount:      req.Amount,
		Status:      "1",
	}

	newAccount, err := s.repo.Save(a)

	if err != nil {
		return nil, err
	}

	res := newAccount.ToNewAccountResponse()

	return &res, nil
}

func (s DefaultAccountService) MakeTransaction(req dto.NewTransactionRequest) (*dto.NewTransactionResponse, *errs.AppError) {
	err := req.Validate()

	if err != nil {
		return nil, err
	}

	if req.IsTransactionTypeWithdrawal() {
		account, err := s.repo.ById(req.AccountId)

		if err != nil {
			return nil, err
		}

		if !account.CanWithdraw(req.Amount) {
			return nil, errs.NewValidationError("Insufficient balance in the account")
		}

	}

	t := domain.Transaction{
		AccountId:       req.AccountId,
		Amount:          req.Amount,
		TransactionType: req.TransactionType,
		TransactionDate: time.Now().Format("2006-01-02 15:04:05"),
	}
	transaction, err := s.repo.SaveTransaction(t)
	if err != nil {
		return nil, err
	}

    response := transaction.ToDto()

    return &response, nil
}

func NewAccountService(repo domain.AccountRepository) DefaultAccountService {
	return DefaultAccountService{
		repo: repo,
	}

}
