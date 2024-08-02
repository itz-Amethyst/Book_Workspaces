package apis

import (
	"net/http"

	"digikala/configs"
	"digikala/models"

	"github.com/labstack/echo/v4"
)

func listBrand(c echo.Context) error {
	DB := configs.DB
	var brands []models.Brand
	if err := DB.Find(&brands).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
	}
	return c.JSON(http.StatusAccepted, brands)
}

func createBrand(c echo.Context) error {

	DB := configs.DB
	var brand models.Brand
	err := c.Bind(&brand)
	if err != nil{
		return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
	}
	if err := DB.Create(&brand).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
	}
	return c.JSON(http.StatusAccepted, brand)
}