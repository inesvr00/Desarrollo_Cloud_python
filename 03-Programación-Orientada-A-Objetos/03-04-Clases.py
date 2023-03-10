import datetime

class Alumno:
    """"Comentarios del uso de la clase"""
    # Variables o propiedades de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None
    
    # Función constructoraa que se ejecuta al crear (instanciar) el objeto
    # self, una variable que representa al mismo objeto
    
    def __init__(self, nombre, apellido1, apellido2 = "") -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2
    
    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    
    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if (len(fecha) == 10):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            return True
        except:
            return False
        
    def getEdad(self) -> int:
        if (self.FechaNacimiento == None):
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento.year
        
# Creamos un objeto(instanciamos un objeto) ejecutando la función constructora
alumno = Alumno("Borja", "Rozas", "Peñasco")
alumno2 = Alumno("Inés", "Victoria")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno2.getNombreCompleto()}")

alumno.setFechaNacimiento("11-09-99")
print(alumno2.setFechaNacimiento("17-11-00"))
resultado = alumno.setFechaNacimiento("11-09-99")

if(resultado == True):
    print("Fecha de nacimiento asignada correctamente.")
else:
    print("Error al asignar fecha de nacimiento")
#Copiar de github aquí te faltan cosas
    
