import random as rd
#tipos de pokemon
Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]

#Todos os pokemons do jogo
pokemondata={"bulbasaur":{"type":"grass",
					"hp":45,
					"atk":49,
					"deff":49,
					"spd":40,
					"satk":40},
	"charmander":{"type":"fire",
					"hp":49,
					"atk":52,
					"deff":43,
					"spd":65,
					"satk":40},
	"squirtle":{"type":"water",
	              "hp":44,
                  "atk":50,
				  "deff":65,
				  "spd":43,
				  "satk":40},
	"caterpie":{"type":"bug",
	              "hp":45,
				  "atk":30,
				  "deff":35,
				  "spd":45,
				  "satk":40},
	"pidgey":{"type":"flying",
	              "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":56,
				  "satk":40},
	"pichu":{"type":"eletric",
                  "hp":20,
				  "atk":40,
				  "deff":15,
				  "spd":60,
				  "satk":40},
	"pikachu":{"type":"eletric",
                  "hp":35,
				  "atk":50,
				  "deff":50,
				  "spd":90,
				  "satk":70},
	"abra":{"type":"psychic",
	              "hp":25,
				  "atk":105,
				  "deff":55,
				  "spd":90,
				  "satk":40},
	"machop":{"type":"fighting",
	              "hp":70,
				  "atk":80,
				  "deff":50,
				  "spd":35,
				  "satk":40},
	"gastly":{"type":"ghost",
	              "hp":30,
				  "atk":100,
				  "deff":35,
				  "spd":80,
				  "satk":40},
	"grimer":{"type":"poison",
	              "hp":80,
				  "atk":80,
				  "deff":50,
				  "spd":25,
				  "satk":40},
	"rhyhorn":{"type":"rock",
	              "hp":80,
				  "atk":85,
				  "deff":95,
				  "spd":25,
				  "satk":50},
	"dratini":{"type":"dragon",
	              "hp":41,
				  "atk":64,
				  "deff":50,
				  "spd":50,
				  "satk":40},
	"bergmite":{"type":"ice",
	              "hp":55,
				  "atk":69,
				  "deff":85,
				  "spd":28,
				  "satk":55},
	"sandile":{"type":"ground",
	              "hp":50,
				  "atk":72,
				  "deff":35,
				  "spd":65,
				  "satk":40},
	"meowth":{"type":"normal",
	              "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":90,
				  "satk":40}}


class Pokemon:
    #classe para pokemons

    def __init__(self,pokemon,lvl):
        self.type=pokemon["type"] #tipo do pokemon
        self.lvl=lvl #lvl do pokemon
        self.hp=(((2*pokemon["hp"]+rd.randrange(1,32)+(50/4))*lvl)/100)+lvl+10 #vida atual do pokemon
        self.atk=(((2*pokemon["atk"]+rd.randrange(1,32)+(50/4))*lvl)/100)+5 #ataque atual do pokemon
        self.deff=(((2*pokemon["deff"]+rd.randrange(1,32)+(50/4))*lvl)/100)+5 #defesa atual do pokemon
        self.spd=(((2*pokemon["spd"]+rd.randrange(1,32)+(50/4))*lvl)/100)+5 #velocidade atual do pokemon
        self.satk=pokemon["satk"]
        self.exp=0
        self.atributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\n".format((self.type).capitalize(),self.lvl,int(self.hp),
                                                                                             (self.atk),int(self.deff),int(self.spd))


    def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)


class Player():
    #classe para o usuário

    def __init__(self,name,pokemon):
        self.party=[pokemon]  #lista de todos os pokemons do player
        self.name="{}".format(name)
        self.insperdex=["???"]*151



import colorama
from colorama import Fore, Back, Style
colorama.init()
import time
import sys
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.001)
delay_print("Welcome to the marvelous World of Inspermon")
input()
delay_print("You are at Proffesor Daniel's Inspermon Research lab\n")

delay_print("\nHello there! Welcome to the world of INSPERMON! My name is Daniel! People call me the INSPERMON Prof!\n")
input()
delay_print("\nThis world is inhabited by creatures called INSPERMON!\n")
input()
delay_print("\nFor some people, INSPERMON are pets. Other use them for fights. Myself… I study INSPERMON as a profession.\n")
input()
delay_print("\nFirst, what is your name?")
playername=input("\n")
playername+=" Ketchum"
delay_print("Right! So your name is {}!".format(playername.title()))
delay_print("Are you a boy or a girl?\nboy:(1)\ngirl:(2)")
boyorgirl=input("-\n")

while boyorgirl!="1" and boyorgirl!="2":
    print("Type a valid command")
    boyorgirl=input("\n")

