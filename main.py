import argparse


from datetime import datetime
from genericpath import isfile

import shutil
yes = datetime.now()
import os

lo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum convallis ante a vulputate. Pellentesque pulvinar congue diam ut bibendum. Phasellus non sem sed leo commodo feugiat. Sed bibendum mollis lorem aliquam rhoncus. Proin egestas pharetra augue ut porta. Sed turpis arcu, vulputate sit amet semper in, convallis ut eros. Nullam eu leo risus. Mauris suscipit, dolor ut accumsan gravida, leo libero tincidunt erat, a consectetur dui turpis id orci. Nullam sollicitudin ante et tellus dignissim mollis. Praesent lacinia turpis non risus fringilla mollis. Vestibulum non nibh non eros venenatis hendrerit. Morbi rhoncus sagittis orci, sed bibendum neque malesuada viverra. Phasellus ex quam, dignissim et tortor quis, semper fermentum leo. Integer finibus sapien et posuere gravida. Sed fermentum nulla eu neque pulvinar sagittis. Vivamus eu nunc eget velit lobortis consequat sed nec lectus. Donec eget accumsan ipsum. Sed et massa varius urna mattis porttitor in vel sem. Fusce ornare lorem molestie, commodo nisi mattis, varius odio. Sed vulputate, risus at eleifend molestie, augue justo ornare nisl, vel ullamcorper orci tellus vitae lectus. Curabitur aliquet eros in arcu laoreet ultrices. Suspendisse potenti. Maecenas varius dolor eget ex faucibus, nec commodo lorem aliquet. Sed justo dolor, fringilla ac ipsum sit amet, lacinia fermentum ex."

RESET = "\u001B[0m"
BLACK = "\u001B[30m"
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
PURPLE = "\u001B[35m"
CYAN = "\u001B[36m"
WHITE = "\u001B[37m"
BLACK_BOLD = "\033[1;30m"
RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
BLUE_BOLD = "\033[1;34m"
PURPLE_BOLD = "\033[1;35m"
CYAN_BOLD = "\033[1;36m"
WHITE_BOLD = "\033[1;37m"
#this is a cli with multiple commands

def colorize(text, color):
    return color + text + RESET
#cli


class algo:

    def __init__(self, tags, description, name, link, index):
        self.tags = tags
        self.description = description
        self.index = index

        self.name= name
        self.link = link        

algos = [
    algo(["pathfinding", "searching"], "An intelligent greedy algorithm used to intelligently find the most efficient path from one point to another.", "Astar", "https://www.geeksforgeeks.org/a-search-algorithm/", 1),
    algo(["looping"], "An algorithm that uses two different speed pointers to find a common number.", "Tortoise and Hare", "https://www.geeksforgeeks.org/a-search-algorithm/", 2),
    algo(["looping", "searching"], "Searches binarily", "Binary Search", "https://www.geeksforgeeks.org/a-search-algorithm", 3)
    
    ]



parser = argparse.ArgumentParser();
subparser = parser.add_subparsers(dest='com', help="sub-command-help")
about = subparser.add_parser("about", help="about command")
about.add_argument("-m", help="more about information", action="store_true")
hau = subparser.add_parser("conti", help="content information")

echo = subparser.add_parser("echo", help = "repeat any singularworded string")
repeated = echo.add_argument("echoo", nargs="+")
addd = subparser.add_parser("cat", help = "add to back of any file, or concatenate two of them")
adddd = addd.add_argument("argu", nargs="+")
list = subparser.add_parser("ls", help = "blue is file, green is folder")
lista = subparser.add_parser("disp", help = "printout") 
repeated = lista.add_argument("shees")
repeato = list.add_argument("-u", help="unstable expanded format", action="store_true")
repeato = list.add_argument("-e", help="expanded format", action="store_true")
listee = subparser.add_parser("date", help = "time information to show through terminal")
awlg = subparser.add_parser("tree", help = "tree") 
tre = awlg.add_argument("-b", help="unstable expanded format", action="store_true")
csharp = subparser.add_parser("lorem", help = "lorem ipsum") 
a = csharp.add_argument("ipsum")
alg = subparser.add_parser("searchA", help = "search algo list") 
algg = alg.add_argument("-n", help="unstable expanded format", action="store_true")
alggg =alg.add_argument("-c", help="unstable expanded format", action="store_true")
algggg =alg.add_argument("-i", help="unstable expanded format", action="store_true")
algggggggggg =alg.add_argument("-l", help="unstable expanded format", action="store_true")
alggggggg = alg.add_argument("given")

kotlin = subparser.add_parser("del", help = "delete") 
java = kotlin.add_argument("file")

kotlina = subparser.add_parser("add", help = "add") 
javaa = kotlina.add_argument("fileLib")

