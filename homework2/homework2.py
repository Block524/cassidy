# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Github is the actual website which hosts git repositories, and git bash is the tool you use to connect your computer to github.

# 2) What’s the difference between the terminal and the command line?
# The terminal is the software that allows for input and text output of commands that are inputted through the command line.

# 3) How does Windows PowerShell differ from Git Bash?
# The only real difference I can find is that git bash is the linux machine shell, while powershell is mostly meant for windows machines, and that syntax slightly differs between the two.

# 4) What’s the difference between Anaconda, conda, and Python?
# conda is the package distributor, while Anaconda is specifically a group of packages conda can manage. Python is a programming language that uses these packages to streamline code.

# 5) What is VS Code?
# VSCode is an IDE, which is a text editor with gui elements that help to streamline code writing/editing. It allows you to import various programming languages to code with, and can directly run and compile code.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# A Jupyter Notebook is a website IDE essentially, specifically for python. It differs from Jupyter Lab (from what I have found) through UI elements, and slightly varying features.

# 7) What does ~/ mean?
# ~/ represents home directory. If you used cd ~/(full directory name), you would start defining the directory from your home directory.
# 8) What’s the difference between an absolute path and a relative path?

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Absolute path: ~/Documents/python_decal_fa26/course_assignments/homework2/
# Relative path: ../course_assignments/homework2/

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# It would delete the current directory

# 12) What do the following commands do?
# git add
# It adds whatever files are in whichever path you input afterwards to the list of things git is preparing to commit.

# git commit
# It saves the things you added through git add to a local repository

# git push
# Pushes the things saved to your local repository and updates the remote repository on github

# 13) What's the difference between "git add ." and "git add <file>"?
# git add . will simply add everything to the pending commit list within your current directory, whilst git add <file> will add that singular file.

# 14) What do "git status" and "git log -1" do?
# git status displays the pending commits, as well as what files have or haven't been added to the pending commit. git log -1 will tell you the most recent commit status.

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning a repository means you're downloading it with no intent to update said remote repository, while a pull request means you are intending to update said repository on github, or at least request for your changes to be updated to it.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# My most frustrating error was trying to figure out how to create an ssh key, which was troubleshot through reading through the git bash installation guide on bcourses.

# 17) What’s a question you still have? What’s something you’re confused about?
# Is there a particular reason the homework doc is asking us to do this assignment through nano? If there's not a functional differnce between using nano and vs code, I'd prefer to swap to vs code.

# 18) Tell me a fun fact!
# I've played cello semi-professionally for the last 5 years.

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print(12 * 2 * 3.1415) # Prints the circumference of a circle of radius 12.
