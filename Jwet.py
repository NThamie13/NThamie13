while True:
    import random
    import time

#Mesaj pou itilisate a 
    nom = input ("Bonjour, entre non'w svp : ")
    print(f"Byenvini {nom} , Nan jwet la ! ")

#Kreyasyon varyab 
    laje_entefas = 15
    wote_entefas = 20
    karakte_lage = " -*"
    karakte_ote = " |*"
    obstak = "-O-"
    abs_obst = 2

#afichaj entefas la ak objet an
    for i in range(laje_entefas):
        if i == 0 or i == laje_entefas - 1:
         print(karakte_lage * laje_entefas)
        elif i == 1 :
            print(karakte_ote + " " * 4 + obstak + "        " * 4 + karakte_ote)
        else:
            print(karakte_ote + "  " * (wote_entefas) + karakte_ote)
# Mod deplasman obstak lan 
    deplase= input("Pou'w komanse jwe, peze J :"  )
    if deplase !="J" and deplase !="j" :
     print("Ere, ou sipoze antre let J.")
    else:
        while abs_obst < wote_entefas :
            time.sleep(0.33)
            abs_obst += 1

#efase ansyen entefas la 
        print("\033c", end="")

#pozisyon obstak la aleatwaman
    pozalea1= random.randint(2,wote_entefas - 2)
    pozalea2 = random.randint(2,laje_entefas-2)

#Reafficher entefas la ak obstak la nan yon pozisyon aleatwa
    for i in range(laje_entefas):
        if i == 0 or i == laje_entefas - 1:
            print(karakte_lage * laje_entefas)
        elif i == pozalea2:
         print(karakte_ote + " " * pozalea1 + obstak + "     " + karakte_ote)
        else:
                print(karakte_ote + "  " * (wote_entefas) + karakte_ote)