kotlinaaa = subparser.add_parser("mkd", help = "mkdir") 
javaaaa = kotlinaaa.add_argument("dir")
kotlinaa = subparser.add_parser("re", help = "rename any file given as extra parameter") 
javaaa = kotlinaa.add_argument("files", nargs="+")

alga = subparser.add_parser("listA", help = "algo list") 

def tree(path, lvl, unstable):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            print(colorize(("   " * lvl + "-" + file), GREEN))
        elif not file.startswith(".") and not unstable:
            print(colorize(("   " * lvl + "-" + file), BLUE))
            tree(os.path.join(path, file), lvl + 1, unstable)
            #can multiply strings by integers to repeat them, I didn't know that :O
        elif unstable:
            print(colorize(("   " * lvl + "-" + file), BLUE))
            tree(os.path.join(path, file), lvl + 1, unstable)
            
args = parser.parse_args()

if args.com == "about":
    if (not args.m):
        print("Quoobo is a program to make unix-based-commands a little bit more fun. It was made in python by Gaurav-Ban22. Check him out on github!")
    else:
        print("Quoobo is a program to make unix-based-commands a little bit more fun. It was made in python by Gaurav-Ban22. Check him out on github!\nThere are also some other things you might want to see; check -h for more commands!")
elif args.com == "echo":
    x = ""
    for i in enumerate(args.echoo):
        x += i[1] + " "
    print(colorize(x, GREEN))
elif args.com == "re":
    isF = ""
    if (len(args.files) > 2):
            print(colorize("Too many arguments; only provide 2 - 1 file to rename and 1 name to rename it to. Please include the file type, such as test.txt or main.py", RED))
    else:
        if (os.path.isfile(os.getcwd() + "/" + args.files[0])):
            isF = "file"
            
        else:
            isF = "directory"

        x = input(colorize("Are you sure you want to rename " + isF + " " + args.files[0] + " to " + args.files[1] + "? (y/n)", YELLOW))
        if x == "y":
            os.rename(os.getcwd() + "/" + args.files[0], args.files[1])
        else:
            print(colorize("Rename not performed", RED))
            

elif args.com == "add":
    fileP = open(os.getcwd() + ("/" + args.fileLib), "x") #x means create file exclusively
    print(colorize("Created file!", GREEN))
elif args.com == "mkd":
    try:
        os.mkdir(os.getcwd() + ("/" + args.dir))
        print(colorize("Created directory", GREEN))
    except FileExistsError:
        print(colorize("Directory already exists in given cwd", RED))
elif args.com == "cat":
    try:
        with open(os.getcwd()+"/"+args.argu[0], "r") as t:
            try:
                li = t.readlines()
                
                print(colorize(args.argu[0] + " catted with " + args.argu[1],BLUE))
                print("---------------------------------")
                for i in (li):        
                    print(colorize(i, GREEN))
               
            except:
                print(colorize(("Cannot read or fine file " + args.argu[0]), RED))
        with open(os.getcwd()+"/"+args.argu[1], "r") as t:
            try:
                print("\n")
                li = t.readlines()            
                for i in (li):        
                    print(colorize(i, GREEN))
                print("---------------------------------")
            except:
                print(colorize(("Cannot read or find file " + args.argu[1]), RED))
    except:
        print(colorize(("There was an error with your request"), RED))
elif args.com == "del":
    p = ""
    if os.path.isfile(os.getcwd() + ("/" + args.file)):
        x = input(colorize(("Are you sure you want to delete file " + args.file + "? (y/n) "), YELLOW))
        if x == "y":
            os.remove(os.getcwd() + ("/" + args.file))
            print(colorize("Folder deleted", RED))
        else:
            print("File not deleted")
    elif os.path.isdir(os.getcwd() + ("/" + args.file)):
        if (len(os.listdir(os.getcwd() + "/" + args.file)) != 0):
            p = "There are " + str(len(os.listdir(os.getcwd() + "/" + args.file))) + " items in this directory. "
            if (len(os.listdir(os.getcwd() + "/" + args.file)) == 1):
                p = "There is 1 item in this directory. "

            
        x = input(colorize(("Are you sure you want to delete folder " + args.file + "? " + p +  "(y/n) "), YELLOW))
        if x == "y":
            try:
                os.rmdir(os.getcwd() + ("/" + args.file))
                print(colorize("Folder deleted", RED))
            except OSError:
                shutil.rmtree(os.getcwd() + ("/" + args.file))
                print(colorize("Folder deleted", RED))
        else:
            print(colorize("Folder not deleted", GREEN))
    else:
        print(colorize("File or directory not found", RED_BOLD))
    
        
    
