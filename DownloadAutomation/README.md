# Download Automation

### Objective:
With this project, I aim to be able to automate file handling of all donwloads that occur on my computer. The script will run such that all files downloaded to the "Downloads" folder on my Mac will get divided into respective folders on the basis of the file's extention.

### Examples
If the download is "transcript.txt", the file will go into a folder called "TXT".
If the download is "image.jpeg", the file will go to a folder called "JPEG".

### Why I chose this Project:
I have never had a clean, organised "Downloads" folder. It is always cluttered with unwanted files, a mix of all different kinds of files like, ".jpg", ".pdf", ".iso", etc. That is why I finally decided to help myself learn and automate this process.

### List of Sub-problems:
1. How will I find out if a file is in the "Downloads" folder?
2. How will I know if something was downloaded in "Downloads"?
3. How will I check if the "Downloads" folder has folders but no other files?

### Solution to Sub-problems:
1. I used the "os" (specifically, `os.path.isfile(file)`) lilbrary in python and found out if the "file" exists in the given path. With this I also learned how to navigate from my current directory to the "Downloads" folder on my Mac.
   - See "checking_for_directory.py" and "check_for_file.py"
2. I used the `os.listdir(directory)` to see if the "directory" has any files in it.
   - See "check_if_dir_is_empty.py"
3. I used the fact that my default folders are all capitalized and have no symbols and that files usually have an extention. Therefore, any item with an extention will be a file.
   - See "folders_but_no_file.py"

### Concepts Learned:
1. `['.DS_Store', '.localized']` are default, hidden files in the "Downloads" folder in a Mac and need to be considered. Their existence though does not need to be manipulated
