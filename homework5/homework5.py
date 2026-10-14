'Git is the framework that lets you save repositories of information'
'to external remote servers, whereas GitHub is the actual series'
'of repositories'
''
'A terminal is the thing that presents text to you, whereas the'
'command line is the place where you input text to run commands'
''
'A Local repository is a directory that is saved locally (i.e. on'
'your device), where a remote repository is that same directory,'
'but saved to an external server'
''
'Version Control essentially lets you hold onto older versions of'
'a repository, in case you need to back up to an older, working version'
'if the newer version goes awry'
''
'The staging area is where the files sit before you launch them'
'to your local repository.'
''
'git add is the command you run to dump all chosen changes'
'to the staging area'
''
'git commit commits those added chosen changes to the local repository'
''
'git push pushes the local repository and its changes to the remote'
'repository'
''
'git status tells you what folders are and arent committed to the'
'local repository, as well as what isnt added to the next commit push'
''
'git pull essentially lets you, for lack of a better phrase,'
'pull a remote repository and its changes to your local repository so'
'you can work with the latest online version'
''
'pwd prints the working directory, as in tells you what folder path'
'youre in at that current moment'
''
'ls lists the child directories in your current folder'
''
'cd maneuvers from your current directory to either a root path'
'or a local path'
''
'nano both can create a txt / txt based file, or edit one that already exists'
''
'touch I believe only creates a txt / txt based file'
''
'mv moves the chosen file to a new directory'
''
'rm removes the folder at the chosen path'
''
'cat concatenates a file, which tells you what the file reads out to,'
'which can be useful for a txt file, and/or can let you figure out what'
'a given file contains without explicitly running the file'
''
'2.2 Questions'
'1. pwd'
'2. ls'
'3. cd ../brianna_repo '
'git pull'
'4. mv homework.py ../judy_decal/homework'
'5. cd ../judy_decal/homework'
'6. git add .'
'git commit'
'git push -m "Finished homework"'
'7. I believe the error means the user is trying to push a change'
'to an outdated version, when someones already pushed'
'to a newer version'
'8. cd ~/Recents'

# HOMEWORK 3 REVIEW

def checkDataType(data_test):
    return str(type(data_test))

def evenOrOdd(checker):
    if checker % 2 == 0:
        return "Even"
    else:
        return "Odd"

# HOMWEORK 4 REVIEW

def numbers(int_list):
    sum = 0
    for i in int_list:
        sum += i
    return(sum)

# HOMEWORK 5 REVIEW

def duplicateList(checker):
    dupe_list = []
    for i in checker:
        dupe_list.append(i)
        dupe_list.append(i)
    return dupe_list

# DEBUGGING

# ORIGINAL CODE
# def square(num)
#     return num * num
# missing a colon on 1st line

# Fixed code
def square(num):
    return num * num

print(duplicateList(['a', 'b', 'c', 'd']))