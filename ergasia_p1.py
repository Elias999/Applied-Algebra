#! /usr/bin/python3

def Sort_out(the_list,the_other_list):
    for y in range(len(the_list)-1,0,-1):
        for i in range(y):
            if the_list[i]>the_list[i+1]:
                temp = the_list[i]
                temp1 = the_other_list[i]
                the_list[i] = the_list[i+1]
                the_other_list[i] = the_other_list[i+1]
                the_list[i+1] = temp
                the_other_list[i+1] = temp1

def make_me_alist(): # φτιάχνει λίστα απο 1 ως το μηκος της μεταθεσης
    na_lista = []
    for i in range(mikos):
        na_lista.append(i+1)
    return na_lista

def parabaseis(the_meta_list):
    parabasis = 0
    for thesi in range(mikos-1):
        checks = thesi+1
        print (checks)
        while checks <=mikos-1:
            if the_meta_list[thesi] > the_meta_list[checks]:
                parabasis +=1
            checks += 1
    return parabasis

metathesis = input("Δώστε την μετάθεση μ, πού διαχωρίζονται με κενό χαρακτήρα:\n")
mikos = 0
list_metathesis = []
antistrofi = []

for i in metathesis:
    if i != " ":
        mikos += 1
        list_metathesis.append(int(i))

me_tin_seira = make_me_alist()
original_metathesis = list(list_metathesis)
kyklos = []
thesi = 0
thesi = original_metathesis[thesi]
i=0
mikos_epa = 1
while True:
        if thesi in kyklos:
            kyklos.append("*")
            try:
                thesi = original_metathesis[thesi-1]
                thesi +=1
            except:
                break
        else:
            kyklos.append(thesi)
            thesi = original_metathesis[thesi-1]
            mikos_epa +=1
        if mikos_epa == mikos + 1:
            break

antistrofi = make_me_alist()



Sort_out(list_metathesis,antistrofi)
parabasis = parabaseis(original_metathesis)
print("Μήκος μετάθεση" , mikos)#erwtima i
print("Αρχική", original_metathesis,"\n","H αντίστροφη μετάθεση ", antistrofi)#erwtima ii
print("Εκφρασμένη ως γινόμενο κύκλων",kyklos)#erwtima iii
print("Οι παραβάσεις ειναι", parabasis)#erwtima V
if parabasis % 2 == 0:#ερώτημα vi
    print("Η μετάθεση ειναι άρτια")
else:
    print ("Η μετάθεση είναι περιττή")
