package main

import "fmt"

func main() {
	// Slice
	//
	// var x = []int{1, 5: 4, 6, 10: 100, 15}
	// fmt.Println(x)

	// // Append
	// var y = []int{1, 2, 3}
	// y = append(y, 4)
	// y = append(y, 5, 6, 7, 8, 9, 10)
	// fmt.Println(y)

	// var z = append(x, y...) // ... spreed operator
	// fmt.Println("z:", z)

	// Difference b/n len and cap
	// var x []int
	// fmt.Println(x, len(x), cap(x))
	// x = append(x, 10)
	// fmt.Println(x, len(x), cap(x))
	// x = append(x, 20)
	// fmt.Println(x, len(x), cap(x))
	// x = append(x, 30)
	// fmt.Println(x, len(x), cap(x))
	// x = append(x, 40)
	// fmt.Println(x, len(x), cap(x))
	// x = append(x, 50)
	// fmt.Println(x, len(x), cap(x))

	// y := make([]int, 5, 10)
	// fmt.Println(y, len(y), cap(y))

	// Using make to create a slice with 0 len size
	// x := make([]int, 0, 5)
	// x = append(x, 1, 2, 3, 4)
	// y := x[:2]
	// z := x[2:]
	// fmt.Println(cap(x), cap(y), cap(z))
	// y = append(y, 30, 40, 50)
	// x = append(x, 60)
	// z = append(z, 70)
	// fmt.Println("x:", x)
	// fmt.Println("y:", y)
	// fmt.Println("z:", z)

	// Converting an array into slice
	// x := [4]int{1, 2, 3, 4}
	// y := x[:2]
	// z := x[2:]

	// // y = append(y, 6)
	// fmt.Println("x:", x)
	// fmt.Println("y:", y)
	// fmt.Println("z:", z)

	// copy If you need to create a slice that’s independent of the original
	x := []int{1, 2, 3, 4}
	y := make([]int, 4)
	// num := copy(y, x)
	copy(y, x)
	fmt.Println(y)

}
