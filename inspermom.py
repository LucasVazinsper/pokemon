import random as rd
#tipos de pokemon
Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]

#Todos os pokemons do jogo
pokemondata={"bulbasaur":{"type":"grass",
                    "name":"Bulbasaur",
                    "dexn":0,
					"hp":45,
					"atk":49,
					"deff":49,
					"spd":40,
					"satk":40},
	"charmander":{"type":"fire",
                    "name":"Charmander",
                    "dexn":3,
					"hp":49,
					"atk":52,
					"deff":43,
					"spd":65,
					"satk":40},
	"squirtle":{"type":"water",
                  "name":"Squirtle",
                  "dexn":6,
				  "hp":44,
                  "atk":50,
				  "deff":65,
				  "spd":43,
				  "satk":40},
	"caterpie":{"type":"bug",
                  "name":"Caterpie",
                  "dexn":9,
				  "hp":45,
				  "atk":30,
				  "deff":35,
				  "spd":45,
				  "satk":40},
	"pidgey":{"type":"flying",
                  "name":"Pidgey",
                  "dexn":12,
				  "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":56,
				  "satk":40},
	"pichu":{"type":"eletric",
                  "name":"Pichu",
                  "dexn":15,
				  "hp":20,
				  "atk":40,
				  "deff":15,
				  "spd":60,
				  "satk":40},
	"abra":{"type":"psychic",
                  "name":"Abra",
                  "dexn":18,
				  "hp":25,
				  "atk":105,
				  "deff":55,
				  "spd":90,
				  "satk":40},
	"machop":{"type":"fighting",
                  "name":"Machop",
                  "dexn":21,
				  "hp":70,
				  "atk":80,
				  "deff":50,
				  "spd":35,
				  "satk":40},
	"gastly":{"type":"ghost",
                  "name":"Gastly",
                  "dexn":24,
				  "hp":30,
				  "atk":100,
				  "deff":35,
				  "spd":80,
				  "satk":40},
	"grimer":{"type":"poison",
                  "name":"Grimer",
                  "dexn":27,
				  "hp":80,
				  "atk":80,
				  "deff":50,
				  "spd":25,
				  "satk":40},
	"rhyhorn":{"type":"rock",
                  "name":"Rhyhorn",
                  "dexn":29,
				  "hp":80,
				  "atk":85,
				  "deff":95,
				  "spd":25,
				  "satk":50},
	"dratini":{"type":"dragon",
                  "name":"Dratini",
                  "dexn":31,
				  "hp":41,
				  "atk":64,
				  "deff":50,
				  "spd":50,
				  "satk":40},
	"bergmite":{"type":"ice",
                  "name":"Bergmite",
                  "dexn":34,
				  "hp":55,
				  "atk":69,
				  "deff":85,
				  "spd":28,
				  "satk":55},
	"sandile":{"type":"ground",
                  "name":"Sandile",
                  "dexn":36,
				  "hp":50,
				  "atk":72,
				  "deff":35,
				  "spd":65,
				  "satk":40},
	"meowth":{"type":"normal",
                  "name":"Meowth",
                  "dexn":39,
				  "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":90,
				  "satk":40}}



