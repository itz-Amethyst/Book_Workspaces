package main

import (
	"fmt"
)

func sum(s []int , c chan int) {
	sum := 0

	for _, v := range s {
		sum += v
	}

	c <- sum
}

func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func main(){

	s := []int {2, 5, 1, 0, 2, -4, -5}

	c := make(chan int)
	ch := make(chan int, 10)

	go fibonacci(cap(c), c)
	for i := 0; i < 20; i++ {
		v, ok := <- c
		fmt.Println(v, ok, i)
	}

	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)

	x, y := <-c, <-c //receive from channel

	fmt.Println(x, y , x+y)
}