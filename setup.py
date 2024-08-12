import re

def replace_variables(file_path, old_var, new_var):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(r'\$\{' + re.escape(old_var) + r'\}', new_var, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Projects Template Setup")

repo = 'repoName'
repo_replace = input("Enter the name of project repository: ")

project = 'projectName'
project_replace = input("Enter the name of initial project: ")

header = 'projectNameHeader'
header_replace = input("Enter the name of initial project header: ")

replace_variables('index.html', repo, repo_replace)
replace_variables('index.html', project, project_replace)
replace_variables('index.html', header, header_replace)

print("Setup successful!")