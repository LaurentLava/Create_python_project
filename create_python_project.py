import sys
import os
from github import Github

my_project_folder = 'Documents/python/'
template_readme = 'Documents/python/templates/template.md'
template_py = 'Documents/python/templates/template.py'


def create_new_python_project():
	"""
	This function created a new project in the python
	directory and creates two files:
		- README.md
		- a .py file that will contain the python code
		- a TODO.txt file
	"""
	# Create the different variables
	folder_name = str(sys.argv[1])
	dir_name = my_project_folder + folder_name
	py_file = dir_name + '/' + folder_name + '.py'
	readme_file = dir_name + '/' + 'README.md'
	todo_file = dir_name + '/' + 'TODO.txt'

	# Create directory if it does not exist yet
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)
		print("Directory " , dir_name ,  " Created ")

		# Create Python file
		data = ''
		with open(template_py, 'r') as file:
			data += file.read()

		with open(py_file, 'w') as f:
			f.write(data)
			print("Python file created")

		# Create README file
		data = ''
		with open(template_readme, 'r') as file:
			data += file.read()

		with open(readme_file, 'w') as f:
			f.write(data)
			print("Readme file created")

		# Create Todo file
		with open(todo_file, 'w') as f:
			print("TODO file created")

		# Create Github repo
		with open(".env", "r") as f:
			data = f.read()

		index_1 = data.find('TOKEN="') + len('TOKEN="')
		token = data[index_1:-1]
		g = Github(token)
		user = g.get_user()
		repo = user.create_repo(folder_name)
		print("Succesfully created repository {}".format(folder_name))


	else:    
		print("Directory " , dir_name ,  " already exists")
	


if __name__ == "__main__":
	create_new_python_project()