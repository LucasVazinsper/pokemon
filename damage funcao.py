def dano(IVatk,baseatk,mov,levelA,IVhp,IVdef,basedef,basehp,levelB):
    ev=22850
    evraiz=(math.sqrt(ev))/4
    ran=90
    hpb=(((((basehp+IVhp)*2)+(evraiz))*levelB)/100)+levelB+10
    atka=(((((baseatk+IVatk)*2)+(evraiz))*levelA)/100)+5
    defb=(((((basedef+IVdef)*2)+(evraiz))*levelB)/100)+5
    dano=(((((2*levelA)/5)+2)*mov)*(atka/defb)/50)+2    #nao esta certa...
    return dano

hp=dano(30,52,110,5,30,30,65,44,5)
print (int(hp))
    
