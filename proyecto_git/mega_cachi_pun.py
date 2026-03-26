print("Bienvenido al mega cachi-pun")

roca_debilidades = [papel, spock]

lagarto_debilidades = [roca, tijeras]

spock_debilidades = [lagarto, papel]

tijeras_debilidades = [roca, spock]

papel_debilidades = [tijeras, lagarto]

lista_movimientos = [roca, papel, tijeras, lagarto, spock]

def jugar(movimiento):
    if movimiento == "roca" and random.choice(lista_movimientos) not in roca_debilidades:
        return "VICTORIA: Aplastante!"
    elif movimiento == "roca" and random.choice(lista_movimientos) in roca_debilidades:
        return "DERROTA: Pierde roca"
    if movimiento == "lagarto" and random.choice(lista_movimientos) not in lagarto_debilidades:
        return "VICTORIA: Ataque reptil"
    elif movimiento == "lagarto" and random.choice(lista_movimientos) in roca_debilidades:
        return "DERROTA: Masacrado a sangre fría"
    if movimiento == "spock" and random.choice(lista_movimientos) not in spock_debilidades:
        return "VICTORIA: Dedos separados"
    elif movimiento == "spock" and random.choice(lista_movimientos) in spock_debilidades:
        return "DERROTA: Devuelvete a Star-Trek"
    if movimiento == "tijeras" and random.choice(lista_movimientos) not in tijeras_debilidades:
        return "VICTORIA: Tajadura"
    elif movimiento == "tijeras" and random.choice(lista_movimientos) in tijeras_debilidades:
        return "DERROTA: Quebrantado"
    if movimiento == "papel" and random.choice(lista_movimientos) not in papel_debilidades:
        return "VICTORIA: Envoltura"
    elif movimiento == "papel" and random.choice(lista_movimientos) in papel_debilidades:
        return "DERROTA: Papel roto"
