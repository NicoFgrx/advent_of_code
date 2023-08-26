package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var inputFile = "sample_input.txt"

func firstPart() (int, error) {
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

	res, err := firstPart()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("First part answer is : %d\n", res)

	res, err = secondPart()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("First part answer is : %d\n", res)

}
