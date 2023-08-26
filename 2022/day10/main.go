package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var (
	inputFile     = "input.txt"
	cycle, x, sum = 0, 1, 0
)

var cycles_ref = map[string]int{
	"noop": 1,
	"addx": 2,
}

func new_cycle() {
	cycle += 1

	if cycle == 20 || cycle%40 == 20 {
		sum += cycle * x
	}

	fmt.Printf("debug : cycle=%d x=%d, sum=%d\n", cycle, x, sum)
}

func noop() {
	new_cycle()
}

func addx(a int) {
	new_cycle()
	new_cycle()
	x += a

}

func firstPart() error {

	file, err := os.Open(inputFile)
	if err != nil {
		return fmt.Errorf("error opening file: %s", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		lines := scanner.Text()
		instruction := strings.Split(lines, " ")
		switch instruction[0] {
		case "noop":
			//fmt.Print("debug : noop")
			noop()

		case "addx":
			//fmt.Printf("debug : addx %s", instruction[1])
			val, err := strconv.Atoi(instruction[1])
			if err != nil {
				log.Fatalln(err)
			}
			addx(val)

		default:
			fmt.Errorf("error : undifined instructin founded %s", instruction[0])
		}

	}

	if err := scanner.Err(); err != nil {
		return fmt.Errorf("error reading file: %s", err)
	}

	return nil
}

func secondPart() (int, error) {
	var result int

	file, err := os.Open(inputFile)
	if err != nil {
		return -1, fmt.Errorf("error opening file: %s", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		_ = strings.Split(line, ";")
		// ur algo
		//fmt.Println(line)
	}

	if err := scanner.Err(); err != nil {
		return -1, fmt.Errorf("error reading file: %s", err)
	}

	return result, nil
}

func main() {

	err := firstPart()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("First part answer is : %d\n", sum)

}
