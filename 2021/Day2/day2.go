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

type Sub_Funcs interface {
	move_horizontal()
	move_depth()
}

type Submarine struct {
	horizontal int
	depth      int
	aim        int
	Sub_Funcs
}

func (sub *Submarine) init_sub() {
	sub.horizontal = 0
	sub.depth = 0
	sub.aim = 0
}

func (sub *Submarine) move_horizontal(magnitude int) {
	sub.horizontal += magnitude
}

func (sub *Submarine) move_depth(magnitude int) {
	sub.depth += magnitude
}

func (sub *Submarine) move_aim(magnitude int) {
	sub.aim += magnitude
}

func (sub *Submarine) move_with_aim(magnitude int) {
	sub.horizontal += magnitude
	sub.depth += (sub.aim * magnitude)
}

func main() {
	// SETUP
	sub_commands := strings.Split(getFileInput("day2_input.txt"), "\n")

	// PART 1
	var sub Submarine
	sub.init_sub()

	for _, command := range sub_commands {
		direction := strings.Split(string(command), " ")[0]
		magnitude, _ := strconv.Atoi(strings.Split(string(command), " ")[1])

		switch direction {
		case "forward":
			sub.move_horizontal(magnitude)
		case "down":
			sub.move_depth(magnitude)
		case "up":
			sub.move_depth(magnitude * -1)
		}

	}

	fmt.Printf("PART 1 MULTIPLIED POSITION: %d\n", sub.depth*sub.horizontal)

	// PART 2
	sub.init_sub()

	for _, command := range sub_commands {
		direction := strings.Split(string(command), " ")[0]
		magnitude, _ := strconv.Atoi(strings.Split(string(command), " ")[1])

		switch direction {
		case "forward":
			sub.move_with_aim(magnitude)
		case "down":
			sub.move_aim(magnitude)
		case "up":
			sub.move_aim(magnitude * -1)
		}
	}

	fmt.Printf("PART 2 MULTIPLIED POSITION: %d\n", sub.depth*sub.horizontal)

}
