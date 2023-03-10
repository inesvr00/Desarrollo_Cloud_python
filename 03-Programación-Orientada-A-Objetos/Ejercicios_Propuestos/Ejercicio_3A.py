# Escribe una función que calcule los impuesto a pagar depediendo el salario.

# Tabla: Menos de 10.000 5% Entre 10.000 y 20.000 15% Entre 20.000 y 35.000 20% Entre 35.000 y 60.000 30% Más de 60.000 45%

#         En concepto de desempleo     4%
#         En concepto de formación   1,2%


# Entrada de datos:

# Salario
# Salida de datos:

# Datos desglosados

def Calculadora_De_Impuestos (ingresos):
    try:
        ingresos = int(ingresos)
    except ValueError:
        return "El ingreso debe ser un número entero o decimal"
    
    if ingresos < 0:
        return "El salario no puede ser negativo"
    
    elif ingresos == 0:
        estado = input("Introduce si estás desempleado o eres estudiante: ").lower()
        if estado == "desempleado":
            porcentaje = 4
            impuesto = ingresos * 0.04
            return f"El porcentaje a pagar es del {porcentaje}%. El impuesto a pagar es del {impuesto:.1f}%"
        elif estado == "estudiante":
            porcentaje = 1.2
            impuesto = ingresos * 0.012
            return f"El porcentaje a pagar es del {porcentaje}%. El impuesto a pagar es del {impuesto:.1f}%"
        else:
            return "Por favor escribe desempleado o estudiante"
    else:
        if ingresos < 10000:
            porcentaje = 5
            impuesto = ingresos * 0.05
        elif ingresos < 20000:
            porcentaje = 15
            impuesto = ingresos * 0.15
        elif ingresos < 35000:
            porcentaje = 20
            impuesto = ingresos * 0.2
        elif ingresos < 60000:
            porcentaje = 30
            impuesto = ingresos * 0.3
        else:
            porcentaje = 45
            impuesto = ingresos * 0.45

        return f"El impuesto a pagar es del {porcentaje}%, por que el impuesto total sobre el sueldo de {ingresos}€ es de {impuesto}€"
    
print(Calculadora_De_Impuestos(25000))