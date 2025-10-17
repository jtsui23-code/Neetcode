import os

directory = "./"
file_count = len(
    [f for f in os.listdir(directory) 
    if os.path.isfile(os.path.join(directory, f))]

)
print(f"You have done {file_count -2} neetcode questions.")