delay_print("Well done {}.Let's get it started!".format(playername.title()))
input()
delay_print("First you have to get your new partner")
input()
delay_print("What do you prefer?")
delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(2)")
delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(3)")
firstpokemon=input("\n")

pokedexfull=list(pokemondata.items())

if firstpokemon=="1":
    Bulbasaur=Pokemon(pokemondata["bulbasaur"],5)
    playername=Player(playername,Bulbasaur)

    delay_print("Congratulations!!!\nBulbasaur is your new Inspermon\n")
    delay_print(Bulbasaur.atributes)

elif firstpokemon=="3":
    Squirtle=Pokemon(pokemondata["squirtle"],5)
    playername=Player(playername,Squirtle)
    delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
    delay_print(Squirtle.atributes)
elif firstpokemon=="2":
    Charmander=Pokemon(pokemondata["charmander"],5)
    playername=Player(playername,Charmander)
    delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
    delay_print(Charmander.atributes)

else:
    playername=Player(playername,0)
    playername.party=[]
    delay_print("I'm sorry {}, but you have to choose your first Inspermon...\n".format((playername.name).title()))
    delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
    delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(2)")
    delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(3)")
    firstpokemon2=input("\n")
    if firstpokemon2=="1":
        Bulbasaur=Pokemon(pokemondata["bulbasaur"],5)
        playername=Player(playername,Bulbasaur)
        delay_print("Congratulations!!!\nBulbasaur is your new Inspermon\n")
        delay_print(Bulbasaur.atributes)
    elif firstpokemon2=="3":
        Charmander=Pokemon(pokemondata["charmander"],5)
        playername=Player(playername,Charmander)
        delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
        delay_print(Charmander.atributes)

    elif firstpokemon2=="2":
        Squirtle=Pokemon(pokemondata["squirtle"],5)
        playername=Player(playername,Squirtle)
        delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
        delay_print(Squirtle.atributes)
    else:
        Pikachu=Pokemon(pokemondata["pikachu"],5)
        playername=Player(playername,Pikachu)
        delay_print("Okay...\nYou win\nCongratulations Pikachu is your new INSPERMON\n")
        delay_print(Pikachu.atributes)



delay_print("\nTo see information of your new INSPERMON, you can always use the INSPERDEX\n\
Your very own INSPERMON legend is about to unfold!\nA world of dreams and adventures with INSPERMON awaits! Let's go!\n")
while True:
    delay_print("You are now in the Insper's Labs\n\
What do you want to do first??\n\
Press (1) for walking around in the LAB\n\
Press (2) for saving the game\n\
Press (3) for looking at your INSPERDEX\n\
Press (4) for sleeping\n")
    action=input()
    if action=="4":
        break
    elif action=="1":
        delay_print("Where do you want to go?\n")
        delay_print("Press (0) for walking around in the Ground Floor\n\
Press (1) for walking around in the First Floor\n\
Press (2) for walking around in the Second Floor\n\
Press (3) for walking around in the Third Floor\n\
Press (4) for walking around in the Fourth Floor\n")
        action=input()
        if action=="0":
            lvlfloor0=rd.randrange(1,6)
            pokemon,atributes=rd.choice(list(pokemondata.items()))
            enemy=Pokemon(pokemondata[pokemon],lvlfloor0)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(pokemon.capitalize(),lvlfloor0))
#             delay_print("What pokemon do you want use to battle?")
#             #delay_print(playername.party[0])
            while (playername.party[0]).hp>0 and enemy.hp>0:
                action=input("Are you going to Attack (1) or Run (2)")
                if action=="2":
                    delay_print("You ran out of the battle...")
                if (playername.party[0]).spd > enemy.spd:
                    delay_print("Your Inspermon's life:{}   Wild {}:{}\n".format(int((playername.party[0]).hp),pokemon.capitalize(),int(enemy.hp)))
                    enemy.hp-=(playername.party[0]).attack(enemy)
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(pokemon))
                        break
                    (playername.party[0]).hp-=enemy.attack(playername.party[0])
                    delay_print("Your Inspermon's life:{}   Wild {}:{}\n".format(int((playername.party[0]).hp),pokemon.capitalize(),int(enemy.hp)))
                elif (playername.party[0]).spd < enemy.spd:
                    delay_print("Your Inspermon's life:{}   Wild {}:{}\n".format(int((playername.party[0]).hp),pokemon.capitalize(),int(enemy.hp)))
                    (playername.party[0]).hp-=enemy.attack(playername.party[0])
                    if (playername.party[0]).hp<0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                    enemy.hp-=(playername.party[0]).attack(enemy)
                    delay_print("Your Inspermon's life:{}   Wild {}:{}\n".format(int((playername.party[0]).hp),pokemon.capitalize(),int(enemy.hp)))
