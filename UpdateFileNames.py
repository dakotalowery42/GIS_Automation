import os

filePath = r"File Path"  # Put the path of your file name here

dir_list = os.listdir(filePath)

for files in dir_list:  # for loop for first replacement
    print(files)
    replaced = files.replace("Character you would like to replace",
                             "Character that you will be replacing it with")
    replacedfilepathname = os.path.join(filePath, replaced)
    filepathname = os.path.join(filePath, files)
    os.rename(filepathname, replacedfilepathname)
for files in dir_list:  # secondary for loop for any other replacements
    print(files)
    replaced = files.replace("Character you would like to replace",
                             "Character that you will be replacing it with")
    replacedfilepathname = os.path.join(filePath, replaced)
    filepathname = os.path.join(filePath, files)
    os.rename(filepathname, replacedfilepathname)
