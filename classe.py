import math
import random as rd

Tipos=["Normal","Fire","Water","Eletric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Ghost","Rock","Dragon"]


class Pokemon:
	#classe de atributos para pokemons

	def __init__(self,vtipo,vhp,vatk,vdeff,vspd,vivatk,vivdeff,vivspd,vev,vmov,vlvl):
		self.hp=vhp  #vida do pokemon
		self.deff=vdeff  # defesa do pokemon
		self.atk=vatk  # ataque do pokemon
		self.spd=vspd  # velocidade do pokemon
		self.tipo=vtipo  #tipo do pokemon
        self.ivatk= #IV de ataque
        self.ivspd=vivspd #IV de velocidade
        self.ivdeff=vivdeff #IV de Defesa
        self.ev=vev #Evaluated Value
        self.mov=vmov #Dano da habilidade (ex:Bubbles)
        self.lvl=vlvl #Level do pokemon
		self.atributos="\nType:{}\nHp:{}\nAttack:{}\nDeffense:{}\nSpeed:{}\n".format(self.tipo,self.hp,self.atk,self.deff,self.spd)


def hp(bhp,ivhp,lvl,ev):
    vida=(((2*bhp+ivhp+(ev/4))*lvl)/100)+lvl+10
    return vida

def atk(batk,ivatk,lvl,ev):
	ataque=(((2*batk+ivatk+(ev/4))*lvl)/100)+5
	return ataque

def deff(bdeff,ivdeff,lvl,ev):
    defesa=(((2*bdeff+ivdeff+(ev/4))*lvl)/100)+5
    return defesa

def spd(bspd,ivspd,lvl,ev):
    velocidade=(((2*bspd+ivspd+(ev/4))*lvl)/100)+5
    return velocidade 
