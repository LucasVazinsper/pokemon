#Status iguias,se eles atacarem juntos a batalha nao fosse em turnos,eles morreriam ao msm tempo
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.01)
minha_vida=20
meu_ataque=5
minha_defesa=0
minha_speed=10
inimigo_vida=20
inimigo_ataque=5
inimigo_defesa=0
inimigo_speed=1
ok=True
while ok:
    a=int(input("passear (0) ou dormir (1): "))
    if a==1:
        break
    if a==0:
        while minha_vida>0 and inimigo_vida>0:
            acao=int(input("atacar:0 correr:1    "))
            if acao==1:
                delay_print("Voce correu.")
                break
            if acao==0 and minha_speed>inimigo_speed:
                inimigo_vida=inimigo_vida+inimigo_defesa-meu_ataque
                delay_print("sua vida:{} vida do inimigo:{}\n".format(minha_vida,inimigo_vida))
                if minha_vida>0 and inimigo_vida>0:
                    minha_vida=minha_vida+minha_defesa-inimigo_ataque
                    delay_print("sua vida:{} vida do inimigo:{}\n".format(minha_vida,inimigo_vida))
                if inimigo_vida<=0:
                    delay_print("Voce venceu!!\n")
                elif minha_vida<=0:
                    delay_print("Vc perdeu...\n")
            if acao==0 and minha_speed<inimigo_speed:
                minha_vida=minha_vida+minha_defesa-inimigo_ataque
                delay_print("sua vida:{} vida do inimigo:{}\n".format(minha_vida,inimigo_vida))
                if minha_vida>0 and inimigo_vida>0:
                    inimigo_vida=inimigo_vida+inimigo_defesa-meu_ataque
                    delay_print("sua vida:{} vida do inimigo:{}\n".format(minha_vida,inimigo_vida))
                if inimigo_vida<=0:
                    print("Voce venceu!!\n")
                elif minha_vida<=0:
                    delay_print("Vc perdeu...\n")
            elif acao!=0 and acao!=1:
                print("Digite um comando válido ")  #caso o usuario insira um numero errado
    else:
        print("Digite um comando válido 5")
