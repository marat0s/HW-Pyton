import os
directory = "NEWDIRECTORY"
parent_dir = "D:/"
path = os.path.join(parent_dir, directory) 
os.mkdir(path)
