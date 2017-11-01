#
# makefile
#
# makefile for floyd.py
#
# Created by John Van Note
# Created on 03/06/12

# viewing (command "make view")

floyd=floyd.py

view: 
	cat $(floyd) | less

# runs the program with input from the user
run: $(floyd)
	python $(floyd)

# test example.input
test1: $(floyd)
	python $(floyd) < example1.input

# test example2.input
test2: $(floyd)
	python $(floyd) < example2.input