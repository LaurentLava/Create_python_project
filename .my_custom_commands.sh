#!/bin/bash

# prints the input (test function)
function print_my_input(){
	echo 'Your input: ' $1
}


# Create a python project with a .py file
# and also a README.md file.

function create_python_project(){
	cd
	source .env
	python create_python_project.py $1
	cd 'Documents/python/'
	cd $1
	git init
    git remote add origin https://github.com/$USERNAME/$1.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master
	VAR0="README.md "
	VAR1=".py"
	VAR2="$1$VAR1"
	open -a Mou $VAR0
	sublime $VAR2
}