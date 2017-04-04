Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]

class Pokemon:
	#classe de atributos para pokemons

	def __init__(self,vtipo,vhp,vatk,vdeff,vspd):
		self.hp=vhp  #vida do pokemon
		self.deff=vdeff  # defesa do pokemon
		self.atk=vatk  # ataque do pokemon
		self.spd=vspd  # velocidade do pokemon
		self.tipo=vtipo  #tipo do pokemon
		self.atributos="\nType:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\n".format(self.tipo,self.hp,self.atk,self.deff,self.spd)

Charmander = Pokemon(Tipos[1],39,52,43,65)
Squirtle = Pokemon(Tipos[2],44,48,65,43)
print("Charmander {}\nSquirtle{}\n".format(Charmander.atributos,Squirtle.atributos))