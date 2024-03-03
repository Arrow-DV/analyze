# Read Text Files Made By Ali-Hany | Arrow Production
# Created - > 2/3/2024 | Last Update - > 3/3/2024
# Visit Us! https://arrow-dev.rf.gd

from sys import argv as arg

# Check If Given Args Less Than [ 3 ]
if len(arg) < 3:
    print("-> Missing Args")
    exit()

# Get File Path
option = arg[1].split("-")[1]
if len(arg) >= 4 :
    filename = arg[3]
else:
    filename = arg[2]

# Functions
def readlines():
    """Read Text Files As Lines\n
[Number Of The Line] Line
    """
    with open(filename, 'r+', encoding="UTF-16") as file:
        for num, line in enumerate(file.readlines(), start=1):
            print(f"[{num}] {line}", end="")

def until_line(line: int):
    """
    print the text content
    until reach the wanted line
    \n
    line - > int
    """
    with open(filename, 'r+', encoding="UTF-16") as file:
        for num, content in enumerate(file.readlines(),start=1):
            if num == line:
                exit()
            else:
                print(f"[{num}] {content}",end="")

def special_text(word: str):
    """Searching The Text File Content
Until Find "Word" Returns\nNumber Of The Line\nElse "Not Found"
-------
word -> String | The Word You Want To Find In The Text File
    """
    with open(filename, 'r+', encoding="UTF-16") as file:
        for num, content in enumerate(file.readlines(), start=1):
            if content.lower().strip() == word.lower().strip():
                print(f'[{num}] {content}',end="")
                return
        else:
            print('-> Not Found')

# [Option] : [Function]
options = {
    "l": readlines,
    "find": special_text,
    "ul": until_line,
}

def main():
    """The Main Function Which Runs The App"""
    try:
        if option in ["find", "ul"]:
            arg[2] = int(arg[2]) + 1 if option == "ul" else str(arg[2])
            options[option](arg[2])
        else:
            options[option]()
    except Exception as err:
        print(f"-> {err}")

try:
    main()
except Exception as error:
    print(f"-> {error}")