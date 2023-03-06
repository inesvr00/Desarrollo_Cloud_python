#####################################################
# Requerimientos funcionales:                       #
#                                                   #
#   - Calcular la letra del DNI                     #
#   - Formular: dni % 23                            #
#                                                   #
#####################################################

letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J',
          'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

try:
    dni = int(input("Introduce tu número del dni: "))
except:
    print("El valor introducido debe ser un número entero de 8 dígitos.")
    exit()
    
if dni < 99999999:
    rest = dni % 23
    letra = letras[rest]
    print(f"Tu letra del dni es {letra}")
else:
    print("El valor introducido debe tener 8 dígitos.")
