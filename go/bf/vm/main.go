package main

import (
	"fmt"
	"os"
)

func main() {
	fileName := os.Args[1]
	code, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", err)
		os.Exit(-1)
	}

	compiler := NewCompiler(string(code))
	instructions := compiler.Compile()

	m := NewMachine(instructions, os.Stdin, os.Stdout)
	m.Execute()
}
