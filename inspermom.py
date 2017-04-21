import random as rd
import pickle
import colorama
from colorama import Fore, Back, Style
colorama.init()
import time
import sys
########################################
n=0                # lista de experiencia para cada level, onde n = level
exp_list=[]
for i in range(1,101):
    n=n+1
    exp=0.8*(n)**3
    exp_list.append(int(exp))

#########################################

#Todos os pokemons do jogo

pickle_in=open("pokemondata.pickle","rb") #Carrega o dicionario com as informacoes de cada pokemon

pokemondata=pickle.load(pickle_in)



class Pokemon:
    #classe para pokemons

    def __init__(self,pokemon,lvl):
        self.floor=pokemon["floor"] #andar no qual cada pokemon pode aparecer
        self.evolution=pokemon["evolution"] #nome da evolução
        self.all=pokemon #todos os atributos basicos do pokemon
        self.ivhp=rd.randrange(1,32) #individual value para a vida do pokemon (deixa todos os pokemons diferentes entre si)
        self.ivatk=rd.randrange(1,32) #individual value para a ataque do pokemon (deixa todos os pokemons diferentes entre si)
        self.ivdeff=rd.randrange(1,32) #individual  value para a defesa do pokemon (deixa todos os pokemons diferentes entre si)
        self.ivspd=rd.randrange(1,32) #individual  value para a velocidade do pokemon (deixa todos os pokemons diferentes entre si)
        self.lvlevolution=pokemon["lvlev"] #level que cada pokemon evolui
        self.basexp=pokemon["xp"] #experiencia base que cada pokemon fornece qnd é fainted "morto"
        self.name=pokemon["name"] #nome do Inspermon
        self.dexn=pokemon["dexn"] #numero da INSPERDEX
        self.type=pokemon["type"] #tipo do pokemon
        self.lvl=lvl #lvl do pokemon
        self.hp=(((2*pokemon["hp"]+self.ivhp+(50/4))*lvl)/100)+lvl+10 #equacao que gera a vida apartir da vida base
        self.atk=(((2*pokemon["atk"]+self.ivatk+(50/4))*lvl)/100)+5 #equacao que gera a vida apartir do ataque base
        self.deff=(((2*pokemon["deff"]+self.ivdeff+(50/4))*lvl)/100)+5 #equacao que gera a vida apartir da defesa base
        self.spd=(((2*pokemon["spd"]+self.ivspd+(50/4))*lvl)/100)+5 #equacao que gera a velocidade apartir da velocidade base
        self.maxhp=(((2*pokemon["hp"]+self.ivhp+(50/4))*lvl)/100)+lvl+10 #vida máxima do pokemon
        self.satk=pokemon["satk"] #poder do golpe que sera usado na equacao de dano
        self.exp=(4*(lvl**3))/5 #experiencia do pokemon
        self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
                                                                                             int(self.atk),int(self.deff),int(self.spd),int(self.exp))


    def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)


    def damage(self,enemy): #dano do ataque do pokemon com vantagens/fraquezas
            effectiveness=[0,0.5,1,2] #dano efetivo recebido pelo pokemon(de acordo com as vantagens/fraquezas)
            dmg=effectiveness[2]
            consolemessage=("It was effective\n")

            if self.type=="normal"and enemy.type=="rock": #rock é resistente ao normal
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="normal" and enemy.type=="ghost": #ghost é imune ao normal
                consolemessage=("But it failed...")
                dmg=effectiveness[0]

            if self.type=="fire" and enemy.type=="fire":
                consolemessage=("It's not very effective...")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="fire"and enemy.type=="ice":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="fire"and enemy.type=="bug":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="fire":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="ground":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="water"and enemy.type=="rock":
                consolemessage=("It's super effective!!!")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="eletric"and enemy.type=="flying":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="eletric"and enemy.type=="ground":
                consolemessage=("But it failed...")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="grass"and enemy.type=="ground":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="grass"and enemy.type=="rock":
                consolemessage=("It's super effective!!!")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="flying":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="ground":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ice"and enemy.type=="dragon":
                consolemessage=("It's super effective!!!")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="fighting"and enemy.type=="ice":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="fighting"and enemy.type=="rock":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="fighting"and enemy.type=="ghost":
                consolemessage=("But it failed...")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="grond"and enemy.type=="grass":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grond"and enemy.type=="bug":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="grond"and enemy.type=="fire":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="eletric":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="poison":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="rock":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ground"and enemy.type=="flying":
                consolemessage=("But it failed...")
                dmg=effectiveness[0]

            if self.type=="flying"and enemy.type=="eletric":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="flying"and enemy.type=="rock":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="flying"and enemy.type=="grass":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="flying"and enemy.type=="fighting":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="flying"and enemy.type=="bug":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="psychic"and enemy.type=="psychic":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="psychic"and enemy.type=="fighting":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="psychic"and enemy.type=="poison":
                consolemessage=("It's super effective!!!")
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
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="bug"and enemy.type=="psychic":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="fighting":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="rock"and enemy.type=="ground":
                consolemessage=("It's not very effective...")
                dmg=effectiveness[1]

            if self.type=="rock"and enemy.type=="fire":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="ice":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="flying":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="rock"and enemy.type=="bug":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ghost"and enemy.type=="psychic":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ghost"and enemy.type=="ghost":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]

            if self.type=="ghost"and enemy.type=="normal":
                consolemessage=("But it failed...")
                dmg=effectiveness[0]

            if self.type=="dragon"and enemy.type=="dragon":
                consolemessage=("It's super effective!!!")
                dmg=effectiveness[3]


            critical=rd.randrange(0,101)
            if critical <=10:
                #10% de chance de um ataque ser critico
                consolemessage+=("\nA critical hit!!!\n")
                enemy.hp-=((self.attack(enemy)*2))*dmg
                if enemy.hp<0:
                    enemy.hp=0
            elif critical >=95:
                #5% de chance de um ataque dar miss
                consolemessage+=("\n{}'s attack missed...".format(self.name))
                enemy.hp-=(((self.attack(enemy)*0))*dmg)

            else:
                enemy.hp-=(self.attack(enemy))*dmg
                if enemy.hp<0:
                    enemy.hp=0

            delay_print("{} caused {} HP of damage\n".format(self.name,int((enemy.maxhp)-(enemy.hp))))
            return delay_print("{}\n".format(consolemessage))
            #,consolemessage ##preciso melhorar a implementação, mas essa é a idea
                                                         #agr ja era fion.


    def lvlup(self,exp_list): #metodo para o pokemon passar de level
        #lvlup(self,exp_list,evolution):
        new_level=0
        for valor in exp_list:
            if self.exp >= valor:
                new_level+=1
            else:
                if self.lvl!=new_level:
                    self.lvl=new_level
                    delay_print("Your {} leveled up to LVL:{}\n".format(self.name,self.lvl))
                    self.hp=(((2*self.all["hp"]+self.ivhp+(50/4))*self.lvl)/100)+self.lvl+10 #vida atual do pokemon
                    self.atk=(((2*self.all["atk"]+self.ivatk+(50/4))*self.lvl)/100)+5 #ataque atual do pokemon
                    self.deff=(((2*self.all["deff"]+self.ivdeff+(50/4))*self.lvl)/100)+5 #defesa atual do pokemon
                    self.spd=(((2*self.all["spd"]+self.ivspd+(50/4))*self.lvl)/100)+5 #velocidade atual do pokemon
                    self.maxhp=(((2*self.all["hp"]+self.ivhp+(50/4))*self.lvl)/100)+self.lvl+10 #vida máxima do pokemon
                    self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
                                                                                                         (self.atk),int(self.deff),int(self.spd),int(self.exp))
                    self.evolving(pokemondata[self.evolution])
                delay_print("Your {}'s experience:{} of {} to the next Level...\n".format(self.name,int(self.exp),valor))
                break


    def expgain(self,enemy):
        self.exp+=((enemy.basexp*enemy.lvl)/7)*3  #experiencia ganha multiplicada para passar de level mais rapido
        self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
                                                                                             (self.atk),int(self.deff),int(self.spd),int(self.exp))
        return self.exp


    def evolving(self,evolution):
        #método de evolução para os pokemons
        if self.lvl>=self.lvlevolution:
            oldname=self.name
            self.floor=evolution["floor"] #andar no qual cada pokemon pode aparecer
            self.evolution=evolution["evolution"] #nome da evolução
            self.lvlevolution=evolution["lvlev"] #level que cada pokemon evolui
            self.all=evolution #todos os atributos basicos do pokemon
            self.basexp=evolution["xp"] #experiencia base que cada pokemon fornece qnd é fainted "morto"
            self.name=evolution["name"] #nome do Inspermon
            self.dexn=evolution["dexn"] #numero da INSPERDEX
            self.type=evolution["type"] #tipo do pokemon
            self.hp=(((2*evolution["hp"]+self.ivhp+(50/4))*self.lvl)/100)+self.lvl+10 #vida atual do pokemon
            self.atk=(((2*evolution["atk"]+self.ivatk+(50/4))*self.lvl)/100)+5 #ataque atual do pokemon
            self.deff=(((2*evolution["deff"]+self.ivdeff+(50/4))*self.lvl)/100)+5 #defesa atual do pokemon
            self.spd=(((2*evolution["spd"]+self.ivspd+(50/4))*self.lvl)/100)+5 #velocidade atual do pokemon
            self.maxhp=(((2*evolution["hp"]+self.ivhp+(50/4))*self.lvl)/100)+self.lvl+10 #vida máxima do pokemon
            self.satk=evolution["satk"] #ataque especial do pokemon
            self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
                                                                                                 int(self.atk),int(self.deff),int(self.spd),int(self.exp))
            playername.dexregister(self)
            return delay_print("What?....\nYour Inspermon is evolving!!!!\nCongratulations! Your {} evolved into {}\n".format(oldname,self.name))


