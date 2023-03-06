#####################################################
# Requerimientos funcionales:                       #
#                                                   #
#   - Visualizar la media de opinión                #
#   - Visualizar nº total de encuestas              #
#   - Resultado se muestra al escribir FIN          #
#####################################################
# Utilizando listas de Python                       #
# Valores entre 0-10                                #
#####################################################

encuesta = True
lista_pun = []

while encuesta == True:
    puntuacion = input("Introduce la puntuación (0-10) a la encuesta o FIN para terminar: ")
    if puntuacion == "FIN" or puntuacion == "fin" or puntuacion == "Fin" or puntuacion == "fIN":
        encuesta = False
        print("La recogida de puntuaciones ha finalizado")
    else:
        if 0 <= puntuacion <= 10:
            try:
                lista_pun.append(int(puntuacion))
            except:
                print("El valor introducido no es válido. Introduce un número entero o FIN")
        else:
            print("Introduce un valor del 0-10.")
            
media_pun = sum(lista_pun) / len(lista_pun)
print(f"La puntuación media es {media_pun} para {len(lista_pun)} encuestas.")
    