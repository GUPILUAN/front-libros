class Libro():
    __id : str
    __titulo : str
    __autor : str
    __isbn : str

    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}"
    
    def convertirToDict(self) -> dict:
        return {"titulo": self.__titulo, "autor" : self.__autor, "isbn" : self.__isbn}  
      
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor
    
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn