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
        self.atributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\n".format((self.type).capitalize(),self.lvl,self.hp,self.atk,self.deff,self.spd)

        
    def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)
    
    def lvlup(self):
        if self.exp==25:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==50:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==75:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==100:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==125:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==150:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==175:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==200:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        if self.exp==225:
            self.lvl+=1
            print("Seu pokemon passou para o lvl{}".format(self.lvl))
        return self.lvl
        
# class Player:
#     #Classe do player
    
#     def __init__(self,pokemon):
#         self.pokemon1=
    
    
#     def capture(self,pokemon):










#Status iguias,se eles atacarem juntos a batalha nao fosse em turnos,eles morreriam ao msm tempo
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.01)
ok=True
while ok:
    a=input("passear (0) ou dormir (1): ")
    Charmanderplayer=Pokemon(pokemondata["charmander"],2)
    if a=="1":
        break
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
            acao=input("atacar:0\ncorrer:1\n    ")
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
                    Charmanderplayer.exp+=50
                    Charmanderplayer.lvlup()
                    
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
                    Charmanderplayer.exp+=50
                    Charmanderplayer.lvlup()
 
                elif Charmanderplayer.hp<=0:
                    delay_print("Vc perdeu...\n")
                   
            else:
                print("Digite um comando válido ")  #caso o usuario insira um numero errado
    else:
        print("Digite um comando válido ")
#         return ""