package main

import "fmt"

func main() {
	unsorted := []int{10, 6, 2, 1, 11, 14, 5, 8, 3, 4, 7, 9}
	array := mergeSort(unsorted)

	fmt.Println(array)

}

func mergeSort(array []int) []int {
	if len(array) < 2 {
		return array
	}
	left := mergeSort(array[:len(array)/2])
	right := mergeSort(array[len(array)/2:])
	return merge(left, right)

}

func merge(left []int, right []int) []int {
	var result []int

	i := 0
	j := 0
	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}
	for ; i < len(left); i++ { // if list still contain element append resultList -> (they are already in order)
		result = append(result, left[i])
	}
	for ; j < len(right); j++ { // if list still contain element append resultList -> (they are already in order)
		result = append(result, right[j])
	}
	return result
}
