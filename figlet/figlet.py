import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fl = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fl))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fl:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

x = input("Input: ")
print(figlet.renderText(x))