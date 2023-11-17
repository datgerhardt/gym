package main

import (
	"fmt"
	"math/cmplx"
)

func main() {
	x := complex(2.5, 3.1)
	y := complex(10.2, 2)

	fmt.Println(x + y)
	fmt.Println(x - y)
	fmt.Println(x * y)
	fmt.Println(x / y)
	fmt.Println(real(x))      // Get the real number part of complex number
	fmt.Println(imag(x))      // Get the imaginary number part of complex number
	fmt.Println(cmplx.Abs(x)) // Return absolute value of the cmplx num
}
