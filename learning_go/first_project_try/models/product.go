package models

import (
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Id    int    `gorm:"primary_key" json:"id"`
	Title string `json:"title"`
	Price int    `json:"price"`
	BrandId int `json:"brand_id"`
	CategoryId int `json:"category_id"`
	Category Category `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
	Brand Brand `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
	DiscountPercentage float32 `json:"discount_percentage"`
	DiscountedPrice int `json:"discounted_price"`
}

type Brand struct {
	gorm.Model
	Id    int    `json:"id"`
	Title string `json:"title"`
}

type Category struct {
	gorm.Model
	Id     int    `json:"id"`
	Title  string `json:"title"`
	Parent int    `json:"Parent"`
}
