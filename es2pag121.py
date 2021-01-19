#Data la parabola y = ax² + bx + c, definisci due funzioni per calcolarne vertice e fuoco.
#Le due funzioni ricevono come parametri a, b, c e restituiscono il valore calcolato.
 

def calcolo_vertice(a, b, c):
    delta = b**2 - 4*a*c
    x_vertice = -b/2*a
    y_vertice = -delta/4*a
    return x_vertice, y_vertice
def calcolo_fuoco(a, b, c):
    delta = b**2 - 4*a*c
    x_fuoco = -b/2*a
    y_fuoco = (1-delta)/4*a
    return x_fuoco, y_fuoco
def main():
    a = int(input("Inserisci il valore di a: "))
    b = int(input("Inserisci il valore di b: "))
    c = int(input("Inserisci il valore di c: "))
    vertice = calcolo_vertice(a, b, c)
    fuoco = calcolo_fuoco(a, b, c)
    print("Le coordinate del vertice sono: ", vertice)
    print("Le coordinate del fuoco sono: ",fuoco)
main()
