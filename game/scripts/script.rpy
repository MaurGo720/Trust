init:
    # Definir personajes
    define s = Character("Dr. Samuel Vázquez", color="#FF0000")
    define e = Character("Elena Ramírez", color="#00FF00")

    # Cargar imágenes
    image bg_hospital_pasillo = "escena_1_pasillo/pasillo.jpg"
    image bg_hospital_quirofano = "escena_2_quirofano/quirofano.jpg"
    image bg_hospital_sotano = "escena_3_sotano.jpg"


label start:

    scene bg_hospital_pasillo
    with fade

    s "Parece que la tormenta ha cortado la electricidad..."
    e "No es solo eso, doctor. Algo está mal en este hospital."

    scene bg_hospital_quirofano
    with fade

    s "Aquí es donde comenzaron los experimentos. Hay documentos en la mesa."
    e "Tal vez si encontramos la verdad, podremos salir de aquí con vida."

    menu:
        "Revisar los documentos detenidamente":
            jump investigacion

        "Buscar una salida inmediata":
            jump escape

label investigacion:
    scene bg_hospital_sotano
    with fade

    e "Esto no tiene sentido... Las fechas, los nombres... ¡Dios mío!"
    s "Es demasiado tarde. Nos han visto."

    return # Final malo

label escape:
    scene bg_hospital_pasillo
    with fade

    s "¡Corre, Elena! ¡Ahora!"
    e "¡Pero doctor, usted...!"

    menu:
        "Elena escapa sola":
            jump final_escape_sola

        "Samuel se sacrifica para que Elena escape":
            jump final_sacrificio

label final_escape_sola:
    e "Lo siento... No puedo quedarme..."
    return # Final de escape

label final_sacrificio:
    s "Corre... y cuéntales la verdad."
    return # Final trágico