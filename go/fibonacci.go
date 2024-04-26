//input:10
//output:series up to 10 terms

package main

import "fmt"

func fibonacci(n int) []int {
	fib := make([]int, n)
	fib[0], fib[1] = 0, 1
	for i := 2; i < n; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}
	return fib
}

func main() {
	n := 10
	fmt.Println("Fibonacci series up to", n, "terms:", fibonacci(n))
}
