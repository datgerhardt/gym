package main

import "fmt"

func main() {
	// Array
	// <Var | Const> < Name of arr > [<size of arr>] < Datatype of arr >
	// var x [3]int

	// Declare Array and initial with values
	// var x = [3]int{1, 2, 3}

	// sparse array (an array where most elements are set to their zero value)
	var x = [12]int{1, 5: 4, 6, 10: 100, 15}
	fmt.Println(x)

	//
	var y = [...]int{10, 20, 30} // this infe the size from the initialization
	var z = [3]int{10, 20, 30}

	fmt.Println(y == z)

	// len return the size of an arr

	fmt.Println("Size of Array:", len(y))

}
