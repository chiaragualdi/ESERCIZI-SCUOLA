while True:
    print("Inserire q per calcolare l'area di un quadrato, r di un rettangolo, t di un triangolo e c di un cerchio, qualsiasi altro valore per interrompere il programma:")
    start=input()
    if start=="q":
        l=int(input("Inserisci il lato del quadrato: "))
        Aq=l*l
        print("L'area del quadrato è di", Aq)
    elif start=="r":
        baser=int(input("Inserisci la base del rettangolo: "))
        hr=int(input("Inserisci l'altezza del rettangolo: "))
        Ar=baser*hr
        print("L'area del rettangolo è di", Ar)
    elif start=="t":
        baset=int(input("Inserisci la base del triangolo: "))
        ht=int(input("Inserisci l'altezza del triangolo: "))
        At=baset*ht
        At=At/2
        print("L'area del triangolo è di", At)
    elif start=="c":
        raggio=int(input("Inserisci il raggio del cerchio: "))
        Ac=raggio*raggio*3.14
        print("L'area del cerchio è di", Ac)
    else:
        False
