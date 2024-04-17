//input: 17
//o/p:prime or not

package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	num := 17
	if isPrime(num) {
		fmt.Println(num, "is prime")
	} else {
		fmt.Println(num, "is not prime")
	}
}
