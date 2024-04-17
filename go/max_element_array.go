//input: {5, 7, 2, 10, 8}
//o/p: 10

package main

import "fmt"

func findMax(arr []int) int {
	max := arr[0]
	for _, num := range arr {
		if num > max {
			max = num
		}
	}
	return max
}

func main() {
	numbers := []int{5, 7, 2, 10, 8}
	fmt.Println("Maximum element in the array:", findMax(numbers))
}
