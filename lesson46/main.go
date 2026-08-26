package main

import "fmt"

type Student struct {
	Name string
	Age  int
      course string
}

func (s Student) Introduce() {
	fmt.Println("My name is", s.Name)
	fmt.Println("I am", s.Age, "years old.")
        fmt.println("I am studying",s.course)
}

func main() {
	student := Student{
		Name: "Jerome",
		Age:  20,
	        course:"computer studies"
}

	student.Introduce()
}
