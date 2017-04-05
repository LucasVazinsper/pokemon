import math
def dano(IVatk,baseatk,mov,levelA,IVhp,IVdef,basedef,basehp,levelB):
    ev=(100) #valor de 1 ate 254
    hpb=(((2*basehp+IVhp+(ev/4))*levelB)/100)+levelB+10
    atka=(((2*baseatk+IVatk+(ev/4))*levelA)/100)+5
    defb=(((2*basedef+IVdef+(ev/4))*levelB)/100)+5
    dano=(((((2*levelA)/5)+2)*mov)*(atka/defb)/50)+2    #nao esta certa...
    return hpb
