package apis

import (

	"github.com/labstack/echo/v4"
)

func main(){

}

func GetRouter() *echo.Echo{
	e := echo.New()

	brandRouter := e.Group("/brands")
	brandRouter.GET("", listBrand)
	// brandRouter.GET(":id", getBrand)
	brandRouter.POST("", createBrand)
	// brandRouter.PUT(":id", updateBrand)
	// brandRouter.DELETE(":id", deleteBrand)
	return e
}