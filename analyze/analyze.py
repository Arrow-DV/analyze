# Analyze Text Files Made By Ali-Hany | Arrow Production
# Created - > 2/3/2024 | Last Update - > 2/3/2024
# Visit Us! https://arrow-dev.rf.gd
# I will slice the code into paragraphs




# Import Needed Library's
from sys import argv as arg
import random
import os


# arg[1] -> file path / arg[2 or 3] -> Commands
if len(arg) < 2:
    exit()
filename = arg[1].strip()
file = None
try:
    file = open(filename, "r")
except FileNotFoundError:
    print("-> File Wasn't Found")
    exit()
counts = {}

# Check Word Counts
for word in file.readlines():
    word = word.strip().lower()
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
file.close()


# Now Print The Result
def show_result():
    print("Word","Count",sep="\t") # سطر للشكل بس
    print("-"*4,"-"*5,sep="\t") # سطر للشكل بس
    for key,value in counts.items():
        print(key,value,sep="\t")


# Def That Make Text File Of The Result
def save_result():
    global counts
    with open(f"result{random.randint(0,100)}.txt","w+") as file:
        file.write("Word\tCount\n") # سطر لشكل الملف بس
        file.write(f"{"-"*4}\t{"-"*5}\n") # سطر لشكل الملف بس
        for key,value in counts.items():
            file.write(f"{key}\t{value}\n")
        print(f"-> File Saved At {os.path.abspath(file.name)}")



# Check Wanted Command Part 
# arg[0] -> Call The Function | arg[1] -> File Path | arg[2 | 3] -> Commands Thats Why It Start From arg[2:]
for _ in arg[2:]:
        if _.lower() == ("-print") :
            show_result() 
        elif _.lower() == ("-create"):
            save_result()
