class Demo:
    def __secreto(self):
        print("Nadie puede saber")
        
    def publico(self):
        print("Todos lo pueden saber")
    
    def getSecret(self, pw):
        if (pw == "12345"):
            print(self.__secreto())
        else:
            print("Sin acceso")
            
demo = Demo()
demo.publico()
demo.getSecret("12345")
demo.getSecret("54624")
print(dir(demo))
demo._Demo__secreto() 
        