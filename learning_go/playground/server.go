package main

import (
	"encoding/json"
	"net/http"
	"fmt"
	// "io"
	"log/slog"
	"os"
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

func getRoute(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("Got / requests \n")
	product := Product {
		1,
		"Chain",
		2000,
	}
	response, _ := json.Marshal(product)
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
	
	_ = p
}

func main(){
	myslog.Info("Start Listening to 8000")
	http.HandleFunc("/", getRoute)
	http.HandleFunc("/create_product", createProduct)
	err := http.ListenAndServe(":8000", nil)
	if err != nil {
		myslog.Error("Something went wrong")
}
}