//input: 5,10
//output: 10,5

package main

import "fmt"

func main() {
	a, b := 5, 10
	fmt.Println("Before swapping: a =", a, ", b =", b)
	a, b = b, a
	fmt.Println("After swapping: a =", a, ", b =", b)
}