class Player():
    #classe para o usuário

    def __init__(self,name,pokemon):
        self.party=[pokemon]  #lista com os pokemons do time do player (maximo de 6 pokemons)
        self.name="{}".format(name) #nome do jogador
        self.insperdex=["???"]*50 #numero da insperdex
        self.box=[] #lista com todos os pokemons do player


    def dex(self,insperdex):
        #metodo para a insperdex
        for i in insperdex:
            print(i)


    def dexregister(self,inspermon):
        #metodo para registrar a insperdex
        self.insperdex[inspermon.dexn]="{}-{}:{}".format(inspermon.dexn,inspermon.name,(inspermon.type).capitalize())
        return


    def savegame(self):
        # metodo para salvar o jogo
        pickle_out=open("dados.pickle","wb")
        pickle.dump(self,pickle_out)
        pickle_out.close()


    def capture(self,pokemon):
        #metodo para capturar o pokemon
        chance=(100-(100*((pokemon.hp)/pokemon.maxhp)))
        lucky=rd.randrange(0,101)
        if lucky<=chance:
            if len(self.party)>=6:
                pokemon.hp=pokemon.maxhp
                (self.box).append(pokemon)
                delay_print("Your party is full, the new inspermon was moved to your box\n")
            else:
                pokemon.hp=pokemon.maxhp
                (self.party).append(pokemon)
            return delay_print("Congratulations!!!\nThe Wild {} was caught!!!\n".format(pokemon.name))
        else:
            delay_print("I'm sorry, the inspermon broke off\n")


    def showparty(self):
        delay_print("-[Daniel]:Hello {}!Welcome back to the LAB!!\nWhat do you want??\n\
        ----------------------------------------------\n\
        Press (1) to see your party Inspermons\n\
        Press (2) To see your box Inspermons\n\
        Press (3) To edit your party\n\
        ----------------------------------------------\n".format(playername.name))
        choice=input()

        if choice=="1":
            partymon=self.pokemonpicker(1)
            delay_print(partymon.attributes)
        if choice=="2":
            if len(self.box)>0:
                boxmon=self.pokemonpicker(2)
                delay_print(boxmon.attributes)
            else:
                delay_print("You don't have any Inspermons on your Box\n")
        if choice=="3":
            if len(self.box)>0:
                delay_print("-[Daniel]: Choose which Inspermon you want to put in your party\n")
                boxmon=self.pokemonpicker(2)
                delay_print("-[Daniel]: Now you can choose which Inspermon you want to trade and put in your box\n")
                partymon=self.pokemonpicker(1)
                delay_print("-[Daniel]: Are you sure you want to swap this inspermons Box: {} and Party: {} \nFor YES Press (1)\nFor NO Press (2)\n".format(boxmon.name,partymon.name))
                sure=input()
                while sure not in ["1","3"]:
                    delay_print("Type a valid command\n")
                    sure=input()
                if sure=="1":
                    (self.box).pop(int(choose))
                    (self.party).pop(int(choose2))
                    (self.party).append(boxmon)
                    (self.box).append(partymon)
                    delay_print("-[Daniel]: Now your party has been updated\n")
                    for i in range(len(self.party)):
                        delay_print(" {} ({}).\n".format((self.party[i]).name,i))
            else:
                delay_print("You don't have any Inspermons on your Box\n")


    def pokemonpicker(self,num):
        if num==1: # escolher o pokemon da party
            numeros=[]
            for i in range(len(self.party)):
                delay_print("For {} Lvl:{} press ({}).\n".format(self.party[i].name,self.party[i].lvl,i))
                numeros.append("{}".format(i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command\n")
                choose=input()
            delay_print("You choosed {}!!\n".format((self.party[int(choose)]).name))
            return self.party[int(choose)]
        if num==2: # escolher o pokemon da box
            numeros=[]
            for k in range(len(self.box)):
                delay_print("For {} press ({}).\n".format((self.box[k]).name,k))
                numeros.append("{}".format(k))
            choose=input()
            while choose not in numeros:
                delay_print("Type a valid command\n")
                choose=input()
            delay_print("You choosed {}!!\n".format((self.party[int(choose)]).name))
            return self.box[int(choose)]



def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.001)


def restorelife(playerpokemon):
    delay_print("Press (1) if you want to use a Health Potion on your Inspermom or (2) if you wish to continue: ")
    hp_potion=input()
    if hp_potion=="1":
        playerpokemon.hp=playerpokemon.maxhp
        return delay_print("Your {} is healed!!!".format((playerpokemon.name)))


def floorpokemons(floor,pokemondatabase):
    pokemondict={}
    for i in pokemondatabase.keys():
        if (floor) in pokemondatabase[i]["floor"]:
            pokemondict[i]=(pokemondatabase[i])

    return pokemondict


def pokemongenerator(floor):
    if floor=="0":
        lvlfloor=rd.randrange(1,6)
    elif floor=="1":
        lvlfloor=rd.randrange(5,20)
    elif floor=="2":
        lvlfloor=rd.randrange(20,31)
    elif floor=="3":
        lvlfloor=rd.randrange(30,41)
    elif floor=="4":
        lvlfloor=rd.randrange(40,51)

    pokemon,attributes=rd.choice(list((floorpokemons(floor,pokemondata)).items()))
    enemy=Pokemon(pokemondata[pokemon],lvlfloor)
    return enemy


def choosepokemon(enemy):
    pokemongenerator(action)
    delay_print("A wild {} Level:{} appears...\n".format(enemy.name,enemy.lvl))
    playername.dexregister(enemy)
    delay_print("The untamed {} was registered in your INSPERDEX\n".format(enemy.name))
    delay_print("A battle is about to begin...\n")
    delay_print("What pokemon do you want to use to battle?\n")
    return playername.pokemonpicker(1),enemy

def showlife(playerpokemon):
    delay_print("-------------------------------------------------------------------------\n\
|Your {}'s HP:{}/{} |                      |Wild {} HP:{}/{}|\n\
-------------------------------------------------------------------------\n".format((playerpokemon[0]).name,
    int((playerpokemon[0]).hp),int((playerpokemon[0]).maxhp),playerpokemon[1].name,int(playerpokemon[1].hp),int(playerpokemon[1].maxhp)))

def batalha(playerpokemon):
    while playerpokemon[0].hp>0 and playerpokemon[1].hp>0:  ## onde playerpokemon[0] é o pokemon do player e o playerpokemon[1] é o inimigo
        choice=input("Are you going to Attack (1), Run (2), Check Status on INSPERDEX(3) or try to catch it (4):\n")
        if choice=="4":
            playername.capture(playerpokemon[1])
            restorelife(playerpokemon[0])
            break
        if choice=="2":
            delay_print("You ran out of the battle...\n")
            restorelife(playerpokemon[0])
            break
        elif choice=="3":
            print("Your {}\n{}\nWild {}\n{}\n".format((playerpokemon[0]).name,(playerpokemon[0]).attributes,playerpokemon[1].name,playerpokemon[1].attributes))
        elif choice=="1" and (playerpokemon[0]).spd >= playerpokemon[1].spd:
            showlife(playerpokemon)
            delay_print("Your {} Attacked...\n".format((playerpokemon[0]).name))
            ((playerpokemon[0]).damage(playerpokemon[1]))
            showlife(playerpokemon)
            if playerpokemon[1].hp<1:
                delay_print("The enemy {} fainted...\nYou won!!!\n".format(playerpokemon[1].name))
                (playerpokemon[0]).expgain(playerpokemon[1])
                (playerpokemon[0]).lvlup(exp_list)
                restorelife(playerpokemon[0])
                break
            delay_print("Wild {} Attacked...\n".format(playerpokemon[1].name))
            (playerpokemon[1].damage(playerpokemon[0]))
            showlife(playerpokemon)
            if (playerpokemon[0]).hp<1:
                delay_print("Your pokemon fainted...\nYou loose!!!\n")
                restorelife(playerpokemon[0])
                break
        elif choice=="1" and (playerpokemon[0]).spd < playerpokemon[1].spd:
            showlife(playerpokemon)
            delay_print("Wild {} Attacked...\n".format(playerpokemon[1].name))
            (playerpokemon[1].damage(playerpokemon[0]))
            showlife(playerpokemon)
            if (playerpokemon[0]).hp<1:
                delay_print("Your pokemon fainted...\nYou loose!!!\n")
                restorelife(playerpokemon[0])
                break
            delay_print("Your {} Attacked...\n".format((playerpokemon[0]).name))
            ((playerpokemon[0]).damage(playerpokemon[1]))
            showlife(playerpokemon)
            if playerpokemon[1].hp<1:
                delay_print("The enemy {} fainted...\nYou won!!!\n".format(playerpokemon[1].name))
                (playerpokemon[0]).expgain(playerpokemon[1])
                (playerpokemon[0]).lvlup(exp_list)
                restorelife(playerpokemon[0])
                break

delay_print("New Game:(1)\n  Load  :(2)")
game=input()
while game not in ["1","2"]:
    print("Type a valid command")
    game=input()

if game=="1":
    delay_print("Welcome to the marvelous World of Inspermon")
    input()
    delay_print("You are at Proffesor Daniel's Inspermon Research lab\n")

    delay_print("\n-[Daniel]: Hello there! Welcome to the world of INSPERMON! My name is Daniel! People call me the INSPERMON Prof!\n")
    input()
    delay_print("\n-[Daniel]: This world is inhabited by creatures called INSPERMON!\n")
    input()
    delay_print("\n-[Daniel]: For some people, INSPERMON are pets. Other use them for fights. Myself… I study INSPERMON as a profession.\n")
    input()
    delay_print("\n-[Daniel]: First, what is your name?\n")
    playername=input("\n")
    playername+=" Ketchum"
    delay_print("-[Daniel]: Right! So your name is {}!".format(playername.title()))
    delay_print("[Daniel]: Are you a boy or a girl?\nboy:(1)\ngirl:(2)")
    boyorgirl=input("\n")

    while boyorgirl!="1" and boyorgirl!="2":
        print("Type a valid command")
        boyorgirl=input("\n")

    delay_print("-[Daniel]: Well done {}.Let's get it started!\n".format(playername.title()))
    input()
    delay_print("-[Daniel]: First you have to get your new partner\n")
    input()
    delay_print("-[Daniel]: What do you prefer?")
    delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
    delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(2)")
    delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(3)")
    firstpokemon=input("\n")

    pokedexfull=list(pokemondata.items())

    if firstpokemon=="1":
        Bulbasaur=Pokemon(pokemondata["bulbasaur"],5)
        playername=Player(playername,Bulbasaur)
        delay_print("Congratulations!!!\nBulbasaur is your new Inspermon\n")
        delay_print(Bulbasaur.attributes)
        playername.dexregister(Bulbasaur)
    elif firstpokemon=="3":
        Squirtle=Pokemon(pokemondata["squirtle"],5)
        playername=Player(playername,Squirtle)
        delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
        delay_print(Squirtle.attributes)
        playername.dexregister(Squirtle)
    elif firstpokemon=="2":
        Charmander=Pokemon(pokemondata["charmander"],5)
        playername=Player(playername,Charmander)
        delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
        delay_print(Charmander.attributes)
        playername.dexregister(Charmander)
    else:
        playername=Player(playername,0)
        playername.party=[]
        delay_print("-[Daniel]: I'm sorry {}, but you have to choose your first Inspermon...\n".format((playername.name).title()))
        delay_print(Fore.GREEN+"\nGrass"+Fore.BLACK+":(1)")
        delay_print(Fore.RED+"\nFire"+Fore.BLACK+":(2)")
        delay_print(Fore.BLUE+"\nWater"+Fore.BLACK+":(3)")
        firstpokemon2=input("\n")
        if firstpokemon2=="1":
            Bulbasaur=Pokemon(pokemondata["bulbasaur"],5)
            playername=Player(playername,Bulbasaur)
            delay_print("Congratulations!!!\nBulbasaur is your new Inspermon\n")
            delay_print(Bulbasaur.attributes)
            playername.dexregister(Bulbasaur)
        elif firstpokemon2=="3":
            Squirtle=Pokemon(pokemondata["squirtle"],5)
            playername=Player(playername,Squirtle)
            delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
            delay_print(Squirtle.attributes)
            playername.dexregister(Squirtle)

        elif firstpokemon2=="2":
            Charmander=Pokemon(pokemondata["charmander"],5)
            playername=Player(playername,Charmander)
            delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
            delay_print(Charmander.attributes)
            playername.dexregister(Charmander)
        else:
            Pikachu=Pokemon(pokemondata["pikachu"],10)
            playername=Player(playername,Pikachu)
            delay_print("\nPIKA PIKA!!!\nOkay...\nYou win\nCongratulations Pikachu is your new INSPERMON\n")
            delay_print(Pikachu.attributes)
            playername.dexregister(Pikachu)

    delay_print("\n-[Daniel]:To see information of your new INSPERMON, you can always use the INSPERDEX.It also can be used in battle for acquiring knowledge of yours enemies strength.\n\
Your very own INSPERMON legend is about to unfold!\nA world of dreams and adventures with INSPERMON awaits! Let's go!\n")

if game=="2":
    pickle_in=open("dados.pickle","rb")
    playername=pickle.load(pickle_in)
    delay_print("Your game has been loaded...\nWelcome Back {}!!!\n".format(playername.name))


while True:
    delay_print("You are now in the Insper's Labs\n\
\n What do you want to do first??\n\
----------------------------------------------\n\
Press (1) to explore the Insper Building\n\
Press (2) for saving the game\n\
Press (3) for looking at your INSPERDEX\n\
Press (4) to access your pokemons\n\
Press (5) for sleeping\n\
----------------------------------------------\n")
    action=input()
    if action=="5":
        delay_print("Good night.")
        break
    if action=="2":
        playername.savegame()
        delay_print("Your game has been saved!\n")
    if action=="4":
        playername.showparty()

    if action=="3":
        print("/////////////////////////////////////////////////////////////")
        playername.dex(playername.insperdex)
        print("/////////////////////////////////////////////////////////////")
    elif action=="1":
        delay_print("Where do you want to go?\n")
        delay_print("----------------------------------------------\n\
Press (0) for walking around in the Ground Floor\n\
Press (1) for walking around in the First Floor\n\
Press (2) for walking around in the Second Floor\n\
Press (3) for walking around in the Third Floor\n\
Press (4) for walking around in the Fourth Floor\n\
Press (5) to exit walking around\n\
----------------------------------------------\n")
        action=input()
        if action=="5":
            continue

        else:
            while action not in ["0","1","2","3","4","5"]:
                delay_print("Type a valid command: \n")
                action=input()
            floorpokemons(action,pokemondata)
            batalha(((choosepokemon((pokemongenerator(action))))))
