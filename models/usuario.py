class Usuario():
    __id : str
    __nombre : str
    __email : str
    __password : str

    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Email: {self.__email}, Password: {len(self.__password) * '*'}"
    
    def convertirToDict(self) -> dict:
        return {"nombre": self.__nombre, "email" : self.__email, "password" : self.__password}  
      
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password