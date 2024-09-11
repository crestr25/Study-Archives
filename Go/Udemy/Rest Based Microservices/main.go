package main

import (
	"github.com/crestr25/banking/app"
	"github.com/crestr25/banking/logger"
)

func main() {
	logger.Info("Starting the application...")
	app.Start()
}
