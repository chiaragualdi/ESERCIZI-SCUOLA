'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono,
oppure un messaggio nel caso la persona non sia presente nella rubrica.
'''
d={
    "nonno":3285677342,
    "nonna":3224322282,
    "mamma":3205543478,
    "papà":3286789101,
    "sorella":3241234567,
    "cugina":3275355678,
    "zio":3206934561,
    "cugino":3285055321
    }
print("Per fermare il programma inserire stop.")
while True:
    persona=input("Inserire il nome della persona della famiglia di cui vuoi sapere il numero: ")
    if persona in d:
        print(d[persona])
    elif persona=="stop":
        break
    else:
        print("La persona richiesta non è presente nella rubrica.")
