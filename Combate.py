def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)

def deffense(self,enemy): #dano recebido pelo pokemon
        effectiveness=[0,0.5,1,2] #dano efetivo recebido pelo pokemon(de acordo com as vantagens/fraquezas)
        dmg=effectiveness[2]
        if self.type=="normal"and enemy.type=="rock": #rock é resistente ao normal
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="normal" and enemy.type=="ghost": #ghost é imune ao normal
            print("But it failed!")
            dmg=effectiveness[0]

        if self.type=="fire" and enemy.type=="fire":
            dmg=effectiveness[1]

        if self.type=="fire"and enemy.type=="water":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fire"and enemy.type=="rock":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fire"and enemy.type=="dragon":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fire"and enemy.type=="grass":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="fire"and enemy.type=="ice":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="fire"and enemy.type=="bug":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="water"and enemy.type=="fire":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="water"and enemy.type=="ground":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="water"and enemy.type=="rock":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="water"and enemy.type=="water":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="water"and enemy.type=="grass":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="water"and enemy.type=="dragon":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="eletric"and enemy.type=="eletric":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="eletric"and enemy.type=="grass":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="eletric"and enemy.type=="dragon":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="eletric"and enemy.type=="water":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="eletric"and enemy.type=="flying":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="eletric"and enemy.type=="ground":
            print("But it failed!")
            dmg=effectiveness[0]

        if self.type=="grass"and enemy.type=="fire":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grass"and enemy.type=="grass":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grass"and enemy.type=="poison":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grass"and enemy.type=="flying":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grass"and enemy.type=="bug":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grass"and enemy.type=="dragon":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grass"and enemy.type=="water":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="grass"and enemy.type=="ground":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="grass"and enemy.type=="rock":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ice"and enemy.type=="fire":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="ice"and enemy.type=="water":
            print("It's not very effective...")
            dmg=effectiveness[1]


        if self.type=="ice"and enemy.type=="ice":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="ice"and enemy.type=="grass":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ice"and enemy.type=="flying":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ice"and enemy.type=="ground":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ice"and enemy.type=="dragon":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="fighting"and enemy.type=="poison":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fighting"and enemy.type=="flying":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fighting"and enemy.type=="psychic":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fighting"and enemy.type=="bug":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fighting"and enemy.type=="normal":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="fighting"and enemy.type=="ice":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="fighting"and enemy.type=="rock":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="fighting"and enemy.type=="ghost":
            print("But it failed!")
            dmg=effectiveness[0]

        if self.type=="poison"and enemy.type=="poison":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="poison"and enemy.type=="ground":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="poison"and enemy.type=="rock":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="poison"and enemy.type=="ghost":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="poison"and enemy.type=="grass":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="grond"and enemy.type=="grass":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grond"and enemy.type=="bug":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="grond"and enemy.type=="fire":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ground"and enemy.type=="eletric":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ground"and enemy.type=="poison":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ground"and enemy.type=="rock":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ground"and enemy.type=="flying":
            print("But it failed!")
            dmg=effectiveness[0]

        if self.type=="flying"and enemy.type=="eletric":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="flying"and enemy.type=="rock":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="flying"and enemy.type=="grass":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="flying"and enemy.type=="fighting":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="flying"and enemy.type=="bug":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="psychic"and enemy.type=="psychic":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="psychic"and enemy.type=="fighting":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="psychic"and enemy.type=="poison":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="bug"and enemy.type=="fire":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="bug"and enemy.type=="fighting":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="bug"and enemy.type=="poison":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="bug"and enemy.type=="flying":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="bug"and enemy.type=="ghost":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="bug"and enemy.type=="grass":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="bug"and enemy.type=="psychic":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="rock"and enemy.type=="fighting":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="rock"and enemy.type=="ground":
            print("It's not very effective...")
            dmg=effectiveness[1]

        if self.type=="rock"and enemy.type=="fire":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="rock"and enemy.type=="ice":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="rock"and enemy.type=="flying":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="rock"and enemy.type=="bug":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ghost"and enemy.type=="psychic":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ghost"and enemy.type=="ghost":
            print("It's super effective!")
            dmg=effectiveness[3]

        if self.type=="ghost"and enemy.type=="normal":
            print("But it failed!")
            dmg=effectiveness[0]

        if self.type=="dragon"and enemy.type=="dragon":
            print("It's super effective!")
            dmg=effectiveness[3]

        return enemy.hp - self.attack(enemy)*dmg ##preciso melhorar a implementação, mas essa é a idea
                                                     #agr ja era fion.
