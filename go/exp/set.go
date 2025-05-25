package main

import "fmt"

func main() {
	intSet := map[int]bool{}
	vals := []int{5, 10, 2, 5, 8, 7, 3, 9, 1, 2, 10}

	for _, val := range vals {
		intSet[val] = true
	}

	fmt.Println(len(intSet), len(vals))
	fmt.Println(intSet[5])
	if intSet[100] {
		fmt.Println("100 is in set")
	}

}