pokemondata2={"ivysaur":{"type":"grass",
                    "name":"Ivysaur",
					"dexn":1,
					"hp":60,
					"atk":80,
					"deff":80,
					"spd":60,
					"satk":70},
	"charmeleon":{"type":"fire",
                    "name":"Charmeleon",
				    "dexn":4,
					"hp":58,
					"atk":80,
					"deff":65,
					"spd":80,
					"satk":70},
	"wartortle":{"type":"water",
                  "name":"Wartortle",
				  "dexn":7,
				  "hp":59,
                  "atk":65,
				  "deff":80,
				  "spd":58,
				  "satk":70},
	"metapode":{"type":"bug",
                  "name":"Metapode",
				  "dexn":10,
				  "hp":50,
				  "atk":25,
				  "deff":55,
				  "spd":30,
				  "satk":70},
	"pidgeotto":{"type":"flying",
                  "name":"Pidgeotto",
				  "dexn":13,
				  "hp":63,
				  "atk":60,
				  "deff":55,
				  "spd":71,
				  "satk":70},
	"pikachu":{"type":"eletric",
                "name":"Pikachu",
				  "dexn":16,
				  "hp":35,
				  "atk":50,
				  "deff":50,
				  "spd":90,
				  "satk":70},
	"kadabra":{"Type":"psychic",
                  "name":"Kadabra",
				  "dexn":19,
				  "hp":40,
				  "atk":120,
				  "deff":70,
				  "spd":105,
				  "satk":40},
	"machoke":{"type":"fighting",
                  "name":"Machoke",
				  "dexn":22,
				  "hp":80,
				  "atk":100,
				  "deff":70,
				  "spd":45,
				  "satk":40},
	"haunter":{"type":"ghost",
                  "name":"Haunter",
				  "dexn":25,
				  "hp":45,
				  "atk":115,
				  "deff":55,
				  "spd":95,
				  "satk":70},
	"muk":{"type":"poison",
                  "name":"Muk",
				  "dexn":28,
				  "hp":80,
				  "atk":80,
				  "deff":50,
				  "spd":25,
				  "satk":40},
	"rhyhorn":{"type":"rock",
                  "name":"Rhyhorn",
				  "dexn":29,
				  "hp":80,
				  "atk":85,
				  "deff":95,
				  "spd":25,
				  "satk":50},
	"dragonair":{"type":"dragon",
                  "name":"Dragonair",
				  "dexn":32,
				  "hp":61,
				  "atk":84,
				  "deff":70,
				  "spd":70,
				  "satk":70},
	"bergmite":{"type":"ice",
                  "name":"Bergmite",
				  "dexn":34,
				  "hp":55,
				  "atk":69,
				  "deff":85,
				  "spd":28,
				  "satk":55},
	"krokorok":{"type":"ground",
                  "name":"Krokorok",
				  "dexn":37,
				  "hp":60,
				  "atk":82,
				  "deff":45,
				  "spd":74,
				  "satk":70},
	"persian":{"type":"normal",
                  "name":"Persian",
				  "dexn":40,
				  "hp":65,
				  "atk":70,
				  "deff":65,
				  "spd":115,
				  "satk":80}}

