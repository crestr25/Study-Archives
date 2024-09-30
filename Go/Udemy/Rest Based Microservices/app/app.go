package app

import (
	"fmt"
	"log"
	"net/http"
	"os"
    "time"

	"github.com/crestr25/banking/domain"
	"github.com/crestr25/banking/service"
	"github.com/gorilla/mux"
	"github.com/jmoiron/sqlx"
	"github.com/joho/godotenv"
)

func sanityCheck() {
    if os.Getenv("SERVER_ADDRESS") == "" || os.Getenv("SERVER_PORT") == "" {
        log.Fatal("Environment variable not defined...")
    }

}

func Start() {

    err := godotenv.Load()
	if err != nil {
		log.Fatalf("unable to load .env file: %e", err)
	}

    sanityCheck()

    router := mux.NewRouter()

    // Wiring
    // ch := CustomerHandler{service.NewCustomerService(domain.NewCustomerRepositoryStub())}
    dbClient := getDbClient()
    ch := CustomerHandler{service.NewCustomerService(domain.NewCustomerRepositoryDb(dbClient))}
    ah := AccountHandler{service.NewAccountService(domain.NewAccountRepositoryDb(dbClient))}

    // Define routes
    router.HandleFunc("/customers", ch.getAllCustomers).Methods(http.MethodGet)
    router.HandleFunc("/customers/{customer_id:[0-9]+}", ch.getCustomer).Methods(http.MethodGet)
    router.HandleFunc("/customers/{customer_id:[0-9]+}/account", ah.newAccount).Methods(http.MethodPost)
    router.HandleFunc("/customers/{customer_id:[0-9]+}/account/{account_id:[0-9]+}", ah.makeTransaction).Methods(http.MethodPost)

    // Starting Server
    address := os.Getenv("SERVER_ADDRESS")
    port := os.Getenv("SERVER_PORT")
    log.Fatal(http.ListenAndServe(fmt.Sprintf("%s:%s", address, port), router))
}

func getDbClient() *sqlx.DB {
    dbUser := os.Getenv("DB_USER")
    dbPasswd := os.Getenv("DB_PASSWD")
    dbAddr := os.Getenv("DB_ADDR")
    dbPort := os.Getenv("DB_PORT")
    dbName := os.Getenv("DB_NAME")

    dataSource := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s", dbUser, dbPasswd, dbAddr, dbPort, dbName)
	client, err := sqlx.Open("mysql", dataSource)

	if err != nil {
		panic(err)
	}

	//Important settings
	client.SetConnMaxLifetime(time.Minute * 3)
	client.SetMaxOpenConns(10)
	client.SetMaxIdleConns(10)

    return client
}
