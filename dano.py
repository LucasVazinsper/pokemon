def dano(atk,lvl,move,deff):
    ran=random.randrange(85,100)
    x=1 #modificador(super efetivo)
    damage=((((2*lvl/5)+2)*move*(atk/deff)/50)+2)*(ran/100)*(x)
    return damage







#teste
