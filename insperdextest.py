import random as rd
#tipos de pokemon
Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]

#Todos os pokemons do jogo
pokemondata={"bulbasaur":{"type":"grass",
                    "dexn":0,
					"hp":45,
					"atk":49,
					"deff":49,
					"spd":40,
					"satk":40},
	"charmander":{"type":"fire",
                    "dexn":1,
					"hp":49,
					"atk":52,
					"deff":43,
					"spd":65,
					"satk":40},
	"meowth":{"type":"normal",
                  "dexn":2,
	              "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":90,
				  "satk":40}}


class Pokemon:
    #classe para pokemons

    def __init__(self,pokemon,lvl):
        self.dexn=pokemon["dexn"]
        self.type=pokemon["type"] #tipo do pokemon
        self.lvl=lvl #lvl do pokemon
        self.hp=(((2*pokemon["hp"]+rd.randrange(1,32)+(50/4))*lvl)/100)+lvl+10 #vida atual do pokemon
        self.atk=(((2*pokemon["atk"]+rd.randrange(1,32)+(50/4))*lvl)/100)+5 #ataque atual do pokemon
        self.deff=(((2*pokemon["deff"]+rd.randrange(1,32)+(50/4))*lvl)/100)+5 #defesa atual do pokemon
        self.spd=(((2*pokemon["spd"]+rd.randrange(1,32)+(50/4))*lvl)/100)+5 #velocidade atual do pokemon
        self.satk=pokemon["satk"]
        self.exp=0
        self.atributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\n".format((self.type).capitalize(),self.lvl,self.hp,self.atk,self.deff,self.spd)


    def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)

import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.01)
insperdex=["???","???","???"]
ok=True
while ok:
    a=input("dormir:(1),passear:(0),checar insperdex:(2)")
    Charmanderplayer=Pokemon(pokemondata["charmander"],2)
    if a=="1":
        break
    if a=="2":
        print(insperdex)
    if a=="0":
        lvlfloor1=rd.randrange(1,11)
        po,atributos=rd.choice(list(pokemondata.items()))
        enemy=Pokemon(pokemondata[po],1)
        mensagem="A wild pokemon appears....\nIt's a {} LvL:{}\n "
        vowals=["a","e","i","o","u"]
        if po[0] in vowals:
            mensagem="A wild pokemon appears....\nIt's an {} Lvl:{}\n "
        delay_print(mensagem.format(po.capitalize(),1))
        while Charmanderplayer.hp>0 and enemy.hp>0:
            acao=input("\natacar:0\ncorrer:1\nregistrar insperdex:3\n")
            if acao=="3":
                insperdex[enemy.dexn]=list(pokemondata)[enemy.dexn]
                print("{} foi registrado na insperdex".format(list(pokemondata)[enemy.dexn]))
            if acao=="1":
                delay_print("Voce correu...\n")
                break
            elif acao=="0" and Charmanderplayer.spd>enemy.spd:
                enemy.hp=enemy.hp-Charmanderplayer.attack(enemy)
                delay_print("sua vida:{} vida do inimigo:{}\n".format(Charmanderplayer.hp,enemy.hp))
                if Charmanderplayer.hp>0 and enemy.hp>0:
                    Charmanderplayer.hp+=-enemy.attack(Charmanderplayer)
                    delay_print("sua vida:{} vida do inimigo:{}\n".format(Charmanderplayer.hp,enemy.hp))
                if enemy.hp<=0:
                    delay_print("Voce venceu!!\n")
                elif Charmanderplayer.hp<=0:
                    delay_print("Vc perdeu...\n")
            elif acao=="0" and Charmanderplayer.spd<enemy.spd:
                Charmanderplayer.hp+=-enemy.attack(Charmanderplayer)
                delay_print("sua vida:{} vida do inimigo:{}\n".format(Charmanderplayer.hp,enemy.hp))
                if Charmanderplayer.hp>0 and enemy.hp>0:
                    enemy.hp=enemy.hp-Charmanderplayer.attack(enemy)
                    delay_print("sua vida:{} vida do inimigo:{}\n".format(Charmanderplayer.hp,enemy.hp))
                if enemy.hp<=0:
                    delau_print("Voce venceu!!\n")
                elif Charmanderplayer.hp<=0:
                    delay_print("Vc perdeu...\n")
