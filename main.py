import argparse
from ctypes.wintypes import tagMSG


from os import *

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

class algorithm:

    def __init__(self, tags, description, name):
        self.tags = tags
        self.description = description
        self.name= name



parser = argparse.ArgumentParser();
subparser = parser.add_subparsers(dest='com', help="sub-command-help")

about = subparser.add_parser("about", help="about command")
about.add_argument("-m", help="more about information", action="store_true")
echo = subparser.add_parser("echo", help = "repeat any singularworded string")
repeated = echo.add_argument("echoo", nargs="+")
list = subparser.add_parser("ls", help = "blue is file, green is folder")
repeato = list.add_argument("-u", help="unstable expanded format", action="store_true")
repeato = list.add_argument("-e", help="expanded format", action="store_true")
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
elif args.com == "ls":
    if (not args.e and not args.u):
        for f in listdir(getcwd()):
            
            if (path.isdir(getcwd()+"/"+f)):
                if (f.startswith(".")):
                    print(colorize(f, YELLOW))
                print(colorize(f, GREEN))
            else:
                print(colorize(f, BLUE))
    elif (args.u):
        for f in listdir(getcwd()):
            
            if (path.isdir(getcwd()+"/"+f)):
                print(colorize(f, GREEN))
                if (f.startswith(".")):
                    print(colorize(f, YELLOW))
                for f in listdir(getcwd()+"/"+f):
                    print("  -" + colorize(f, RED))
            else:
                print(colorize(f, BLUE))

    elif(args.e):
        for f in listdir(getcwd()):
            
            if (path.isdir(getcwd()+"/"+f)):
                if (not f.startswith(".")):
                    print(colorize(f, GREEN))
                    for f in listdir(getcwd()+"/"+f):
                        print("  -" + colorize(f, RED))
                else:
                    print(colorize(f, YELLOW))
            else:
                print(colorize(f, BLUE))


        
        
        

    