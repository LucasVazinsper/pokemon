import random





Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]


class Pokemon:
    #classe de atributos para pokemons

    def __init__(self,vtipo,vhp,vatk,vdeff,vspd,vmov,vnome):
        self.hp=vhp  #vida do pokemon
        self.deff=vdeff  # defesa do pokemon
        self.atk=vatk  # ataque do pokemon
        self.spd=vspd  # velocidade do pokemon
        self.tipo=vtipo  #tipo do pokemon
        self.mov=vmov #Dano da habilidade (ex:Bubbles)
        self.nome=vnome
        self.dados=[vtipo,vhp,vatk,vdeff,vspd,vmov,vnome]


bulbasaur=Pokemon("grama",45,49,49,40,40,"Bulbasaur")
charmander=Pokemon("fogo",49,52,43,65,40,"Charmander")
squirtle=Pokemon("água",44,50,65,43,40,"Squirtle")


pkmsfracos=[bulbasaur.dados,charmander.dados,squirtle.dados]

def stats(z):
    x=random.randrange(0,len(pkmsfracos)) #garante o pokemon que tera os dados gerados
    ivatk=random.randrange(1,31)    #
    ivdeff=random.randrange(1,31)     #
    ivspd=random.randrange(1,31)        #  Garante que msm sendo o msm pokemon ele sera diferente
    ivhp=random.randrange(1,31)      #
    lvlf=random.randrange(1,10)  #
    vida=(((2*z[x][1]+ivhp+(50/4))*lvlf)/100)+lvlf+10
    print(z[x][6])   #testa qual pokemon esta sendo gerado
    #atk=
    #deff=    #faz ai juan
    #spd=
    return vida    #falta ataque,defesa e speed


print("vida do pokemon gerado:{}".format(stats(pkmsfracos))) #


pok={"bulbasaur":{"type":"grass",
					"hp":45,
					"atk":49,
					"deff":49,
					"spd"40,
					"vmov":40,},
	"charmander":{"type":"grass",
					"hp":45,
					"atk":49,
					"deff":49,
					"spd"40,
					"vmov":40,}