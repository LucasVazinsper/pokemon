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
				  "def":50,
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
        self.atributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\n".format((self.type).capitalize(),self.lvl,int(self.hp),int(self.atk),int(self.deff),
                                                                                             int(self.spd))


    def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)


class Player:
    #classe para o usuário

    def __init__(self,name,pokemon):
        self.party=[pokemon]  #lista de todos os pokemons do player
        self.name="{}".format(name)


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
delay_print("Welcome to the marvelous World of Inspermon")
input()
delay_print("Are you a boy or a girl?\nboy:(1)\ngirl:(2)")
boyorgirl=input("-\n")
while boyorgirl!="1" and boyorgirl!="2":
    print("Type a valid command")
    boyorgirl=input("\n")
delay_print("What is you name young trainer")
playername=input("\n")
playername+=" Ketchum"

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
    Bulbasaur=Pokemon(pokemondata["bulbasaur"],1)
    playername=Player(playername,Bulbasaur)

    delay_print("Congratulations!!!\nBulbasaur is your new pokemon\n")
    delay_print(Bulbasaur.atributes)

elif firstpokemon=="3":
    Squirtle=Pokemon(pokemondata["squirtle"],1)
    playername=Player(playername,pokedexfull[2])
    delay_print("Congratulations!!!\nSquirtle is your new pokemon\n")
    delay_print(Squirtle.atributes)
elif firstpokemon=="2":
    Charmander=Pokemon(pokemondata["charmander"],1)
    playername=Player(playername,pokedexfull[1])
    delay_print("Congratulations!!!\nCharmander is your new pokemon\n")
    delay_print(Charmander.atributes)

else:
    playername=Player(playername,0)
    delay_print("I'm sorry {}, but you have to choose your first pokemon...\n".format(playername.name))
    delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
    delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(2)")
    delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(3)")
    firstpokemon2=input("\n")
    if firstpokemon2=="1":
        Bulbasaur=Pokemon(pokemondata["bulbasaur"],1)
        playername=Player(playername,pokedexfull[0])
        delay_print("Congratulations!!!\nBulbasaur is your new pokemon\n")
        delay_print(Bulbasaur.atributes)
    elif firstpokemon2=="2":
        Squirtle=Pokemon(pokemondata["squirtle"],1)
        playername=Player(playername,pokedexfull[2])
        delay_print("Congratulations!!!\nSquirtle is your new pokemon\n")
        delay_print(Squirtle.atributes)

    elif firstpokemon2=="3":
        Charmander=Pokemon(pokemondata["charmander"],1)
        playername=Player(playername,pokedexfull[1])
        delay_print("Congratulations!!!\nCharmander is your new pokemon\n")
        delay_print(Charmander.atributes)


    else:
        Pikachu=Pokemon(pokemondata["pikachu"],1)
        playername=Player(playername,pokedexfull[6])
        delay_print("Okay...\nYou win\nCongratulations Pikachu is your new pokemon\n")
        delay_print(Pikachu.atributes)



delay_print("\nTo see information of your new pokemon, you can use the insperdex")
