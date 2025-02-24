define Ma = Character("Matias")



label start:

    scene bg room

    show eileen happy

    # Presenta las líneas del diálogo.

    Ma "Hola soy Matias"

    Ma "¿A donde vamos ahora?"

    Ma "que te parece hacer?"

    call visita

    Ma "Me encanto la visita, nos vemos"

    # Finaliza el juego:

    return

label visita:
    menu:
        "Podemos ir a..."
        "Heladeria":
            jump heladeria
        "Bombonera":
            jump bombonera
return

label heladeria:
    scene bg heladeria

    show eileen happy
    Ma "Me encantan los helados"
return


label bombonera:
    scene bg bombonera

    show eileen happy
    Ma "Yo soy del boca papaaaaaa"
return
