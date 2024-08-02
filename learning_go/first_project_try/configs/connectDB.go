package configs

import (
	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"digikala/logger"
)

var DB *gorm.DB

func ConnectDb(config *Config) {
	var err error
	log := logger.GetLogger()
	cnn_string := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=disable", config.DBHost, config.DBUserName, config.DBUserPassword, config.DBName, config.DBPort)

	DB, err = gorm.Open(postgres.Open(cnn_string), &gorm.Config{})
	if err != nil {
		log.fatal("Failed to connect to db")
	}

	fmt.Println("Successfully connected to db")
}
