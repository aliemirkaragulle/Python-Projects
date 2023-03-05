# Advanced Python Modules Solution
import os
import re
import shutil

# Unzip the file unzip_me_for_instructions.zip
to_be_unzipped = "/Users/aliemirkaragulle/Desktop/Complete Python Bootcamp From Zero to Hero in Python/Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/unzip_me_for_instructions.zip"
dir_for_extract_result = "unzipped_instructions"
# shutil.unpack_archive(to_be_unzipped, dir_for_extract_result, 'zip')

# Search for a telephone number in the ###-###-#### format using Regular Expressions 
#pattern = r'\d{3}-\d{3}-\d{4}'

# Change the Current Working Directory to the Desktop 
curr_work_dir = os.getcwd()
if curr_work_dir != "/Users/aliemirkaragulle/Desktop":
    print(f"Current Working Directory: {os.getcwd()}")
    print("Changing the Current Working Directory to the Desktop")
    os.chdir("/Users/aliemirkaragulle/Desktop")
print(f"Current Working Directory: {os.getcwd()} \n")
print(f"Directories: {os.listdir()} \n")

# Check if the Directory that We Want to Search is in the Desktop
present = 0
if dir_for_extract_result in os.listdir():
    present = 1
    print(f"The directory - {dir_for_extract_result} - is present in the Desktop!")
else:
    present = 0
    print(f"The directory - {dir_for_extract_result} - is not present in the Desktop!")

# There is no need for the code below 
"""
# Change the Current Working Directory Inside the Directory that We Want to Search if It is Present in the Desktop
if present:
    print("Changing the Current Working Directory to the Directory that We Want to Search")
    os.chdir(f"/Users/aliemirkaragulle/Desktop/{dir_for_extract_result}")
print(f"Current Working Directory: {os.getcwd()} \n")
print(f"Directories: {os.listdir()} \n")
"""

print('\n')
phone_number = "Searching..."
for folder, sub_folders, files in os.walk(dir_for_extract_result):
    print("Current Folder: "+ folder)
    print('\n')

    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold)

    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)

        # Open the file
        if f != ".DS_Store":
            with open(f"{os.getcwd()}/{folder}/{f}", "r") as file:
                # Read the file
                text = file.read()
                #print(f"\t Path: {os.getcwd()}/{folder}/{f} File: {f} Type: {type(search_file)}")

                # Search for the pattern in the file
                match = re.search(r'\d{3}-\d{3}-\d{4}', text)
                if match is not None:
                    phone_number = match.group()
                    print(f"\t The phone number {match.group()} has been found in the file {f} inside the subfolder {sub_fold}!")
    print('\n')

print(f"The number we were looking for is: {phone_number}")