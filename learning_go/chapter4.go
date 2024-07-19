package main

import (
	"fmt"
	"math/rand"
)

func main(){
	n := rand.Intn(20)

	if n == 0 {
		fmt.Println("0 mentioned")
	} else if n > 10 {
		fmt.Println("higher than 10 mentioned")
	} else {
		fmt.Println("Something else")
	}

	for i := 0; i <= 10; i++{
		fmt.Println(i)
	}

	vals := []int {1, 3 , 5 , 7}
	// i can be ignored by _
	for i, v := range vals {
		fmt.Println(i, v)
	}

	m := map[string]bool{
		"a": true,
		"b": true,
		"c": false,
	}

	for i := 1; i <= 3; i++{
		fmt.Println("Loop", i)
		for k, v := range m {
			// Different answers!
			fmt.Println(k,v)
		}
	}


	samples := []string {"hello", "world"}

	for _,v := range smaples{
		for i,v := range v {
			fmt.Println(i, string(v))
		}
	}

	for i, v := range vals {
		vals[i] = v * 2	
	}
	fmt.Println(vals)

	out_scope:	
		for _, sample := range samples{
			for i, v := range sample {
				fmt.Println(i, string(v))
				if v == 'w' {
					continue out_scope
				}
			}
			fmt.Println()
		}

	for i:=0; i < 10; i++ {
		switch i {
		case 0, 2 ,4:
			fmt.Println(i, "it's even")
		case 1, 3 ,5 :
			fmt.Println(i, "it's odd")
		default:
			fmt.Println(i, "No Idea!")
			break
		}
	}

	for i := 1; i <=100; i++{
		switch {
		case i % 3 == 0 && i % 5 == 0:
			fmt.Println("FizzBuzz")
		case i % 3 == 0:
			fmt.Println("Fizz")
		case i % 5 == 0:
			fmt.Println("Buzz")
		default:
			continue
		}
	}

	something(20, 50)
}

func something(a, b int) {
	for i := 0; i < a; i++ {
		fmt.Println("SOMETING")

		switch i {
		case 5:
			goto another_mode
		}
	}


	another_mode:
		for y := 0; i < b; i++ {

			fmt.Println("something in b")
		}
}
