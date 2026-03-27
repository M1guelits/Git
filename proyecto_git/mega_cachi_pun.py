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
    movimiento_maquina = random.choice(lista_movimientos)
    if movimiento == "roca" and movimiento_maquina=="roca":
        return "empate"
    if movimiento == "roca" and movimiento_maquina not in roca_debilidades:
        print("VICTORIA: Aplastante!" )
        return True
    if movimiento == "roca" and movimiento_maquina in roca_debilidades:
        print("DERROTA: Pierde roca")
        return False
    if movimiento == "lagarto" and movimiento_maquina=="lagarto":
        return "empate"
    if movimiento == "lagarto" and movimiento_maquina not in lagarto_debilidades:
        print("VICTORIA: Ataque reptil")
        return True
    if movimiento == "lagarto" and movimiento_maquina in lagarto_debilidades:
        print("DERROTA: Masacrado a sangre fría")
        return False
    if movimiento == "spock" and movimiento_maquina=="spock":
        return "empate"
    if movimiento == "spock" and movimiento_maquina not in spock_debilidades:
        print("VICTORIA: Dedos separados") 
        return True
    if movimiento == "spock" and movimiento_maquina in spock_debilidades:
        print("DERROTA: Devuelvete a Star-Trek")
        return False
    if movimiento == "tijeras" and movimiento_maquina=="tijeras":
        return "empate"
    if movimiento == "tijeras" and movimiento_maquina not in tijeras_debilidades:
        print("VICTORIA: Tajadura") 
        return True
    if movimiento == "tijeras" and movimiento_maquina in tijeras_debilidades:
        print("DERROTA: Quebrantado") 
        return False
    if movimiento == "papel" and movimiento_maquina=="papel":
        return "empate"
    if movimiento == "papel" and movimiento_maquina not in papel_debilidades:
        print("VICTORIA: Envoltura")
        return True
    if movimiento == "papel" and movimiento_maquina in papel_debilidades:
        print("DERROTA: Papel roto") 
        return False
#bucle del juego (vicho)
puntaje_yo=0
puntaje_terminal=0
while True:
    move=input("Elige entre roca, lagarto, spock, tijeras o papel -> ")
    if jugar(move)==True:
        puntaje_yo+=1
    if jugar(move)==False:
        puntaje_terminal+=1
    if jugar(move)=="empate":
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