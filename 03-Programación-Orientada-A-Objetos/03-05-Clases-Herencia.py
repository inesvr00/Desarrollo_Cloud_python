#####################################################################
# Herencia                                                          #
#####################################################################
#                                                                   #
#   Sintaxis: class [nombre de la clase]([clase base]):             #
#                                                                   #
#   Ejemplos:                                                       #
#       class Estudiante(Alumno):                                   #
#                                                                   #
#####################################################################
from datetime import datetime

# Definición de la clase ALUMNO
class Alumno:
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    def __init__(self, nombre, apellido1, apellido2="") -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

    def getNombreCompleto(self) -> str:
        return f"{self.Apellido1} {self.Apellido2}, {self.Nombre}"

    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if (len(fecha) == 10):
                self.FechaNacimiento = datetime.strptime(
                    fecha, "%d-%m-%Y").date()
            else:
                self.FechaNacimiento = datetime.strptime(
                    fecha, "%d-%m-%y").date()

            return True
        except:
            return False

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None):
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento.year

# Definición de la clase ESTUDIANTE, que hereda de la clase ALUMNO
class Estudiante(Alumno):
    # Añadimos una variable Curso
    Curso = None

    # Sobreescribimos la función contructora del objeto
    def __init__(self, nombre, apellido1, curso) -> None:
        #self.Nombre = nombre
        #self.Apellido1 = apellido1
        #self.Apellido2 = ""
        # Las lineas superiores comentadas no son necesarias escribirlas ya que están en la
        # clase base y las podemos invocar con la función super()
        super().__init__(nombre, apellido1)
        self.Curso = curso

    # Sobreescribimos la función getNombreCompleto
    def getNombreCompleto(self) -> str:
        return f"{super().getNombreCompleto()} - ({self.FechaNacimiento})"

    # Añadimos una nueva función
    def test(self):
        return "función test"


# Creamos (instaciamos) un objeto Alumno
alumno = Alumno("Borja", "Cabeza")
print(f"Me llamo: {alumno.getNombreCompleto()}")


# Creamos (instaciamos) un objeto Estudiante.
# Utilizamos la nueva función constructora y la nueva variable Curso
estudiante = Estudiante("Borja", "Cabeza", "1A")
print(f"Me llamo: {estudiante.getNombreCompleto()}")
print(f"Curso: {estudiante.Curso}")