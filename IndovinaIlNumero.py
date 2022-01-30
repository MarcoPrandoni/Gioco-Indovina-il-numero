import random
dec="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
while(1==1):
    print('''INDOVINA IL NUMERO
In questo gioco dovrai indovinare un numero casuale tra 1 e 20 in 5 tentativi.
Il gioco ti dirà se il numero inserito è maggiore o minore di quello da indovinare\n''')

    numero=random.randint(1,20)
    while(numero<1 or numero>20):
        numero=random.randint(1,20)
    i=5
    while(i>0):
        print(f"ti rimangono {i} tentativi\n")
        scelta=int(input("Inserire il numero scelto\n"))
        i-=1
        if(scelta==numero):
            print(f"COMPLIMENTI HAI VINTO!!\n{dec}")
            i=10
            break
        else:
            print("Il numero non è corretto, fai un'altro tentativo")
            if(scelta<numero):
                print("il numero scelto è minore del numero da indovinare")
            else:
                print("il numero scelto è maggiore del numero da indovinare")
    if(i==0):
         print(f"Mi dispiace ma hai finito i tenativi, se vuoi puoi riprovare con un numero diverso\n{dec}\nIl numero era {numero}")
