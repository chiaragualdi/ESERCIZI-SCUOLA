#Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e sull'imposta media.

perc_tasse={
    15000:(15000, 23),
    28000:(13000, 27),
    55000:(27000 ,38),
    75000:(20000, 41),
    1000000000000:(0, 43)
}
tasse=0
reddito=int(input("Inserire il reddito: "))
        
reddito_rid=reddito
for valore in perc_tasse:
    if reddito_rid>=valore:
        reddito_rid-=perc_tasse[valore][0]
        tasse+=(perc_tasse[valore][0]*perc_tasse[valore][1])/100
    else:
        tasse+=(reddito_rid*perc_tasse[valore][1])/100
        break
tasse=round(tasse, 2)
importo_media=round(tasse/reddito*100, 2)
print("Le tasse imposte sono {}\nCioè il {}% del reddito({})".format(tasse, importo_media, reddito))