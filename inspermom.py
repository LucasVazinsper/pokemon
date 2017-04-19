import random as rd
#tipos de pokemon
Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]


n=0
exp_list=[]
for i in range(1,101):
    n=n+1
    exp=0.8*(n)**3
    exp_list.append(int(exp))



#Todos os pokemons do jogo
pokemondata={"bulbasaur":{"type":"grass",
                    "name":"Bulbasaur",
                    "dexn":0,
					"hp":45,
					"atk":49,
					"deff":49,
					"spd":40,
                    "xp":64,
                    "lvlev":7,
                    "floor":[0,1],
                    "evolution":"ivysaur",
					"satk":40},
	"charmander":{"type":"fire",
                    "name":"Charmander",
                    "dexn":3,
					"hp":49,
					"atk":52,
					"deff":43,
					"spd":65,
                    "xp":62,
                    "lvlev":7,
                    "floor":[0,1],
                    "evolution":"charmander",
					"satk":40},
	"squirtle":{"type":"water",
                  "name":"Squirtle",
                  "dexn":6,
				  "hp":44,
                  "atk":50,
				  "deff":65,
				  "spd":43,
                  "xp":63,
                  "lvlev":16,
                  "floor":[0,1],
                  "evolution":"wartortle",
				  "satk":40},
	"caterpie":{"type":"bug",
                  "name":"Caterpie",
                  "dexn":9,
				  "hp":45,
				  "atk":30,
				  "deff":35,
				  "spd":45,
                  "xp":39,
                  "lvlev":7,
                  "floor":[0,1],
                  "evolution":"metapode",
				  "satk":40},
	"pidgey":{"type":"flying",
                  "name":"Pidgey",
                  "dexn":12,
				  "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":56,
                  "xp":50,
                  "lvlev":18,
                  "floor":[0,1],
                  "evolution":"pidgeotto",
				  "satk":40},
	"pichu":{"type":"eletric",
                  "name":"Pichu",
                  "dexn":15,
				  "hp":20,
				  "atk":40,
				  "deff":15,
				  "spd":60,
                  "xp":41,
                  "lvlev":10,
                  "floor":[0,1],
                  "evolution":"pikachu",
				  "satk":40},
	"abra":{"type":"psychic",
                  "name":"Abra",
                  "dexn":18,
				  "hp":25,
				  "atk":105,
				  "deff":55,
				  "spd":90,
                  "xp":62,
                  "lvlev":16,
                  "floor":[0,1],
                  "evolution":"kadabra",
				  "satk":40},
	"machop":{"type":"fighting",
                  "name":"Machop",
                  "dexn":21,
				  "hp":70,
				  "atk":80,
				  "deff":50,
				  "spd":35,
                  "xp":61,
                  "lvlev":28,
                  "floor":[0,1],
                  "evolution":"machoke",
				  "satk":40},
	"gastly":{"type":"ghost",
                  "name":"Gastly",
                  "dexn":24,
				  "hp":30,
				  "atk":100,
				  "deff":35,
				  "spd":80,
                  "xp":62,
                  "lvlev":25,
                  "floor":[0,1],
                  "evolution":"haunter",
				  "satk":40},
	"grimer":{"type":"poison",
                  "name":"Grimer",
                  "dexn":27,
				  "hp":80,
				  "atk":80,
				  "deff":50,
				  "spd":25,
                  "xp":65,
                  "lvlev":38,
                  "floor":[0,1],
                  "evolution":"muk",
				  "satk":40},
	"rhyhorn":{"type":"rock",
                  "name":"Rhyhorn",
                  "dexn":29,
				  "hp":80,
				  "atk":85,
				  "deff":95,
				  "spd":25,
                  "xp":69,
                  "lvlev":42,
                  "floor":[0,1],
                  "evolution":"rhydon",
				  "satk":50},
	"dratini":{"type":"dragon",
                  "name":"Dratini",
                  "dexn":31,
				  "hp":41,
				  "atk":64,
				  "deff":50,
				  "spd":50,
                  "xp":60,
                  "lvlev":42,
                  "floor":[0,1],
                  "evolution":"dragonair",
				  "satk":40},
	"bergmite":{"type":"ice",
                  "name":"Bergmite",
                  "dexn":34,
				  "hp":55,
				  "atk":69,
				  "deff":85,
				  "spd":28,
                  "xp":61,
                  "lvlev":37,
                  "floor":[0,1],
                  "evolution":"avalugg",
				  "satk":55},
	"sandile":{"type":"ground",
                  "name":"Sandile",
                  "dexn":36,
				  "hp":50,
				  "atk":72,
				  "deff":35,
				  "spd":65,
                  "xp":58,
                  "lvlev":29,
                  "floor":[0,1],
                  "evolution":"krokorok",
				  "satk":40},
	"meowth":{"type":"normal",
                  "name":"Meowth",
                  "dexn":39,
				  "hp":40,
				  "atk":45,
				  "deff":40,
				  "spd":90,
                  "xp":58,
                  "lvlev":28,
                  "floor":[0,1],
                  "evolution":"persian",
				  "satk":40}}








