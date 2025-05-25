package main

import "fmt"

func main() {
	// var nilMap map[string]int
	totalWins := map[string]int{}

	// teams := map[string][]string {
	// 	"orca": []string{"Fred", "Raplh"},
	// }
	totalWins["Orcas"] = 1
	totalWins["Loins"] = 2

	m := map[string]int{
		"Hello": 1,
		"World": 2,
	}
	v, ok := m["Hello"]
	fmt.Println(v, ok)

	v, ok = m["goodbye"]
	fmt.Println(v, ok)

	// Delete item from map
	delete(m, "Hello")

	v, ok = m["Hello"]
	fmt.Println(v, ok)
}
