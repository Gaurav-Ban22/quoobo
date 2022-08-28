import argparse
from asyncore import dispatcher_with_send
from ctypes.wintypes import tagMSG
from dataclasses import asdict
from datetime import datetime
import io
from ssl import ALERT_DESCRIPTION_NO_RENEGOTIATION

yes = datetime.now()
import os



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

def colorize(text, color):
    return color + text + RESET

class algo:

    def __init__(self, tags, description, name, link):
        self.tags = tags
        self.description = description

        self.name= name
        self.link = link        

algos = [
    algo(["pathfinding, searching"], "An intelligent greedy algorithm used to intelligently find the most efficient path from one point to another.", "Astar", "https://www.geeksforgeeks.org/a-search-algorithm/"),
    algo(["looping"], "An algorithm that uses two different speed pointers to find a common number.", "Tortoise and Hare", "https://www.geeksforgeeks.org/a-search-algorithm/")]



parser = argparse.ArgumentParser();
subparser = parser.add_subparsers(dest='com', help="sub-command-help")

about = subparser.add_parser("about", help="about command")
about.add_argument("-m", help="more about information", action="store_true")
hau = subparser.add_parser("conti", help="content information")

echo = subparser.add_parser("echo", help = "repeat any singularworded string")
repeated = echo.add_argument("ec-hoo", nargs="+")
list = subparser.add_parser("ls", help = "blue is file, green is folder")
lista = subparser.add_parser("disp", help = "printout") 
repeated = lista.add_argument("shees")
repeato = list.add_argument("-u", help="unstable expanded format", action="store_true")
repeato = list.add_argument("-e", help="expanded format", action="store_true")
listee = subparser.add_parser("date", help = "time information to show through terminal")

alg = subparser.add_parser("searchA", help = "search algo list") 
algg = alg.add_argument("-n", help="unstable expanded format", action="store_true")
alggg =alg.add_argument("-c", help="unstable expanded format", action="store_true")
algggg = alg.add_argument("given")


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
    print(x)
elif args.com == "searchA":
    if (args.n):
        y = 0
        for f in algos:
            if args.given.lower() in f.name.lower():
                y += 1
                print(colorize(f.name, GREEN) + ": " + colorize(f.description, YELLOW)) 
        if y == 0:
            print(colorize("None matched your query", RED))

    # elif (args.c):
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


        
        
        

    