pokemondata2={"ivysaur":{"type":"grass",
                    "name":"Ivysaur",
					"dexn":1,
					"hp":60,
					"atk":80,
					"deff":80,
					"spd":60,
                    "xp":142,
                    "lvlev":35,
                    "floor":[2,3],
                    "evolution":"venusaur",
					"satk":70},
	"charmeleon":{"type":"fire",
                    "name":"Charmeleon",
				    "dexn":4,
					"hp":58,
					"atk":80,
					"deff":65,
					"spd":80,
                    "xp":142,
                    "lvlev":36,
                    "floor":[2,3],
                    "evolution":"charizard",
					"satk":70},
	"wartortle":{"type":"water",
                  "name":"Wartortle",
				  "dexn":7,
				  "hp":59,
                  "atk":65,
				  "deff":80,
				  "spd":58,
                  "xp":142,
                  "lvlev":36,
                  "floor":[2,3],
                  "evolution":"blastoise",
				  "satk":70},
	"metapode":{"type":"bug",
                  "name":"Metapode",
				  "dexn":10,
				  "hp":50,
				  "atk":25,
				  "deff":55,
				  "spd":30,
                  "xp":72,
                  "lvlev":11,
                  "floor":[2,3],
                  "evolution":"butterfree",
				  "satk":70},
	"pidgeotto":{"type":"flying",
                  "name":"Pidgeotto",
				  "dexn":13,
				  "hp":63,
				  "atk":60,
				  "deff":55,
				  "spd":71,
                  "xp":122,
                  "lvlev":36,
                  "floor":[2,3],
                  "evolution":"pidgeot",
				  "satk":70},
	"pikachu":{"type":"eletric",
                "name":"Pikachu",
				  "dexn":16,
				  "hp":35,
				  "atk":50,
				  "deff":50,
				  "spd":90,
                  "xp":122,
                  "lvlev":30,
                  "floor":[2,3],
                  "evolution":"raichu",
				  "satk":70},
	"kadabra":{"Type":"psychic",
                  "name":"Kadabra",
				  "dexn":19,
				  "hp":40,
				  "atk":120,
				  "deff":70,
				  "spd":105,
                  "xp":140,
                  "lvlev":40,
                  "floor":[2,3],
                  "evolution":"alakazam",
				  "satk":40},
	"machoke":{"type":"fighting",
                  "name":"Machoke",
				  "dexn":22,
				  "hp":80,
				  "atk":100,
				  "deff":70,
				  "spd":45,
                  "xp":142,
                  "lvlev":40,
                  "floor":[2,3],
                  "evolution":"machamp",
				  "satk":40},
	"haunter":{"type":"ghost",
                  "name":"Haunter",
				  "dexn":25,
				  "hp":45,
				  "atk":115,
				  "deff":55,
				  "spd":95,
                  "xp":142,
                  "lvlev":40,
                  "floor":[2,3],
                  "evolution":"gengar",
				  "satk":70},
	"muk":{"type":"poison",
                  "name":"Muk",
				  "dexn":28,
				  "hp":80,
				  "atk":80,
				  "deff":50,
				  "spd":25,
                  "xp":175,
                  "lvlev":101,
                  "floor":[2,3],
                  "evolution":"abra",
				  "satk":40},
	"rhyhorn":{"type":"rock",
                  "name":"Rhyhorn",
				  "dexn":29,
				  "hp":80,
				  "atk":85,
				  "deff":95,
				  "spd":25,
                  "xp":69,
                  "lvlev":42,
                  "floor":[2,3],
                  "evolution":"rhydon",
				  "satk":50},
	"dragonair":{"type":"dragon",
                  "name":"Dragonair",
				  "dexn":32,
				  "hp":61,
				  "atk":84,
				  "deff":70,
				  "spd":70,
                  "xp":147,
                  "lvlev":55,
                  "floor":[2,3],
                  "evolution":"dragonite",
				  "satk":70},
	"krokorok":{"type":"ground",
                  "name":"Krokorok",
				  "dexn":37,
				  "hp":60,
				  "atk":82,
				  "deff":45,
				  "spd":74,
                  "xp":123,
                  "lvlev":40,
                  "floor":[2,3],
                  "evolution":"krookodile",
				  "satk":70},
	"persian":{"type":"normal",
                  "name":"Persian",
				  "dexn":40,
				  "hp":65,
				  "atk":70,
				  "deff":65,
				  "spd":115,
                  "xp":154,
                  "lvlev":101,
                  "floor":[2,3],
                  "evolution":"abra",
				  "satk":80}}




