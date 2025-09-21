import os
from pathlib import Path
import shutil
os.chdir("C:/Users/catas/OneDrive/Desktop/Mrinal/Dummy Folder")

Path("data").mkdir(exist_ok=True) # Create new folder in the location. 

# Another old way:
if not os.path.exists("data1"):
    os.mkdir("data1")

for file in os.listdir():
    if file == "data":
        continue
    print(file) # data file does not get printed. 
    shutil.move(file,"data1") # All files are now in data1 folder from dummy folder. 