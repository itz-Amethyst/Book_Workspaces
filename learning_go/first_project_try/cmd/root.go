package cmd

import (
	"fmt"
	"digikala/migrations"
	"digikala/apis"
	"github.com/spf13/cobra"
)


// func run(){

// 	myslog := logger.GetLogger()
// 	http.HandleFunc("/", apis.GetRoot)
// 	http.HandleFunc("/create_product", apis.CreateProduct)



// 	db_connection := mydb.ConnectDatabase()
// 	defer db_connection.Close()

// 	// migrations.CreateTables()
// 	myslog.Info("Start Listening to 8000")
// 	serverErr := http.ListenAndServe(":8000", nil)
// 	if serverErr != nil {
// 		myslog.Error("Something is Wrong")
// 	}
// }

func main(){

	var cmdMigrate = &cobra.Command{
		Use:   "migrate",
		Short: "Migrate the models to database",
		Run: func(cmd *cobra.Command, args []string) {
			migrations.RunMigration()
		},
	}

	var cmdRun = &cobra.Command{
		Use:   "run",
		Short: "Run the server",
		Run: func(cmd *cobra.Command, args []string) {
			// run()
			migrations.Setup()
			router := apis.GetRouter()
			if err := router.Start(":8000"); err != nil {
				fmt.Println("Something wrong")
			}
		},
	}

	var rootCmd = &cobra.Command{Use: "app"}
	rootCmd.AddCommand(cmdRun, cmdMigrate)
	rootCmd.Execute()

}