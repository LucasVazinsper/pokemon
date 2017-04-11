import colorama
from colorama import Fore, Back, Style
colorama.init()
import time
import sys
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.01)
delay_print("Welcome to the marvelous word of Inspermon")
input()
delay_print("Are you a boy or a girl?\nboy:(1)\ngirl:(2)")
boyorgirl=input("-\n")
while boyorgirl!="1" and boyorgirl!="2":
    print("Type a valid command")
    boyorgirl=input("\n")
delay_print("What is you name young trainer")
playername=input("\n")
delay_print("Well done {}.Let's get it started!".format(playername.title()))
input()
delay_print("First you have to get your new partner")
input()
delay_print("What do you prefer?")
delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(2)")
delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(3)")
firstpokemon=input("\n")
