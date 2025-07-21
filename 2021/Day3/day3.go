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

func initBitmap(bit_length int) map[int]map[int]int {
	var bitmap = make(map[int]map[int]int)
	for i := 0; i < bit_length; i++ {
		bitmap[i] = map[int]int{0: 0, 1: 0}
	}
	return bitmap

}

func constructRates(bitmap map[int]map[int]int, bit_length int) (int64, int64) {
	gamma_rate := ""
	epsilon_rate := ""
	for i := 0; i < bit_length; i++ {
		if bitmap[i][0] > bitmap[i][1] {
			gamma_rate += "0"
			epsilon_rate += "1"
		} else {
			gamma_rate += "1"
			epsilon_rate += "0"
		}
	}

	gamma_rate_decimal, _ := strconv.ParseInt(gamma_rate, 2, 64)
	epsilon_rate_decimal, _ := strconv.ParseInt(epsilon_rate, 2, 64)
	return gamma_rate_decimal, epsilon_rate_decimal
}

func main() {
	// SETUP
	diagnostic_report := strings.Split(getFileInput("day3_input.txt"), "\n")
	bit_length := len(diagnostic_report[0])
	bitmap := initBitmap(bit_length)

	// PART 1
	for _, val := range diagnostic_report {
		for i := 0; i < bit_length; i++ {
			bit_val, _ := strconv.Atoi(string(val[i]))
			bitmap[i][bit_val] += 1
		}
	}

	gamma_rate, epsilon_rate := constructRates(bitmap, bit_length)
	fmt.Printf("PART 1 POWER RATE: %d\n", gamma_rate*epsilon_rate)

	// PART 2

}