elif args.com == "lorem":
    x = lo.split(" ")
    if len(args.ipsum) <= len(x):
        print(colorize(" ".join(x[:int(args.ipsum)]), GREEN))

elif args.com == "tree":
    tree(os.getcwd(), 0, args.b)
    files = 0
    dirs = 0
    dots = 0
    total = 0
    for f in os.listdir(os.getcwd()):
        if os.path.isfile(os.getcwd()+"/"+f):
            files += 1
        if os.path.isdir(os.getcwd()+"/"+f):
            if f.startswith("."):
                dots += 1
            else:
                dirs += 1
    total = files + dirs + dots

    print(colorize("\nFiles: " + str(files), CYAN))
    print(colorize("Directories: " + str(dirs), GREEN))
    print(colorize("DotFiles: " + str(dots), YELLOW))
    print(colorize("Total: " + str(total), WHITE))

elif args.com == "listA":
    for i in algos:
            print(str(i.index) + "  " + colorize(i.name, GREEN) + ": " + colorize(i.description, YELLOW)) 

elif args.com == "searchA":
    if (args.n):
        y = 0
        for f in algos:
            if args.given.lower() in f.name.lower():
                y += 1
                print(str(f.index) + "  " + colorize(f.name, GREEN) + ": " + colorize(f.description, YELLOW)) 
        if y == 0:
            print(colorize("None matched your query", RED))

    elif (args.c):
        y = 0
        for f in algos:
            for i in f.tags:
                if args.given.lower() == i:
                    y += 1
                    print(str(f.index) + "  " + colorize(f.name, GREEN) + ": " + colorize(f.description, YELLOW)) 
        if y == 0:
            print(colorize("None matched your query", RED))
    elif (args.i):
        try:
            for i in algos:
                
                if i .index == int(args.given):
                    print(str(i.index) + "  " + colorize(i.name, GREEN) + ": " + colorize(i.description, YELLOW)) 
                    print(colorize(i.link, BLUE)) 
            
        except:
            print(colorize("There was an issue with the index provided", RED))

        


elif args.com == "conti":
    files = 0
    dirs = 0
    dots = 0
    total = 0
    for f in os.listdir(os.getcwd()):
        if os.path.isfile(os.getcwd()+"/"+f):
            files += 1
        if os.path.isdir(os.getcwd()+"/"+f):
            if f.startswith("."):
                dots += 1
            else:
                dirs += 1
    total = files + dirs + dots

    print(colorize("Files: " + str(files), CYAN_BOLD))
    print(colorize("Directories: " + str(dirs), GREEN_BOLD))
    print(colorize("DotFiles: " + str(dots), YELLOW_BOLD))
    print(colorize("Total: " + str(total), WHITE_BOLD))

        
elif args.com == "disp":
    with open(os.getcwd()+"/"+args.shees, "r") as t:
        try:
            li = t.readlines()
            
            print(colorize(args.shees,BLUE))
            print("---------------------------------")
            for i in (li):        
                print(colorize(i, GREEN))
            print("---------------------------------")
        except:
            raise ValueError("Cannot read this file")

        
elif args.com == "date":
    
    dat = yes.strftime("%b-%d-%Y")
    dataso = yes.strftime("%H-%M-%S")
    print(colorize(dat, PURPLE))
    print(colorize(dataso, GREEN))
elif args.com == "ls":
    if (not args.e and not args.u):
        for f in os.listdir(os.getcwd()):
            
            if (os.path.isdir(os.getcwd()+"/"+f)):
                if (f.startswith(".")):
                    print(colorize(f, YELLOW)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")
                else:

                    print(colorize(f, GREEN)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")
            else:
                print(colorize(f, BLUE)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")
    elif (args.u):
        for f in os.listdir(os.getcwd()):
            
            if (os.path.isdir(os.getcwd()+"/"+f)):
                if (not f.startswith(".")):
                    print(colorize(f, GREEN,) + "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")
                    
                else:
                    print(colorize(f, YELLOW)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")

                for x in os.listdir(os.getcwd()+"/"+f):
                    print("  -" + colorize(x, RED)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f+"/"+x)) + "  bytes")
            else:
                print(colorize(f, BLUE)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")

    elif(args.e):
        for f in os.listdir(os.getcwd()):
            
            if (os.path.isdir(os.getcwd()+"/"+f)):
                if (not f.startswith(".")):
                    print(colorize(f, GREEN)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")
                    for x in os.listdir(os.getcwd()+"/"+f):
                        print("  -" + colorize(x, RED)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f+"/"+x)) + "  bytes")
                else:
                    print(colorize(f, YELLOW)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")
            else:
                print(colorize(f, BLUE)+ "  " + str(os.path.getsize(os.getcwd()+"/"+f)) + "  bytes")



#uses argparse top make a cli pog



