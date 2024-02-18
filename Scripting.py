"""
Python Scripting
"""

import os

cwd = os.getcwd() 

directory_list = os.listdir(cwd) 

path = "./"

file_list = []

print(directory_list)

for item in directory_list:
  
    file_name = os.path.basename(item)
    
    file_path = os.path.join(cwd,item)
    
    file_size = os.path.getsize(item)
    
   
    file_info = {'Name': item, 'File Size': file_size}

    file_list.append(file_info)

print(file_list)



for file_info in file_list:
    print(file_info)
    