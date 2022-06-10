from operator import truediv
from threading import local
import time

ag=10
fca=6
forcafaca=1.5
lobo=True
faca=0
Vida=True

while Vida==True:
    print("""Você para na cidade de Stanfordshire-Upon-Trent para conseguir mercadoria.
Naturalmente, o ponto de chegada das carroças é conturbado e cheio de pessoas.
Sua sacola de dinheiro é roubada por um trombadinha que sai correndo. Você não vê onde ele vai.
Sem dinheiro e em uma cidade desconhecida, você precisa encontrar alguma maneira de sobreviver.""")
    time.sleep(2)
    nome=input(str("""\"Ei forasteiro!\", você ouve uma voz vindo de uma barraca. \"Qual é seu nome? Vou ver se posso te ajudar...\"
    """))

    print(f"""\"{nome} é? Sendo assim, direi o meu. Washington, um famoso burguês da região. Já ouviu falar
    de mim?\"
1- Sim
2- Não""")
    t1=int(input("Sua resposta é: "))

    if t1==1:
        print("""\"Hahaha! Sábio da sua parte se informar bem antes de viajar. Você não parece tão
perdido como eu imaginava\"""")

    elif t1==2:
        print("""\"Muito bom, então me apresentarei. Washington, duque de Berryhill, comendador 3 vezes
como Cavaleiro Real da Vanguarda. Mas isso já faz tempo. Não luto há eras e meu braço se
tornou frágil. Hoje acumulo minhas riquezas e vivo dentre a nobreza. Meu ducado é certamente
um dos mais prósperos da região.\"""")

    else:
        print("""Hm... de qualquer forma...""")

    t1=None

    time.sleep(2)
    print("""\"Eu vi o infortúnio que você presenciou, sinto muito por isso. Na verdade, quero ajudar você
a se recompor financeiramente pois gostaria de contratar seus serviços. Preciso de uma entrega feita em
um certo endereço fora da cidade no meu condado, mas isto ficará para outro dia\"""")
    time.sleep(4)
    print("""\"Por hora, quero te dar isso\"""")
    time.sleep(2)
    g=50
    sacoOuro=1
    mapaCidade=1
    temMapaCidade=1
    print(f"// VOCÊ RECEBEU:{sacoOuro}x Saco de moeda")
    print(f"// VOCÊ REBECEU:{g}x Ouro")
    print(f"// VOCÊ RECEBEU:{mapaCidade}x Mapa da Cidade")
    time.sleep(2)
    print("""
    \"Isso vai ajudar você a manter seu prato de comida cheio por hoje e um teto sobre sua cabeça. Mas
vejo que esse braço seu já viu combate. Lembra-me o meu na minha época de ouro. Por que você não vai
procurar uma boa espada? Inclusive, você deveria ir no quartel relatar que foi roubado. Quem sabe eles
não possam te ajudar\"""")
    time.sleep(4)
    print("""\"Isso é tudo, amigo! Bem vindo a Stanfordshire-Upon-Trent! Tome cuidado lá fora e boa sorte encontrando
aquilo que é seu!\"
    """)
    print("""(Washington sai)
       """)
    time.sleep(4)
    print(t1)
    acao1=False
    pos=1311

    if pos==1311:
            while acao1==False:
                print("""Você se encontra no ponto de parada das carroças. Você deveria ir ao quartel.
1- Andar para NORTE
2- Andar para SUL
3- Andar para LESTE
4- Andar para OESTE
5- Usar ITEM""")
                t1=int(input("Sua ação é: "))

                escolha=False
                if t1==5:
                    while escolha==False:
                        print("INVENTÁRIO")
                        print(f"1- {sacoOuro} Ouro")
                        print(f"2- {mapaCidade} Mapa da cidade"*int(temMapaCidade))
                        time.sleep(4)
                        t2=int(input("Escolha um item para usar: "))
                        if t2==1:
                            print("Este item não parece ser útil nessa ocasião...")
                            time.sleep(4)
                            escolha=True
                            faca=1
                        if t2==2:
                            print("Você usa o mapa da cidade:")
                            print("--= MAPA DE STANFORDSHIRE-UPON-TRENT =--")
                            print("[ ] [ ] [ ] [ ]――――☷ | Estábulo do comércio:")
                            print("     ♣♣♣    [ ]|[ ]☷ | Um estábulo simples onde")
                            print("  ♣ [ ] [ ] [ ] [ ]☷ | comerciantes chegam todos os")
                            print("♣♣  [ ] [ ] [ ]――――☷ | dias com suas mercadorias para")
                            print("♣♣♣♣♣♣♣♣[ ] [ ] 〜 ☷ | vender. Por estar na periferia,")
                            print("♣♣♣♣[ ] [X]  〜〜〜〜| é um local considerado perigoso")
                            time.sleep(6)
                            escolha=True
                        else:
                            escolha=False
                if t1==4:
                    pos=pos-100
                    acao1=True
                    #resto das possibilidades

    if pos==1211:
        acao1=False
        t1=None
        while acao1==False:
                print("""Você anda para oeste pelo caminho que veio à cavalo e se depara com a floresta
que atravessou para chegar na cidade. Você não tem comida preservada o suficiente para fazer a viagem
de volta. Próximo ao início da floresta, você encontra pequenas propriedades rurais com placas
denominando os endereços com os nomes das pessoas que moram nelas.
1- Andar para NORTE
2- Andar para SUL
3- Andar para LESTE
4- Andar para OESTE
5- Usar ITEM
―――――――――――――――――――――
6- Bater na porta da casa: Joanne and Phillip Kinsley
7- Bater na porta da casa: David Trout
8- Bater na porta da casa: Frederik Steiner""")
                t1=int(input("Sua ação é: "))

                escolha=False
                if t1==6:
                    escolha2=False
                    vidaLobo=30
                    vidaPersonagem=25
                    while lobo==True:
                        t2=None
                        print("Você bate na porta.")
                        print("Ninguém responde. De repente, um lobo aparece na sua frente.")
                        print("Ele rosna. Não há como sair dessa sem lutar!")
                        print("""1- ATACAR""")
                        t2=int(input("Sua ação é: "))

                        while vidaLobo>0 and vidaPersonagem>0:
                            if t2==1:
                                print(f"A - {faca}x Faca"*int(faca))
                                print(f"B - Soco")
                                t3=str(input("Use um ataque: "))
                                if t3=="A":
                                    print("Você ataca o lobo com a Faca")
                                    vidaLobo=vidaLobo-(fca*forcafaca)
                                    print(f"O lobo tem {vidaLobo} de vida")
                                    print("O lobo te ataca com Garra")
                                    vidaPersonagem=vidaPersonagem-10
                                    print(f"Você tem {vidaPersonagem} de vida")
                                if t3=="B":
                                    print("Você ataca o lobo com o Soco")
                                    vidaLobo=vidaLobo-fca
                                    print(f"O lobo tem {vidaLobo} de vida")
                                    print("O lobo te ataca com Garra")
                                    vidaPersonagem=vidaPersonagem-10
                                    print(f"Você tem {vidaPersonagem} de vida")
                        if vidaLobo<0:
                            print("O lobo morre.")
                        if vidaPersonagem<0:
                            print(f"{nome} morre.")
                            time.sleep(4)
                            Vida=False
                        lobo=False               

                            
                            

                    



                
                
            





#Dungeon1 = False
#while Dungeon1 = False
