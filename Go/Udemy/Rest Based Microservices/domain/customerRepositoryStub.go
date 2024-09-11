package domain

// Stub struct with receiver function that satisfies the interface
type CustomerRepositoryStub struct {
	customers []Customer
}

func (s CustomerRepositoryStub) FindAll() ([]Customer, error) {
	return s.customers, nil
}

func NewCustomerRepositoryStub() CustomerRepositoryStub {
	customers := []Customer{
		{
			Id:          "1",
			Name:        "Carlos",
			City:        "Medellin",
			Zipcode:     "050021",
			DateofBirth: "26-06-1993",
			Status:      "1",
		},
		{
			Id:          "2",
			Name:        "Luisa",
			City:        "Madrid",
			Zipcode:     "00000",
			DateofBirth: "11-09-1997",
			Status:      "1",
		},
	}

	return CustomerRepositoryStub{customers: customers}
}
