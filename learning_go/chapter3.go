package main

import (
	"fmt"
	"slices"
)

func main(){
	// var x = []int{2, 5, 6, 7}
	// another version 
	x := make([]int, 0)
	copy(x, []int {2, 5, 6, 7})

	
	var y = []int{2, 5, 6, 7}
	var b = [3]int {1, 3 ,5}
	result := make([]int , 2) // only 2!
	copy(result, b[:]) // [:] sliced version of b

	var useCase = []int {2, 4 , 6 , 8}
	var i = []int{1, 5:4, 7:10,8,100}
	// x[0] = 10

	fmt.Println(x)
	fmt.Println(i)
	fmt.Println(slices.Equal(x,y))

	useCase = append(useCase, 10)

	combined := append(useCase, i...) 
	fmt.Println(useCase)
	fmt.Println(combined)
	fmt.Println(result)

	// ------------------------

	// rune type is good for emojy strings
	var s string = "Hello world"

	s1 := s[:6]
	s2 := s[6:]
	fmt.Println(s1, s2)

	// 0 value is nil
	// test_map := make(map[int]string, 10)


	m := map[string]int {
		"hello": 4,
		"world": 6,
	}

	m["test"] = 10
	delete(m, "test")
	// clear(m)
	//! Important Note here: we declared v,ok once so if we use := for the second appraoch it will face and error so neither can have 2 values with same name
	v, ok := m["apex"]
	if !ok {
		fmt.Println("We dont have apex")
	}
	v, ok = m["world"]
	if ok{
		fmt.Println(v)
	}

	// -----------------

	inSet := map[int]bool{}
	vals := []int{2, 4, 6, 8, 10}
	for _, v := range vals{
		inSet[v] = true
	}

	fmt.Println(len(vals), len(inSet))
	fmt.Println(inSet[5]) // False we dont have 5 in map
	fmt.Println(inSet)
	// -------------------
	type house struct {
		adderess string
		area int
	}

	tehran := house{
		"IRAN TEHRAN",
		250,
	}

	anonymous := struct{
		name string
		age int
	}{
		"SOMETHING",
		22,
	}


	fmt.Println(anonymous)
	fmt.Println(tehran)
}