pokemondata3={"venusaur":{"type":"grass",
                    "name":"Venusaur",
                    "dexn":2,
					"hp":80,
					"atk":122,
					"deff":123,
					"spd":80,
                    "xp":281,
                    "lvlev":101,
                    "floor":[3,4],
                    "evolution":"abra",
					"satk":90},
	"charizard":{"type":"fire",
                    "name":"Charizard",
                    "dexn":5,
                    "hp":78,
					"atk":109,
					"deff":85,
					"spd":100,
                    "xp":240,
                    "lvlev":101,
                    "floor":[3,4],
                    "evolution":"abra",
					"satk":90},
	"blastoise":{"type":"water",
                  "name":"Blastoise",
                  "dexn":8,
                  "hp":79,
                  "atk":85,
				  "deff":105,
				  "spd":78,
                  "xp":239,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"butterfree":{"type":"bug",
                  "name":"Butterfree",
                  "dexn":11,
                  "hp":60,
				  "atk":90,
				  "deff":80,
				  "spd":70,
                  "xp":178,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"pidgeot":{"type":"flying",
                  "name":"Pidgeot",
                  "dexn":14,
                  "hp":83,
				  "atk":80,
				  "deff":75,
				  "spd":101,
                  "xp":216,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"raichu":{"type":"eletric",
                  "name":"Raichu",
                  "dexn":17,
                  "hp":60,
				  "atk":95,
				  "deff":85,
				  "spd":110,
                  "xp":218,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"alakazam":{"Type":"psychic",
                  "name":"Alakazam",
                  "dexn":20,
                  "hp":55,
				  "atk":135,
				  "deff":70,
				  "spd":120,
                  "xp":225,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"machamp":{"type":"fighting",
                  "name":"Machamp",
                  "dexn":23,
                  "hp":90,
				  "atk":130,
				  "deff":85,
				  "spd":55,
                  "xp":227,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"gengar":{"type":"ghost",
                  "name":"Gengar",
                  "dexn":26,
                  "hp":60,
				  "atk":130,
				  "deff":75,
				  "spd":110,
                  "xp":225,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":110},
	"muk":{"type":"poison",
                  "name":"Muk",
                  "dexn":28,
                  "hp":105,
				  "atk":105,
				  "deff":100,
				  "spd":50,
                  "xp":175,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"rhydon":{"type":"rock",
                  "name":"Rhydon",
                  "dexn":30,
                  "hp":105,
				  "atk":130,
				  "deff":120,
				  "spd":40,
                  "xp":170,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"dragonite":{"type":"dragon",
                  "name":"Dragonite",
                  "dexn":33,
                  "hp":91,
				  "atk":134,
				  "deff":100,
				  "spd":80,
                  "xp":270,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"avalugg":{"type":"ice",
                  "name":"Avalugg",
                  "dexn":35,
                  "hp":95,
				  "atk":117,
				  "deff":184,
				  "spd":28,
                  "xp":180,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"krookodile":{"type":"ground",
                  "name":"Krookodile",
                  "dexn":38,
                  "hp":95,
				  "atk":117,
				  "deff":80,
				  "spd":92,
                  "xp":234,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":90},
	"persian":{"type":"normal",
                  "name":"Persian",
                  "dexn":40,
                  "hp":65,
				  "atk":70,
				  "deff":65,
				  "spd":115,
                  "xp":154,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
				  "satk":80},
    "snorlax":{"type":"normal",
                  "name":"Snorlax",
                  "dexn":41,
                  "hp":160,
              	  "atk":110,
              	  "deff":65,
              	  "spd":30,
                  "xp":189,
                  "lvlev":101,
                  "floor":[3,4],
                  "evolution":"abra",
              	  "satk":90}}




class Pokemon:
    #classe para pokemons

    def __init__(self,pokemon,lvl):
        self.floor=pokemon["floor"] #andar no qual o pokemon pode aparecer
        self.evolution=pokemon["evolution"] #nome da evolução
        self.all=pokemon #todos os atributos basicos do pokemon
        self.ivhp=rd.randrange(1,32) #invisible value para a vida do pokemon (deixa todos os pokemons diferentes entre si)
        self.ivatk=rd.randrange(1,32) #invisible value para a ataque do pokemon (deixa todos os pokemons diferentes entre si)
        self.ivdeff=rd.randrange(1,32) #invisible value para a defesa do pokemon (deixa todos os pokemons diferentes entre si)
        self.ivspd=rd.randrange(1,32) #invisible value para a velocidade do pokemon (deixa todos os pokemons diferentes entre si)
        self.lvlevolution=pokemon["lvlev"] #level que cada pokemon evolui
        self.basexp=pokemon["xp"] #experiencia base que cada pokemon fornece qnd é fainted "morto"
        self.name=pokemon["name"] #nome do Inspermon
        self.dexn=pokemon["dexn"] #numero da INSPERDEX
        self.type=pokemon["type"] #tipo do pokemon
        self.lvl=lvl #lvl do pokemon
        self.hp=(((2*pokemon["hp"]+self.ivhp+(50/4))*lvl)/100)+lvl+10 #vida atual do pokemon
        self.atk=(((2*pokemon["atk"]+self.ivatk+(50/4))*lvl)/100)+5 #ataque atual do pokemon
        self.deff=(((2*pokemon["deff"]+self.ivdeff+(50/4))*lvl)/100)+5 #defesa atual do pokemon
        self.spd=(((2*pokemon["spd"]+self.ivspd+(50/4))*lvl)/100)+5 #velocidade atual do pokemon
        self.maxhp=(((2*pokemon["hp"]+self.ivhp+(50/4))*lvl)/100)+lvl+10 #vida máxima do pokemon
        self.satk=pokemon["satk"] #ataque especial do pokemon
        self.exp=(4*(lvl**3))/5 #experiencia do pokemon
        self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
                                                                                             (self.atk),int(self.deff),int(self.spd),int(self.exp))


    def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)


    def damage(self,enemy): #dano do ataque do pokemon com vantagens/fraquezas
            effectiveness=[0,0.5,1,2] #dano efetivo recebido pelo pokemon(de acordo com as vantagens/fraquezas)
            dmg=effectiveness[2]
            consolemessage=("It was effective")
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
            enemy.hp-=(self.attack(enemy))*dmg
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
                missing_exp=valor-self.exp
                delay_print("Your {} need {} more exp to the next Level...\n".format(self.name,str(int((valor-self.exp)))))
                break
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
            #self.evolving(self,evolution)



    def expgain(self,enemy):
        self.exp+=(enemy.basexp*enemy.lvl)/7
        self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
                                                                                             (self.atk),int(self.deff),int(self.spd),int(self.exp))
        return self.exp

    # def evolving(self,evolution):
    #     if self.lvl>=self.evolution:
    #         self.all=evolution #todos os atributos basicos do pokemon
    #         self.evolution=evolution["lvlev"] #level que cada pokemon evolui
    #         self.basexp=evolution["xp"] #experiencia base que cada pokemon fornece qnd é fainted "morto"
    #         self.name=evolution["name"] #nome do Inspermon
    #         self.dexn=evolution["dexn"] #numero da INSPERDEX
    #         self.type=evolution["type"] #tipo do pokemon
    #         self.hp=(((2*evolution["hp"]+self.ivhp+(50/4))*self.lvl)/100)+self.lvl+10 #vida atual do pokemon
    #         self.atk=(((2*evolution["atk"]+self.ivatk+(50/4))*self.lvl)/100)+5 #ataque atual do pokemon
    #         self.deff=(((2*evolution["deff"]+self.ivdeff+(50/4))*self.lvl)/100)+5 #defesa atual do pokemon
    #         self.spd=(((2*evolution["spd"]+self.ivspd+(50/4))*self.lvl)/100)+5 #velocidade atual do pokemon
    #         self.maxhp=(((2*evolution["hp"]+self.ivhp+(50/4))*self.lvl)/100)+self.lvl+10 #vida máxima do pokemon
    #         self.satk=evolution["satk"] #ataque especial do pokemon
    #         self.attributes="Type:{}\nLevel:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\nExperience:{}\n".format((self.type).capitalize(),self.lvl,int(self.maxhp),
    #                                                                                              int(self.atk),int(self.deff),int(self.spd),int(self.exp))
    #         return delay_print("What?....\nYour {} is evolving!!!!".format(self.all[]))





class Player():
    #classe para o usuário

    def __init__(self,name,pokemon):
        self.party=[pokemon]  #lista de todos os pokemons do player
        self.name="{}".format(name) #nome do jogador
        self.insperdex=["???"]*50 #numero da insperdex


    def dex(self,insperdex):
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

def restorelife(playerpokemon):
    delay_print("Press (1) if you want to use a Health Potion on your Inspermom: ")
    hp_potion=input()
    if hp_potion=="1":
        playerpokemon.hp=playerpokemon.maxhp
        return delay_print("Your {} is healed!!!".format((playerpokemon.name)))

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
    delay_print(Bulbasaur.attributes)
    playername.insperdex[Bulbasaur.dexn]="{}-{}:{}".format(Bulbasaur.dexn,Bulbasaur.name,Bulbasaur.type)
elif firstpokemon=="3":
    Squirtle=Pokemon(pokemondata["squirtle"],5)
    playername=Player(playername,Squirtle)
    delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
    delay_print(Squirtle.attributes)
    playername.insperdex[Squirtle.dexn]="{}-{}:{}".format(Squirtle.dexn,Squirtle.name,Squirtle.type)
elif firstpokemon=="2":
    Charmander=Pokemon(pokemondata["charmander"],5)
    playername=Player(playername,Charmander)
    delay_print("Congratulations!!!\nCharmander is your new Inspermon\n")
    delay_print(Charmander.attributes)
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
        delay_print(Bulbasaur.attributes)
        playername.insperdex[Bulbasaur.dexn]="{}-{}:{}".format(Bulbasaur.dexn,Bulbasaur.name,Bulbasaur.type)
    elif firstpokemon2=="3":
        Squirtle=Pokemon(pokemondata["squirtle"],5)
        playername=Player(playername,Squirtle)
        delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
        delay_print(Squirtle.attributes)
        playername.insperdex[Squirtle.dexn]="{}-{}:{}".format(Squirtle.dexn,Squirtle.name,Squirtle.type)

    elif firstpokemon2=="2":
        Charmander=Pokemon(pokemondata["charmander"],5)
        playername=Player(playername,Charmander)
        delay_print("Congratulations!!!\nSquirtle is your new Inspermon\n")
        delay_print(Charmander.attributes)
        playername.insperdex[Charmander.dexn]="{}-{}:{}".format(Charmander.dexn,Charmander.name,Charmander.type)
    else:
        Pikachu=Pokemon(pokemondata2["pikachu"],10)
        playername=Player(playername,Pikachu)
        delay_print("Okay...\nYou win\nCongratulations Pikachu is your new INSPERMON\n")
        delay_print(Pikachu.attributes)
        playername.insperdex[Pikachu.dexn]="{}-{}:{}".format(Pikachu.dexn,Pikachu.name,Pikachu.type)



delay_print("\nTo see information of your new INSPERMON, you can always use the INSPERDEX\n\
Your very own INSPERMON legend is about to unfold!\nA world of dreams and adventures with INSPERMON awaits! Let's go!\n")
while True:
    delay_print("You are now in the Insper's Labs\n\
What do you want to do first??\n\
----------------------------------------------\n\
Press (1) for walking around in the LAB\n\
----------------------------------------------\n\
Press (2) for saving the game\n\
----------------------------------------------\n\
Press (3) for looking at your INSPERDEX\n\
----------------------------------------------\n\
Press (4) for sleeping\n")
    action=input()
    if action=="4":
        break
    if action=="3":
        print("/////////////////////////////////////////////////////////////")
        playername.dex(playername.insperdex)
        print("/////////////////////////////////////////////////////////////")
    elif action=="1":
        delay_print("Where do you want to go?\n")
        delay_print("Press (0) for walking around in the Ground Floor\n\
----------------------------------------------\n\
Press (1) for walking around in the First Floor\n\
----------------------------------------------\n\
Press (2) for walking around in the Second Floor\n\
----------------------------------------------\n\
Press (3) for walking around in the Third Floor\n\
----------------------------------------------\n\
Press (4) for walking around in the Fourth Floor\n\
----------------------------------------------\n\
Press (5) to exit walking around\n")
        action=input()
        if action=="5":
            continue

        # def pokemongenerator():
        #     pokemon,attributes=rd.choice(list(pokemondata.items()))
        #     enemy=Pokemon(pokemondata[pokemon],lvlfloor0)



        elif action=="0":
            lvlfloor0=rd.randrange(1,6)
            pokemon,attributes=rd.choice(list(pokemondata.items()))
            enemy=Pokemon(pokemondata[pokemon],lvlfloor0)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(enemy.name,enemy.lvl))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            delay_print("What pokemon do you want to use to battle?\n")
            numeros=[]
            for i in range(len(playername.party)):
                delay_print("For {} press ({}).\n".format(playername.party[i].name,i))
                numeros.append("{}".format(i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command")
                choose=input()
            maxhp=(playername.party[int(choose)]).hp
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:
                choice=input("Are you going to Attack (1) or Run (2) or Check Status on INSPERDEX(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    restorelife(playername.party[int(choose)])
                    break
                if choice=="3":
                    print("Your {}\n{}\nWild {}\n{}\n".format((playername.party[int(choose)]).name,(playername.party[int(choose)]).attributes,enemy.name,enemy.attributes))
                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("-------------------------------------------------------------------------\n\
|Your {}'s Life:{} |                      |Wild {} Life:{}|\n\
-------------------------------------------------------------------------\n".format((playername.party[int(choose)]).name,
                    int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    (playername.party[int(choose)]).damage(enemy)
                    if enemy.hp<1:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<1:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<1:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<1:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break

        elif action=="1":
            lvlfloor1=rd.randrange(5,20)
            pokemon,attributes=rd.choice(list(pokemondata.items()))
            enemy=Pokemon(pokemondata[pokemon],lvlfloor1)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(enemy.name,lvlfloor1))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            delay_print("What pokemon do you want to use to battle?\n")
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command")
                choose=input()
            maxhp=(playername.party[int(choose)]).hp
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:

                choice=input("Are you going to Attack (1) or Run (2) or Check Status on INSPERDEX(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    restorelife(playername.party[int(choose)])
                    break
                if choice=="3":
                    print("Your {}\n{}\nWild {}\n{}\n".format((playername.party[int(choose)]).name,(playername.party[int(choose)]).attributes,enemy.name,enemy.attributes))
                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break


        elif action=="2":
            lvlfloor2=rd.randrange(20,31)
            pokemon,attributes=rd.choice(list(pokemondata2.items()))
            enemy=Pokemon(pokemondata2[pokemon],lvlfloor2)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(enemy.name,lvlfloor2))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            delay_print("What pokemon do you want to use to battle?\n")
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command")
                choose=input()
            maxhp=(playername.party[int(choose)]).hp
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:

                choice=input("Are you going to Attack (1) or Run (2) or Check Status on INSPERDEX(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    restorelife(playername.party[int(choose)])
                    break
                if choice=="3":
                    print("Your {}\n{}\nWild {}\n{}\n".format((playername.party[int(choose)]).name,(playername.party[int(choose)]).attributes,enemy.name,enemy.attributes))
                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break



        elif action=="3":
            lvlfloor3=rd.randrange(30,41)
            pokemon,attributes=rd.choice(list(pokemondata2.items()))
            enemy=Pokemon(pokemondata2[pokemon],lvlfloor3)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(enemy.name,lvlfloor3))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            delay_print("What pokemon do you want to use to battle?\n")
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command")
                choose=input()
            maxhp=(playername.party[int(choose)]).hp
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:

                choice=input("Are you going to Attack (1) or Run (2) or Check Status on INSPERDEX(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    restorelife(playername.party[int(choose)])
                    break
                if choice=="3":
                    print("Your {}\n{}\nWild {}\n{}\n".format((playername.party[int(choose)]).name,(playername.party[int(choose)]).attributes,enemy.name,enemy.attributes))
                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break




        elif action=="4":
            lvlfloor4=rd.randrange(40,51)
            pokemon,attributes=rd.choice(list(pokemondata3.items()))
            enemy=Pokemon(pokemondata3[pokemon],lvlfloor4)
            message="A wild {} Level:{} appears...\n"
            delay_print(message.format(enemy.name,lvlfloor4))
            playername.insperdex[enemy.dexn]="{}-{}:{}".format(enemy.dexn,enemy.name,enemy.type)
            delay_print("What pokemon do you want to use to battle?\n")
            for i in range(len(playername.party)):
                delay_print("{}({})".format(playername.party[i].name,i))
            choose=input()
            while choose not in numeros:
                print("Type a valid command")
                choose=input()
            maxhp=(playername.party[int(choose)]).hp
            while (playername.party[int(choose)]).hp>0 and enemy.hp>0:

                choice=input("Are you going to Attack (1) or Run (2) or Check Status on INSPERDEX(3):")
                if choice=="2":
                    delay_print("You ran out of the battle...")
                    restorelife(playername.party[int(choose)])
                    break
                if choice=="3":
                    print("Your {}\n{}\nWild {}\n{}\n".format((playername.party[int(choose)]).name,(playername.party[int(choose)]).attributes,enemy.name,enemy.attributes))
                elif (playername.party[int(choose)]).spd > enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    if enemy.hp<=0:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                elif (playername.party[int(choose)]).spd < enemy.spd:
                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    delay_print("Wild {} Attacked...\n".format(enemy.name))
                    (enemy.damage(playername.party[int(choose)]))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if (playername.party[int(choose)]).hp<=0:
                        delay_print("Your pokemon fainted...\nYou loose!!!\n")
                        restorelife(playername.party[int(choose)])
                        break
                    delay_print("Your {} Attacked...\n".format((playername.party[int(choose)]).name))
                    ((playername.party[int(choose)]).damage(enemy))

                    delay_print("Your {}'s life:{}   Wild {}:{}\n".format((playername.party[int(choose)]).name,
                                                                          int((playername.party[int(choose)]).hp),enemy.name,int(enemy.hp)))
                    if enemy.hp<1:
                        delay_print("The enemy {} fainted...\nYou won!!!\n".format(enemy.name))
                        (playername.party[int(choose)]).expgain(enemy)
                        (playername.party[int(choose)]).lvlup(exp_list)
                        restorelife(playername.party[int(choose)])
                        break
