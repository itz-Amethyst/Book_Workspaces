package migrations

import (
	"fmt"
	"digikala/logger"
	_ "digikala/mydb"
	_ "github.com/lib/pq"
	"digikala/configs"
	"digikala/models"
)
func Setup(){

	myslog := logger.GetLogger()
	config2, err := configs.LoadConfig(".")
	if err != nil {
		myslog.Error("Could not find the env")
	}

	configs.ConnectDb(&config2)
}

func RunMigration(){
	Setup()
	configs.DB.AutoMigrate(&models.Product{}, & models.Brand{})
	fmt.Println("Successfully migrated")
}

// func CreateTables(){

// 	globalDatabase := mydb.ConnectDatabase()
// 	myslog := logger.GetLogger()

// 	myslog.Info("create tables")
// 	rows, err := globalDatabase.Query(`create table if not exists Product (
//   id INT PRIMARY KEY,
//   title TEXT,
//   price INT
// )`)
// 	if err != nil {
// 		myslog.Error(err.Error())
// 	}
// 	fmt.Println(rows)
// }