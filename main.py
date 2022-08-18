import argparse

parser = argparse.ArgumentParser();
subparser = parser.add_subparsers(dest='com')

about = subparser.add_parser("about")
about.add_argument("about", help="about quoobo", action="store_true")
args = parser.parse_args()

if args.com == "about":
    print("Quoobo is a program to make unix-based-commands a little bit more fun. It was made in python by Gaurav-Ban22. Check him out on github!")