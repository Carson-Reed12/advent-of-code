package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getFileInput(file_name string) string {
	dat, err := os.ReadFile(file_name)
	check(err)

	return string(dat)
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func convertStrToInt(arr []string) []int {
	var int_arr = []int{}

	for _, val := range arr {
		int_val, err := strconv.Atoi(val)
		check(err)

		int_arr = append(int_arr, int_val)
	}

	return int_arr
}

func main() {
	// SETUP
	input_text := getFileInput("day1_input.txt")
	depths := convertStrToInt(strings.Split(input_text, "\n"))

	// PART 1
	inc_count := 0
	for i := 0; i < len(depths)-1; i++ {
		if depths[i] < depths[i+1] {
			inc_count += 1
		}
	}

	fmt.Printf("PART 1 INCREASE COUNT: %d\n", inc_count)

	// PART 2
	// PART 1
	inc_count = 0
	for i := 0; i < len(depths)-3; i++ {
		first_sum := depths[i] + depths[i+1] + depths[i+2]
		second_sum := depths[i+1] + depths[i+2] + depths[i+3]

		if first_sum < second_sum {
			inc_count += 1
		}
	}

	fmt.Printf("PART 2 INCREASE COUNT: %d\n", inc_count)
}
