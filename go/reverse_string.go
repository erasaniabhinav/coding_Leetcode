//input: hello
//output: olleh

package main

import "fmt"

func reverseString(s string) string {
	reversed := ""
	for i := len(s) - 1; i >= 0; i-- {
		reversed += string(s[i])
	}
	return reversed
}

func main() {
	str := "hello"
	fmt.Println("Original string:", str)
	fmt.Println("Reversed string:", reverseString(str))
}
