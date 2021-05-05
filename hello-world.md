
supports items 3,4,5


# Github Profiles 101
**Executive Summary:** This Document is the lesson plan for the most important system configuration diagnostic tool. We will explore the program 'hello world'.

## Main takeaway: If you can run 'hello world' your system is set up.

## Reminder of Definitions
1. 'hello world' - a type of program, characterized by minimum overhead to demonstrate a system is set up and functional
2. system - for example a programming environment. for example python

## "hello world" .... what is it good for?
Wikipedia puts it extremely well
> A "Hello, World!" program generally is a computer program that outputs or displays the message "Hello, World!". Such a program is very simple in most programming languages, and is often used to illustrate the basic syntax of a programming language. It is often the first program written by people learning to code.[1][2] It can also be used as a sanity test to make sure that a computer language is correctly installed, and that the operator understands how to use it.

* In this orientation we are going to be setting up resources and the goal is to finish with the ability to run 'hello world'.
* The second thing that it does is provide a beachhead. When you encounter a new computer environment by running 'hello world' a person has established the base upon which to build their foundation.
* Once the habit of using 'hello world' is established then in new locations it gives you a sense of orientation.


## Contemporary Environments
* BASH - `echo 'hello world'`
* python - `print('hello world')`
* R - `print('hello world')`

## Old School Environment Example - 6502 Assembly
```
* = $C000       ;set the initial memory address

CHROUT = $FFD2  ;set the address for the character out subroutine

         LDY #$00 

LOOP     LDA HELLO, Y 

         CMP #$00

        BEQ END 

        JSR CHROUT 

        INY 

        BNE LOOP 

END      RTS

HELLO    ASC 'HELLO, WORLD.' ; PETSCII

HELLOEND DFB 0 ; zero byte to mark the end of the string
```


# Conclusions, Homework, and Takeaways
* When you are setting up a system in this orientation (bash,python,R) or in the future. The first program you run should be 'hello world'
* Now read [this article](https://www.wintellect.com/30-years-of-hello-world/) and compare those languages with python and R and reflect on how lucky you are.



## Reading List
This list is initially populated with wikipedia articles. The goal of the exercise for the students is to improve this list. When you find something better make a pull request and improve the list.
* https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
* https://www.wintellect.com/30-years-of-hello-world/
