import os
from pathlib import Path


for file in os.listdir():
    f=Path(file)
    name, ext = f.stem, f.suffix
    splitted=name.split("-")
    splitted=[s.strip() for s in splitted] 
    new_name=f"{splitted[3].zfill(2)}-{splitted[2]}-{splitted[1]}-{splitted[0]}{ext}"
    f.rename(new_name)

# Error coming due to Indexing. 