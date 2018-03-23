#! /usr/bin/python3
import itertools

def anatheseis(num_pollaplasiasmos):
    x = num_pollaplasiasmos[0]
    y = num_pollaplasiasmos[1]
    return x,y

def upologismos_pollaplasiasmwn(x,y,z):
    return x*y*z


def pinakas_pollaplasiasmwn():
    x = [1,1,2,2,3]
    lista = []
    y  = list(itertools.permutations(x,5))
    for i in y:
        if i in lista:
            continue
        lista.append(i)
    return lista

def diabase_diastaseis():
    for i in pinakes:
        while 1:
            print("Δώστε διαστάσεις με κενό η το συμβολο '*'για τον πίνακα",i)
            x = input()
            if "*" in x or " " in x:
                break
            else:
                print("Πρέπει να βάλετε * η κενό")
                continue
        temp = { i : x}
        diastasis.update(temp)
    return diastasis

geniko_synolo = []
teleuteos_pinakas = []
neos_pinakas = []
neos_pinakas1 = []
antistoixies = {"0" : (0,1),"1" : (2,3),"2" : (4,5), "3" : (6,7) , "4" : (8,9)}
oloi_pollaplasiasoi = pinakas_pollaplasiasmwn()
pinakes = ["A","B","C","D","E"]
temp = {}
diastasis = {}
lista_me_megethoi = []
diastasis = diabase_diastaseis()
for pinakas in pinakes:
    row = True
    y = "0"
    x = y
    for i in diastasis[pinakas]:
        if i == " " or i =="*":
            row = False
            continue
        if row == False:
            y += i
        else:
            x += i
    #Στα μονα οι στηλες, ζυγά και 0 γραμμες
    lista_me_megethoi.append(int(x))
    lista_me_megethoi.append(int(y))
for pollaplasiasmos in oloi_pollaplasiasoi:
    prwtos = []#pollaplasiasmos
    deuteros = []#pollaplasiasmos
    thesi = 0
    for z in pollaplasiasmos:
        if z == 1:
            prwtos.append(thesi)
        if z == 2:
            deuteros.append(thesi)
        else:
            tritos = thesi
        thesi += 1

    synolo = 0
    x, y = anatheseis(prwtos)
    z, w = anatheseis(deuteros)
    megethoi  = antistoixies[str(x)]
    megethoi2  = antistoixies[str(y)]

    if lista_me_megethoi[megethoi[1]] != lista_me_megethoi[megethoi2[0]]:
        print("Οι πολλαπλασιασμοι δεν γίνονται για τον συνδιασμό",pollaplasiasmos,"Οπου ίδιος αριθμός πολλαπλασιάζετε αντιστοιχος πίνακας")
        continue
    else:
        neos_pinakas=[lista_me_megethoi[megethoi[0]],lista_me_megethoi[megethoi2[1]]]
        synolo = lista_me_megethoi[megethoi[0]] * lista_me_megethoi[megethoi2[1]] * lista_me_megethoi[megethoi[1]] + synolo

    megethoi  = antistoixies[str(z)]
    megethoi2  = antistoixies[str(w)]

    if lista_me_megethoi[megethoi[1]] != lista_me_megethoi[megethoi2[0]]:
        print("Οι πολλαπλασιασμοι δεν γίνονται για τον συνδιασμό",pollaplasiasmos,"Οπου ίδιος αριθμός πολλαπλασιάζετε αντιστοιχος πίνακας")
        continue
    else:
        neos_pinakas1=[lista_me_megethoi[megethoi[0]],lista_me_megethoi[megethoi2[1]]]
        synolo = lista_me_megethoi[megethoi[0]] * lista_me_megethoi[megethoi2[1]] * lista_me_megethoi[megethoi[1]] + synolo

    if neos_pinakas[1] != neos_pinakas1[0]:
        print("Οι πολλαπλασιασμοι των πινάκων",neos_pinakas,neos_pinakas1," δεν γίνονται για τον συνδιασμό",pollaplasiasmos,"Οπου ίδιος αριθμός πολλαπλασιάζετε αντιστοιχος πίνακας")
        continue
    else:
        teleuteos_pinakas = [neos_pinakas[0],neos_pinakas1[1]]
        synolo = neos_pinakas[0] * neos_pinakas[1] * neos_pinakas1[1] + synolo

    last = antistoixies[str(tritos)]
    if lista_me_megethoi[last[1]] != teleuteos_pinakas[0]: #out of index?
        print("Οι πολλαπλασιασμοι των πινάκων",megethoi,teleuteos_pinakas," δεν γίνονται για τον συνδιασμό",pollaplasiasmos,"Οπου ίδιος αριθμός πολλαπλασιάζετε αντιστοιχος πίνακας")
    else:
        synolo = lista_me_megethoi[last[0]] * lista_me_megethoi[last[1]] * teleuteos_pinakas[1] + synolo
    geniko_synolo.append(synolo)
print("Οι λιγότεροι πολλαπλασιασμοι που μπορουν να γινουν για τις μητρες ειναι",min(geniko_synolo))
