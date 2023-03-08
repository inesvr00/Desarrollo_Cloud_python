#####################################################
# Requerimientos funcionales:                       #
#                                                   #
#   - Visualizar la media de opinión                #
#   - Visualizar nº total de encuestas              #
#   - Resultado se muestra al escribir FIN          #
#   - Visualizar el promedio por edades: <18, 18-55 #
#     >55                                           #
#####################################################
# Utilizando listas de Python                       #
# Valores entre 0-10                                #
#####################################################

lista_18 = []
lista_18_55 = []
lista_55 = []
encuesta = True

while encuesta == True:
    edad_q = True
    while edad_q == True:
        edad = (input("Introduce tu edad o fin: "))
        if edad.lower() == "fin":
            encuesta = False
            edad_q = False
            print("La recogida de puntuaciones ha finalizado")
        else:
            try:
                edad = int(edad)
                edad_q = False  
                pun_q = True   
            except:
                print("Introduce tu edad en números.")
    

    while pun_q == True:            
        puntuacion = input("Introduce la puntuación (0-10) a la encuesta: ")
        try:
            puntuacion = int(puntuacion)
            if 0 <= puntuacion <= 10:
                if edad > 55:
                    lista_55.append(puntuacion)
                    pun_q = False
                elif edad < 18:
                    lista_18.append(puntuacion)
                    pun_q = False
                else:
                    lista_18_55.append(puntuacion)
                    pun_q = False
            else:
                print("Introduce un valor del 0-10 o FIN 1.")
        except:
            print("Introduce un valor numérico")
        
    
if len(lista_18) == 0:
    print("No existen participantes menores de 18 años")
else:
    media_pun_18 = sum(lista_18) / len(lista_18)
    print(f"La puntuación media de personas menores de 18 años es {media_pun_18} para {len(lista_18)} encuestados.")
    
if len(lista_18_55) == 0:
    print("No existen participantes de entre 18 y 55 años.")
else:
    media_pun_18_55 = sum(lista_18_55) / len(lista_18_55)
    print(f"La puntuación media de personas menores de entre 18 y 55 años es {media_pun_18_55} para {len(lista_18_55)} encuestados.")
    
if len(lista_55) == 0:
    print("No existen participantes mayores de 55 años.")
else: 
    media_pun_55 = sum(lista_55) / len(lista_55)
    print(f"La puntuación media de personas mayores de 55 años es {media_pun_55} para {len(lista_55)} encuestados.")
           
