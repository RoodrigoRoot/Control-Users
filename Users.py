import uuid

class User: 
    def __init__(self, name, country, username):
        self.__name = name
        self.__country = country
        self.__username = username
        self.__id = str(uuid.uuid4())[:4]

    def __str__(self):
        return "id: {} Nombre: {} Apellido: {} Usuario: {}".format(str(self.__id),
                                                       self.__name,
                                                       self.__country,
                                                       self.__username)    
    @property
    def id(self):
        return self.__id


