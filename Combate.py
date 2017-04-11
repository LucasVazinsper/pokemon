def attack(self,enemy): #dano do ataque do pokemon
        return ((((2*self.lvl/5)+2)*self.satk*(self.atk/enemy.deff)/50)+2)*(rd.randrange(85,101)/100)

def deffense(self,enemy): #dano recebido pelo pokemon
        effectiveness=[0,0.5,1,2] #dano efetivo recebido pelo pokemon(de acordo com as vantagens/fraquezas)
        dmg=effectiveness[2]
        if self.type=="normal"and enemy.type=="rock": #rock é resistente ao normal
            print("It's not very effective...")
            dmg=effectiveness[1]
        if self.type=="normal" and enemy.type=="ghost": #ghost é imune ao normal
            print("It's not effective...")
            dmg=effectiveness[0]
        if self.type=="fight" and enemy.type=="normal": #normal é fraco contra fight  
            print("It's super effective")
            dmg=effectiveness[3]
        return enemy.hp - self.attack(enemy)*dmg ##preciso melhorar a implementação, mas essa é a idea
   