pokemondata3={"venusaur":{"type":"grass",
                    "name":"Venusaur",
                    "dexn":2,
					"hp":80,
					"atk":122,
					"deff":123,
					"spd":80,
					"satk":90},
	"charizard":{"type":"fire",
                    "name":"Charizard",
                    "dexn":5,
                    "hp":78,
					"atk":109,
					"deff":85,
					"spd":100,
					"satk":90},
	"blastoise":{"type":"water",
                  "name":"Blastoise",
                  "dexn":8,
                  "hp":79,
                  "atk":85,
				  "deff":105,
				  "spd":78,
				  "satk":90},
	"butterfree":{"type":"bug",
                  "name":"Butterfree",
                  "dexn":11,
                  "hp":60,
				  "atk":90,
				  "deff":80,
				  "spd":70,
				  "satk":90},
	"pidgeot":{"type":"flying",
                  "name":"Pidgeot",
                  "dexn":14,
                  "hp":83,
				  "atk":80,
				  "deff":75,
				  "spd":101,
				  "satk":90},
	"raichu":{"type":"eletric",
                  "name":"Raichu",
                  "dexn":17,
                  "hp":60,
				  "atk":95,
				  "deff":85,
				  "spd":110,
				  "satk":90},
	"alakazam":{"type":"psychic",
                  "name":"Alakazam",
                  "dexn":20,
                  "hp":55,
				  "atk":135,
				  "deff":70,
				  "spd":120,
				  "satk":90},
	"machamp":{"type":"fighting",
                  "name":"Machamp",
                  "dexn":23,
                  "hp":90,
				  "atk":130,
				  "deff":85,
				  "spd":55,
				  "satk":90},
	"gengar":{"type":"ghost",
                  "name":"Gengar",
                  "dexn":26,
                  "hp":60,
				  "atk":130,
				  "deff":75,
				  "spd":110,
				  "satk":110},
	"muk":{"type":"poison",
                  "name":"Muk",
                  "dexn":28,
                  "hp":105,
				  "atk":105,
				  "deff":100,
				  "spd":50,
				  "satk":90},
	"rhydon":{"type":"rock",
                  "name":"Rhydon",
                  "dexn":30,
                  "hp":105,
				  "atk":130,
				  "deff":120,
				  "spd":40,
				  "satk":90},
	"dragonite":{"type":"dragon",
                  "name":"Dragonite",
                  "dexn":33,
                  "hp":91,
				  "atk":134,
				  "deff":100,
				  "spd":80,
				  "satk":90},
	"avalugg":{"type":"ice",
                  "name":"Avalugg",
                  "dexn":35,
                  "hp":95,
				  "atk":117,
				  "deff":184,
				  "spd":28,
				  "satk":90},
	"krookodile":{"type":"ground",
                  "name":"Krookodile",
                  "dexn":38,
                  "hp":95,
				  "atk":117,
				  "deff":80,
				  "spd":92,
				  "satk":90},
	"persian":{"type":"normal",
                  "name":"Persian",
                  "dexn":40,
                  "hp":65,
				  "atk":70,
				  "deff":65,
				  "spd":115,
				  "satk":80},
    "snorlax":{"type":"normal",
                  "name":"Snorlax",
                  "dexn":41,
                  "hp":160,
              	  "atk":110,
              	  "deff":65,
              	  "spd":30,
              	  "satk":90}}


