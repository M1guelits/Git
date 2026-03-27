print("Bienvenido al mega cachi-pun")
nombre = input("Ingresa tu nombre")
print(f"Ok {nombre}, jugaras contra la terminal de vscode! Las reglas son simples")

roca_debilidades = [papel, spock]

lagarto_debilidades = [roca, tijeras]

spock_debilidades = [lagarto, papel]

tijeras_debilidades = [roca, spock]

papel_debilidades = [tijeras, lagarto]

lista_movimientos = [roca, papel, tijeras, lagarto, spock]

def jugar(movimiento):
    if movimiento == "roca" and random.choice(lista_movimientos) not in roca_debilidades:
        print("VICTORIA: Aplastante!" )
        return True
    elif movimiento == "roca" and random.choice(lista_movimientos) in roca_debilidades:
        print("DERROTA: Pierde roca")
        return False

    if movimiento == "lagarto" and random.choice(lista_movimientos) not in lagarto_debilidades:
        print("VICTORIA: Ataque reptil")
        return True
    elif movimiento == "lagarto" and random.choice(lista_movimientos) in roca_debilidades:
        print("DERROTA: Masacrado a sangre fría")
        return False

    if movimiento == "spock" and random.choice(lista_movimientos) not in spock_debilidades:
        print("VICTORIA: Dedos separados") 
        return True
    elif movimiento == "spock" and random.choice(lista_movimientos) in spock_debilidades:
        print("DERROTA: Devuelvete a Star-Trek")
        return False

    if movimiento == "tijeras" and random.choice(lista_movimientos) not in tijeras_debilidades:
        print("VICTORIA: Tajadura") 
        return True
    elif movimiento == "tijeras" and random.choice(lista_movimientos) in tijeras_debilidades:
        print("DERROTA: Quebrantado") 
        return False

    if movimiento == "papel" and random.choice(lista_movimientos) not in papel_debilidades:
        print("VICTORIA: Envoltura")
        return True
    elif movimiento == "papel" and random.choice(lista_movimientos) in papel_debilidades:
        print("DERROTA: Papel roto") 
        return False

    

