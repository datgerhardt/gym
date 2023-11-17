package main

import "fmt"

func main() {
	var x int = 10
	var y float64 = 30.2
	z := float64(x) + y
	var d int = int(z)
	fmt.Println(x, y, z, d)
}
