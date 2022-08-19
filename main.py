import argparse

parser = argparse.ArgumentParser();
subparser = parser.add_subparsers(dest='com', help="sub-command-help")

about = subparser.add_parser("about", help="about command")
about.add_argument("-m", help="more about information", action="store_true")
echo = subparser.add_parser("echo", help = "repeat any string")
repeated = echo.add_argument("echoo")
args = parser.parse_args()

if args.com == "about":
    if (not args.m):
        print("Quoobo is a program to make unix-based-commands a little bit more fun. It was made in python by Gaurav-Ban22. Check him out on github!")
    else:
        print("Quoobo is a program to make unix-based-commands a little bit more fun. It was made in python by Gaurav-Ban22. Check him out on github!\nThere are also some other things you might want to see; check -h for more commands!")
elif args.com == "echo":
    print(args.echoo)