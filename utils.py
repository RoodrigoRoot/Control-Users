from BDUsers import BD_users
from Users import User

class UserMethod:
    
    @classmethod
    def add_user(cls, user_list):
        print("*****Agregar usuario*****")
        name = input("Ingrese el nombre del usuario: ")
        last_name = input("Ingrese el país del usuario: ")
        age = input("Ingrese el nombre de usuario: ")
        user = User(name, last_name, age)
        user_list.append(user)
        print("******************************")
        print("Usuario Agregado")
        print("******************************\n")
        return user_list
    
    @classmethod
    def delete_user(cls, user_list):
        print("*****Borrar usuario*****")
        id_user = input("Ingrese el id del usuario: ")
        for index, user in enumerate(user_list):
            if user.id == id_user:
                print(user_list.pop(index))
                print("******************************")
                print("Usuario Eliminado")
                print("******************************\n")
    
    @classmethod
    def search_user(cls, user_list):
        print("*****Buscar usuario*****")
        id_user = input("Ingrese el id del usuaio a buscar: ")
        for index, user in enumerate(user_list):
            if user.id == id_user:
                print("******************************")
                print(user_list[index])
        print("******************************")
        pass
    
    @classmethod
    def print_users(cls, user_list):
        print("\n*****Lista de usuarios registrados:*****")
        for user in user_list:
            print(user)
        print("******************************\n")

  
list_users = BD_users()

def menu():
    menu = """Control de Usuarios
**Escoge una opción**
1.-Agregar Usuario
2.-Buscar Usuario
3.-Eliminar Usuario
4.-Mostrar todos los Usuarios
5.-Salir
Opción: """

    while True:
        option = int(input(menu))
        if option == 5:
            break
        selected_option(option, list_users)
    
        
def selected_option(option, user_list):
    
    if option == 1:  
        UserMethod.add_user(user_list)
    elif option == 2:
        UserMethod.search_user(user_list)
    
    elif option == 3:
        UserMethod.delete_user(user_list)
    
    elif option == 4:
        UserMethod.print_users(user_list)
        