class Pokemon:
    #classe para pokemons

    def __init__(self,pokemon,lvl):
        self.name=pokemon["name"]
        self.dexn=pokemon["dexn"]
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


    def deffense(self,enemy): #dano recebido pelo pokemon
            effectiveness=[0,0.5,1,2] #dano efetivo recebido pelo pokemon(de acordo com as vantagens/fraquezas)
            dmg=effectiveness[2]
            consolemessage=("It was effective")
            if self.type=="normal"and enemy.type=="rock": #rock é resistente ao normal
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="normal" and enemy.type=="ghost": #ghost é imune ao normal
                consolemessage=("But it failed!")
                dmg=effectiveness[0]

            if self.type=="fire" and enemy.type=="fire":
                consolemessage=("It's not very effective")
                dmg=effectiveness[1]

            if self.type=="fire"and enemy.type=="water":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fire"and enemy.type=="rock":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fire"and enemy.type=="dragon":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fire"and enemy.type=="grass":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="fire"and enemy.type=="ice":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="fire"and enemy.type=="bug":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="fire":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="ground":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="rock":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="water":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="water"and enemy.type=="grass":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="water"and enemy.type=="dragon":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="eletric"and enemy.type=="eletric":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="eletric"and enemy.type=="grass":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="eletric"and enemy.type=="dragon":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="eletric"and enemy.type=="water":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="eletric"and enemy.type=="flying":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="eletric"and enemy.type=="ground":
                consolemessage=("But it failed!")
                dmg=effectiveness[0]

            if self.type=="grass"and enemy.type=="fire":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grass"and enemy.type=="grass":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grass"and enemy.type=="poison":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grass"and enemy.type=="flying":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grass"and enemy.type=="bug":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grass"and enemy.type=="dragon":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grass"and enemy.type=="water":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="grass"and enemy.type=="ground":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="grass"and enemy.type=="rock":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="fire":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="ice"and enemy.type=="water":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]


            if self.type=="ice"and enemy.type=="ice":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="ice"and enemy.type=="grass":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="flying":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="ground":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="dragon":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="fighting"and enemy.type=="poison":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fighting"and enemy.type=="flying":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fighting"and enemy.type=="psychic":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fighting"and enemy.type=="bug":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fighting"and enemy.type=="normal":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="fighting"and enemy.type=="ice":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="fighting"and enemy.type=="rock":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fighting"and enemy.type=="ghost":
                consolemessage=("But it failed!")
                dmg=effectiveness[0]

            if self.type=="poison"and enemy.type=="poison":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="poison"and enemy.type=="ground":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="poison"and enemy.type=="rock":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="poison"and enemy.type=="ghost":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="poison"and enemy.type=="grass":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="grond"and enemy.type=="grass":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grond"and enemy.type=="bug":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grond"and enemy.type=="fire":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="eletric":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="poison":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="rock":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="flying":
                consolemessage=("But it failed!")
                dmg=effectiveness[0]

            if self.type=="flying"and enemy.type=="eletric":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="flying"and enemy.type=="rock":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="flying"and enemy.type=="grass":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="flying"and enemy.type=="fighting":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="flying"and enemy.type=="bug":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="psychic"and enemy.type=="psychic":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="psychic"and enemy.type=="fighting":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="psychic"and enemy.type=="poison":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="bug"and enemy.type=="fire":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="bug"and enemy.type=="fighting":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="bug"and enemy.type=="poison":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="bug"and enemy.type=="flying":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="bug"and enemy.type=="ghost":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="bug"and enemy.type=="grass":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="bug"and enemy.type=="psychic":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="fighting":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="rock"and enemy.type=="ground":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="rock"and enemy.type=="fire":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="ice":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="flying":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="bug":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ghost"and enemy.type=="psychic":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ghost"and enemy.type=="ghost":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            if self.type=="ghost"and enemy.type=="normal":
                consolemessage=("But it failed!")
                dmg=effectiveness[0]

            if self.type=="dragon"and enemy.type=="dragon":
                consolemessage=("It's super effective!")
                dmg=effectiveness[3]

            return [enemy.hp - (self.attack(enemy))*dmg,consolemessage]
            #,consolemessage ##preciso melhorar a implementação, mas essa é a idea
                                                         #agr ja era fion.



class Player():
    #classe para o usuário

    def __init__(self,name,pokemon):
        self.party=[pokemon]  #lista de todos os pokemons do player
        self.name="{}".format(name)
        self.insperdex=["???"]*50


def dex(insperdex):
    for i in insperdex:
        print(i)

numeros=[]
for i in range(10):
    numeros.append("{}".format(i))






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
boyorgirl=input("\n")

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
    playername.insperdex[Bulbasaur.dexn]="{}-{}:{}".format(Bulbasaur.dexn,Bulbasaur.name,Bulbasaur.type)
elif firstpokemon=="3":
    Squirtle=Pokemon(pokemondata["squirtle"],5)
    playername=Player(playername,Squirtle)
    delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
    delay_print(Squirtle.atributes)
    playername.insperdex[Squirtle.dexn]="{}-{}:{}".format(Squirtle.dexn,Squirtle.name,Bulbasaur.type)
elif firstpokemon=="2":
    Charmander=Pokemon(pokemondata["charmander"],5)
    playername=Player(playername,Charmander)
    delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
    delay_print(Charmander.atributes)
    playername.insperdex[Charmander.dexn]="{}-{}:{}".format(Charmander.dexn,Charmander.name,Charmander.type)
