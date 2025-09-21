import os

print(os.getcwd) # Current working directory
print("///////////////////////\n")

os.chdir("C:/Users/catas/OneDrive/Desktop/Mrinal/Dummy Folder") # Changing directory. 
print("Now in:", os.getcwd())
print("///////////////////////\n")

print(os.listdir()) # List of all files in that directory. 
print("///////////////////////\n")

for file in os.listdir():
    print(file)  # List of all files in that directory. 
print("///////////////////////\n")

for file in os.listdir():
    if file =='lists - python course - 3.mov': # Getting a specific file out and printing other files. 
        continue
    print(file)
print("//////////////////////\n")

for file in os.listdir():
    name, ext =os.path.splitext(file) # Splitting base name from the extension and modify the name and putting it back together with the extension afterwards. 
    print(name)
    print(ext)
print("//////////////////////\n")

for file in os.listdir():
    name, ext = os.path.splitext(file)
    splitted=name.split("-")
    splitted=[s.strip() for s in splitted] # Removing spaces for every character in splitted.
    new_name=f"{splitted[3].zfill(2)}-{splitted[2]}-{splitted[1]}-{splitted[0]}{ext}" # zfill() for adding zeroes in the beginning. 
    print(splitted) # Lists with all the separate elements
    print(new_name) # Lists with specific arrangement name of files
print("//////////////////////\n")

for file in os.listdir():
    name, ext =os.path.splitext(file)
    splitted=name.split("-")
    splitted=[s.strip() for s in splitted] 
    new_name=f"{splitted[3].zfill(2)}-{splitted[2]}-{splitted[1]}-{splitted[0]}{ext}"
    os.rename(file, new_name) # File name changed in the folder. 

