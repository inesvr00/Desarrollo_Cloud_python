"""
Contruye un objeto que permita insertar, actulizar, eliminar y consultar los datos de un Alumno.
    Consultar mediante GET -> api/people/<id> por ejemplo api/people/5 -> Retorna 200 OK
    Consultar listado  GET -> api/people/ -> Retorna 200 OK
    
    Insertar mediante POST -> api/people + datos en JSON en el Body -> Retorna 201 Created + Id del nuevo alumno
    
    Actualizar mediante PUT -> api/people/<id> por ejemplo api/people/5 + datos en JSON en el Body -> Retorna 204 NoContent
    
    Eliminar mediante DELETE -> api/people/<id> por ejemplo api/people/5 -> Retorna 204 NoContent
    ATENCIÓN, eliminar solo los alumnos creados por vosotros
"""
import requests
import pprint
from tabulate import tabulate

# Colección de URLs utilizadas
url = {
    'Base': 'http://eoi-api.eastus.cloudapp.azure.com/api/',
    'Alumnos': 'http://eoi-api.eastus.cloudapp.azure.com/api/people/',
}

response_alumnos = requests.get(url['Alumnos'])
print("Consultar listado  GET -> api/people/")
print(f"Código de Estado: ", response_alumnos.status_code)
print(f"Estado: ", response_alumnos.reason)
print("")

print("Consultar mediante GET -> api/people/<id> por ejemplo api/people/8")
response_alumno_8 = requests.get(url['Alumnos']+'8')
print(f"Código de Estado: ", response_alumno_8.status_code)
print(f"Estado: ", response_alumno_8.reason)
print("")

import requests
import json
import datetime
from dateutil.parser import parse


class Alumnos:
    def __init__(self, base_url):
        self.base_url = base_url
        self.alumnos_url = base_url + 'people/'

    def listar_alumnos(self):
        response = requests.get(self.alumnos_url)
        if response.status_code == 200:
            alumnos = response.json()
            headers = ['ID', 'Nombre', 'Apellido', 'Fecha de inscripción']
            tabla = []
            for alumno in alumnos:
                id = alumno['personID']
                nombre = alumno['firstName']
                apellido = alumno['lastName']
                if alumno['enrollmentDate'] is not None:
                    fecha_inscripcion = parse(alumno['enrollmentDate']).strftime('%Y-%m-%d')
                else:
                    fecha_inscripcion = 'No disponible'
                fila = [id, nombre, apellido, fecha_inscripcion]
                tabla.append(fila)
            return tabulate(tabla, headers=headers, tablefmt='pretty')
        else:
            return None

    def consultar_alumno(self, id):
        response = requests.get(self.alumnos_url + str(id))
        if response.status_code == 200:
            alumno = response.json()
            id = alumno['personID']
            nombre = alumno['firstName']
            apellido = alumno['lastName']
            if alumno['enrollmentDate'] is not None:
                fecha_inscripcion = parse(alumno['enrollmentDate']).strftime('%Y-%m-%d')
            else:
                fecha_inscripcion = 'No disponible'
            headers = ['ID', 'Nombre', 'Apellido', 'Fecha de inscripción']
            tabla = [[id, nombre, apellido, fecha_inscripcion]]
            return tabulate(tabla, headers=headers, tablefmt='pretty')
        else:
            return None

    def insertar_alumno(self):
        # Se le pide al usuario los datos del alumno
        id = input("ID del alumno: ")
        nombre = input("Nombre del alumno (requerido): ")
        apellido = input("Apellido del alumno: ")
        fecha_inscripcion = input("Fecha de inscripción (YYYY-MM-DD): ")
        if fecha_inscripcion:
            fecha_inscripcion = parse(fecha_inscripcion).isoformat()
        else:
            fecha_inscripcion = None
        hire_date = None
        office = None
        grades = [],
        courses = [],
        data = {
            'personID': id,
            'firstName': nombre,
            'lastName': apellido,
            'enrollmentDate': fecha_inscripcion,
            'hireDate': hire_date,
            'officeAssignment': office,
            'studentGrades': grades,
            'courses': courses
        }

        # Comprobar si ya existe un alumno con ese ID
        response = requests.get(self.alumnos_url + str(id))
        if response.status_code == 200:
            print(f"El ID {id} ya está en uso.")
            return None

        # Si el ID no está siendo utilizado se le añade a la lista
        response = requests.post(self.alumnos_url, json=data)
        print(f"Código de Estado: ", response.status_code)
        if response.status_code == 201:
            # Si el alumno fue añadido correctamente se imprime su información
            id = response.json()
            headers = ['ID', 'Nombre', 'Apellido', 'Fecha de inscripción']
            tabla = [[id, nombre, apellido, fecha_inscripcion]]
            return tabulate(tabla, headers=headers, tablefmt='pretty')
        else:
            # Si ocurre un error retorna None
            print("Ha ocurrido un error.")
            print(response.json())
            return None



    def actualizar_alumno(self, id, datos_alumno):
        headers = {'Content-type': 'application/json'}
        response = requests.put(self.alumnos_url + str(id), data=json.dumps(datos_alumno), headers=headers)
        if response.status_code == 204:
            return True
        else:
            return False

    def eliminar_alumno(self, id):
        response = requests.delete(self.alumnos_url + str(id))
        if response.status_code == 204:
            return True
        else:
            return False

api = Alumnos('http://eoi-api.eastus.cloudapp.azure.com/api/')

# Listar todos los alumnos
alumnos = api.listar_alumnos()
print(alumnos)
print("\n")

# Consultar un alumno por su ID
alumno = api.consultar_alumno(3)
print(alumno)

# Insertar un nuevo alumno
api.insertar_alumno()

# # Actualizar un alumno existente
# datos_actualizados = {'FirstName': 'Juan', 'LastName': 'García', 'EnrollmentDate': '2023-04-09'}
# actualizado = api.actualizar_alumno(8, datos_actualizados)
# print(actualizado)

# # Eliminar un alumno existente
# eliminado = api.eliminar_alumno(8)
# print(eliminado)

