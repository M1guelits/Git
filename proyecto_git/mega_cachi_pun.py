import random
print("Bienvenido al mega cachi-pun")
nombre = input("Ingresa tu nombre antes de jugar -> ")
print(f"Ok {nombre}, jugaras contra la terminal de vscode! Las reglas son simples")

roca_debilidades = ["papel", "spock"]

lagarto_debilidades = ["roca", "tijeras"]

spock_debilidades = ["lagarto", "papel"]

tijeras_debilidades = ["roca", "spock"]

papel_debilidades = ["tijeras", "lagarto"]

lista_movimientos = ["roca", "papel", "tijeras", "lagarto", "spock"]

def jugar(movimiento):
    if movimiento == "roca" and random.choice(lista_movimientos)=="roca":
        return "empate"
    if movimiento == "roca" and random.choice(lista_movimientos) not in roca_debilidades:
        print("VICTORIA: Aplastante!" )
        return True
    elif movimiento == "roca" and random.choice(lista_movimientos) in roca_debilidades:
        print("DERROTA: Pierde roca")
        return False
    if movimiento == "lagarto" and random.choice(lista_movimientos)=="lagarto":
        return "empate"
    if movimiento == "lagarto" and random.choice(lista_movimientos) not in lagarto_debilidades:
        print("VICTORIA: Ataque reptil")
        return True
    elif movimiento == "lagarto" and random.choice(lista_movimientos) in roca_debilidades:
        print("DERROTA: Masacrado a sangre fría")
        return False
    if movimiento == "spock" and random.choice(lista_movimientos)=="spock":
        return "empate"
    if movimiento == "spock" and random.choice(lista_movimientos) not in spock_debilidades:
        print("VICTORIA: Dedos separados") 
        return True
    elif movimiento == "spock" and random.choice(lista_movimientos) in spock_debilidades:
        print("DERROTA: Devuelvete a Star-Trek")
        return False
    if movimiento == "tijeras" and random.choice(lista_movimientos)=="tijeras":
        return "empate"
    if movimiento == "tijeras" and random.choice(lista_movimientos) not in tijeras_debilidades:
        print("VICTORIA: Tajadura") 
        return True
    elif movimiento == "tijeras" and random.choice(lista_movimientos) in tijeras_debilidades:
        print("DERROTA: Quebrantado") 
        return False
    if movimiento == "papel" and random.choice(lista_movimientos)=="papel":
        return "empate"
    if movimiento == "papel" and random.choice(lista_movimientos) not in papel_debilidades:
        print("VICTORIA: Envoltura")
        return True
    elif movimiento == "papel" and random.choice(lista_movimientos) in papel_debilidades:
        print("DERROTA: Papel roto") 
        return False
#bucle del juego (vicho)
puntaje_yo=0
puntaje_terminal=0
while True:
    move=input("Elige entre roca, lagarto, spock, tijeras o papel -> ")
    if jugar(move)==True:
        puntaje_yo+=1
    elif jugar(move)==False:
        puntaje_terminal+=1
    elif jugar(move)=="empate":
        print("EMPATE")
    if puntaje_terminal==10:
        print("HA GANADO LA TERMINAL")
        break
    if puntaje_yo==10:
        print(f"HAS GANADO {nombre} FELICIDADES")
        break
    print(f"{nombre} {puntaje_yo} - TERMINAL {puntaje_terminal}")
print("PUNTAJE FINAL")
print(f"{nombre} {puntaje_yo} - TERMINAL {puntaje_terminal}")