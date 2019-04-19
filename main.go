package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := ioutil.ReadFile("default")
	check(err)

	data := string(dat)
	lines := strings.Split(data, "\n")

	for i := 0; i < len(lines); i++ {
		fmt.Print(lines[i])
		fmt.Print("\n")
	}
}
