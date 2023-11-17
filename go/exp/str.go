package main

import "fmt"

func main() {

	var s string = "Hello, world"
	var s2 string = s[:3]
	var s3 = s[:2]
	s4 := s3 + " is good"
	fmt.Print(s2, "\n", s3, "\n", s4, "\n")

}
