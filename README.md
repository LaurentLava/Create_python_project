# Project Title

Automatization of the creation of a python project and direct creation of the github corresponding repo

## Description

As I created more and more projects in Python, I decided to automatize the way to create a Python project. I therefore created a custom terminal command that triggers the creation of:

* a .py file based on a template of mine
* a readme.md file based on a template of mine
* a todo.txt

It generates a github repo automatically and synchronizes these files. It then open the .py and .md files with sublime and Mou respectively. 


## Getting Started

### Dependencies

* Built on mac
* Need sublime and Mou installed
* File structures:
	* home
		* create_python_project.py
		* .env
		* Documents
			* python
				* Templates
				
				
The project will be create in the python subfolder


### Installing

* Clone the repo using

```
https://github.com/LaurentLava/Create_python_project
```

### Executing program

* Run the following line in your terminal

```
create_python_project MyProjectName
```



## Authors

Laurent Lava (laurentlava04[at]gmail.com)

## Version History

* 0.2 
	* Add github capabilities
* 0.1
    * Initial Release

## Acknowledgments

Main inspirations are:

* https://stackoverflow.com/questions/28675121/how-to-create-a-new-repository-with-pygithub
* https://github.com/KalleHallden/ProjectInitializationAutomation