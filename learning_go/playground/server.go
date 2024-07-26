package main

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"fmt"
	// "io"
	"log/slog"
	"os"

	"github.com/lib/pg"
)

const (
	host = "localhost"
	port = 5432
	user = "someone"
	dbname = "test"
	password = "1234"
)

type Product struct {
	Id int `json:"id"`
	Title string `json:"title"`
	Price int `json:"price"`
}

var generalProduct *Product = &Product{
	2,
	"TeST",
	15000,
}

var jsonHandler *slog.JSONHandler = slog.NewJSONHandler(os.Stderr, nil)
var myslog *slog.Logger = slog.New(jsonHandler)
var globalDatabase *sql.DB

func createTables(){
	rows, err := globalDatabase.Query(`create table if not exists Products(
		id INT PRIMARY KEY,
		title TEXT,
		price INT
	)`)
	if err != nil {
		myslog.Error(err.Error()))
	}
	fmt.Println(rows)
}

func getRoute(w http.ResponseWriter, r *http.Request) {
	var (
		id int
		title string
		price int
	)
	// fmt.Printf("Got / requests \n")
	product := Product {
		1,
		"Chain",
		2000,
	}

	rows, err := globalDatabase.Query(`select * from Products`)
	if err != nil {
		myslog.Error(err.Error())
	}
	defer rows.Close()

	for rows.Next() {
		err := rows.Scan(&id, &title, &price)
		if err != nil {
			myslog.Error(err.Error())
		}
		fmt.Prinln(id, title, price)
	}
	fmt.Println(rows)
	response, _ := json.Marshal(Product{Id: id, Title: title, Price: price})
	w.Header().Set("Content-Type", "application/json")
	w.Write(response)
	products := []Product{*generalProduct}
	productResponse, _ := json.Marshal(products)
	w.Write(productResponse)
	// io.WriteString(response)
}

func createProduct(w http.ResponseWriter, r *http.Request) {

	body := json.NewDecoder(r.Body)
	p := &Product{}
	err := body.Decode(p)
	if err != nil {
		http.Error(w, err.Error(), 500)
	}
	
	rows, err := globalDatabase.Query(`insert into Products (id, title, price) values ($1, $2, $3)`, p.Id, p.Title, p.Price)
	if err != nil {
		myslog.Error(err.Error())
	}
	fmt.Println(rows)
}

func main(){
	myslog.Info("Start Listening to 8000")
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s" + "password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)
	http.HandleFunc("/", getRoute)
	http.HandleFunc("/create_product", createProduct)

	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}
	defer db.close()
	err = db.Ping()
	if err != nil {
		panic(err)
	}
	globalDatabase = db
	myslog.Info("Start creating tables process")
	createTables()
	err := http.ListenAndServe(":8000", nil)
	if err != nil {
		myslog.Error("Something went wrong")
}
}