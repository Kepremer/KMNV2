if m==1:
    while True:
        print("Kes mangime? esc - valja, enter - mangime")
        if read_key()=='enter':
            p1=choice(v1)
            print("Esimene bot: ",p1)
            p2=choice(v2)
            print("Teine bot: ",p2)
            if p1==p2:
                print("Viik")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1 and p2==v2[2]:
                print ("Voitis 1")
            else:
                print ("Voitis 2")