else:
    playername=Player(playername,0)
    playername.party=[]
    delay_print("I'm sorry {}, but you have to choose your first Inspermon...\n".format((playername.name).title()))
    delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
    delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(2)")
    delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(3)")
    firstpokemon2=input("\n")
    if firstpokemon2=="1":
        Bulbasaur=Pokemon(pokemondata["bulbasaur"],5)
        playername=Player(playername,Bulbasaur)
        delay_print("Congratulations!!!\nBulbasaur is your new Inspermon\n")
        delay_print(Bulbasaur.atributes)
        playername.insperdex[Bulbasaur.dexn]="{}-{}:{}".format(Bulbasaur.dexn,Bulbasaur.name,Bulbasaur.type)
    elif firstpokemon2=="2":
        Charmander=Pokemon(pokemondata["charmander"],5)
        playername=Player(playername,Charmander)
        delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
        delay_print(Charmander.atributes)
        playername.insperdex[Squirtle.dexn]="{}-{}:{}".format(Squirtle.dexn,Squirtle.name,Bulbasaur.type)

    elif firstpokemon2=="3":
        Squirtle=Pokemon(pokemondata["squirtle"],5)
        playername=Player(playername,Squirtle)
        delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
        delay_print(Squirtle.atributes)
        playername.insperdex[Charmander.dexn]="{}-{}:{}".format(Charmander.dexn,Charmander.name,Charmander.type)
    else:
        Pikachu=Pokemon(pokemondata2["pikachu"],10)
        playername=Player(playername,Pikachu)
        delay_print("Okay...\nYou win\nCongratulations Pikachu is your new INSPERMON\n")
        delay_print(Pikachu.atributes)
        playername.insperdex[Pikachu.dexn]="{}-{}:{}".format(Pikachu.dexn,Pikachu.name,Pikachu.type)



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
    if action=="3":
        dex(playername.insperdex)
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
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            delay_print("What pokemon do you want to use to battle?\n")
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command")
                choose=input()
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:
                choice=input("Are you going to Attack (1) or Run (2) or Check Status(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    break
                if choice=="3":
                    print("ronaldo")

                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break

        elif action=="1":
            lvlfloor1=rd.randrange(5,20)
            pokemon,atributes=rd.choice(list(pokemondata.items()))
            enemy=Pokemon(pokemondata[pokemon],lvlfloor1)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(pokemon.capitalize(),lvlfloor1))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()

            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:
                choice=input("Are you going to Attack (1) or Run (2) or Check Status(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    break
                if choice=="3":
                    print("ronaldo")

                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break


        elif action=="2":
            lvlfloor2=rd.randrange(20,31)
            pokemon,atributes=rd.choice(list(pokemondata2.items()))
            enemy=Pokemon(pokemondata2[pokemon],lvlfloor2)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(pokemon.capitalize(),lvlfloor2))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:
                choice=input("Are you going to Attack (1) or Run (2) or Check Status(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    break
                if choice=="3":
                    print("ronaldo")

                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break

        elif action=="3":
            lvlfloor3=rd.randrange(30,41)
            pokemon,atributes=rd.choice(list(pokemondata2.items()))
            enemy=Pokemon(pokemondata2[pokemon],lvlfloor3)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(pokemon.capitalize(),lvlfloor3))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:
                choice=input("Are you going to Attack (1) or Run (2) or Check Status(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    break
                if choice=="3":
                    print("ronaldo")

                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break


        elif action=="4":
            lvlfloor4=rd.randrange(40,51)
            pokemon,atributes=rd.choice(list(pokemondata3.items()))
            enemy=Pokemon(pokemondata3[pokemon],lvlfloor4)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(pokemon.capitalize(),lvlfloor4))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:
                choice=input("Are you going to Attack (1) or Run (2) or Check Status(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    break
                if choice=="3":
                    print("ronaldo")

                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    (playername.party[int(choose)]).hp=(enemy.deffense(playername.party[int(choose)]))[0]
                    print((enemy.deffense(playername.party[int(choose)]))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        break
                    enemy.hp=((playername.party[int(choose)]).deffense(enemy))[0]
                    print(((playername.party[int(choose)]).deffense(enemy))[1])
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        break
