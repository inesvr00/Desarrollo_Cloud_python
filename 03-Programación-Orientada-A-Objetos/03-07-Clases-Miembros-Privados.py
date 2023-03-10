#####################################################################
# Miembros privados                                                 #
#####################################################################
"""
Las variables «privadas», que no pueden accederse excepto desde dentro de un objeto,
no existen en Python. 
Sin embargo, hay una convención que se sigue en la mayoría del código Python: un nombre 
prefijado con un guión bajo (por ejemplo, _spam) debería tratarse como una parte no pública.
 Cualquier identificador con la forma __spam (al menos dos guiones bajos al principio,
 como mucho un guión bajo al final) es textualmente reemplazado por _nombredeclase__spam.
"""

class Demo:
    def __secreto(self):
        print("Nadie puede saber")

    def publico(self):
        print("Todos puede saber")

    def getSecreto(self, pw):
        if(pw == "12345"):
            self.__secreto()
        else:
            print("Sin acceso")

demo = Demo()
demo.publico()
demo.getSecreto("12345")
print(dir(demo))
demo._Demo__secreto()