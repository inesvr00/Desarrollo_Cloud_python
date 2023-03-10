# Ejercicio 7A
# Escribe una función que calcule el interés de una inversion.

# Entrada de datos:

# Importe total
# Interés anual
# Salida de datos:

# Importe invertido + beneficios a un día, un mes, un trimestre, un semestre y un año

def calcular_interes_inversion(importe, interes_anual):
    interes_diario = interes_anual / 365
    beneficio_dia = importe * interes_diario
    beneficio_mes = importe * (interes_anual / 12)
    beneficio_trimestre = importe * (interes_anual / 4)
    beneficio_semestre = importe * (interes_anual / 2)
    beneficio_anual = importe * interes_anual
    
    print(f"Importe invertido: ${importe:.2f}")
    print(f"Beneficio a un día: ${beneficio_dia:.2f}")
    print(f"Beneficio a un mes: ${beneficio_mes:.2f}")
    print(f"Beneficio a un trimestre: ${beneficio_trimestre:.2f}")
    print(f"Beneficio a un semestre: ${beneficio_semestre:.2f}")
    print(f"Beneficio a un año: ${beneficio_anual:.2f}")