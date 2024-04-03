from prettytable import PrettyTable
import random
from werkzeug.security import generate_password_hash


#Lista con los nombres de 10 de sus futuros usuarios de tu aplicación 
class Futurosusuarios:
    def __init__(self, id, nombre, contraseña, telefono):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.telefono = telefono
       
list_futuros_usuarios = [
    Futurosusuarios("P001", "Hector Carrasco", "", ""),
    Futurosusuarios("P002", "Jacinta Carrasco", "", ""),
    Futurosusuarios("P003", "Josefina Carrasco", "", ""),
    Futurosusuarios("P004", "Carlos Carrasco", "", ""),
    Futurosusuarios("P005", "Juan Carrasco", "", ""),
    Futurosusuarios("P006", "Maxi Carrasco", "", ""),
    Futurosusuarios("P007", "Emma Carrasco", "", ""),
    Futurosusuarios("P008", "Gillermo Carrasco", "", ""),
    Futurosusuarios("P009", "Eduardo Carrasco", "", ""),
    Futurosusuarios("P010", "Belen Carrasco", "", "")
]
#fin de la Lista con los nombres de 10 de sus futuros usuarios de tu aplicación 

#Imprime por pantalla los futuros usuarios de tu aplicación
def imprimir_productos():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre"]
    for usuarios in list_futuros_usuarios:
        tabla.add_row([usuarios.id, usuarios.nombre])
    print(tabla)
#Imprime por pantalla los futuros usuarios de tu aplicación (hatsa con con contraseña)    
def imprimir_productos_contraseña():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Contraseña"]
    for usuarios in list_futuros_usuarios:
        tabla.add_row([usuarios.id, usuarios.nombre,usuarios.contraseña])
    print(tabla)
#Imprime por pantalla los futuros usuarios de tu aplicación sumando el telefono
def imprimir_usuario_telefono():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Telefono"]
    for usuarios in list_futuros_usuarios:
        tabla.add_row([usuarios.id, usuarios.nombre,usuarios.telefono])
    print(tabla)
    
#La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
#En este caso no se solicita simbolos pero que en codigo para casos posteriores 
# simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
#base = minus+mayus+numeros+simbolos
base = minus+mayus+numeros
longitud = 12
posicion = 0
print("***Lista Variables con Contraseñas***") 
for usuarios in list_futuros_usuarios:
    
    for _ in range(1):
        muestra = random.sample(base, longitud)
        password = "".join(muestra)
        password_encriptado = generate_password_hash(password)#queda en el codigo solo para casoso posteriores (encriptado)
        # print("{} => {}".format(password, password_encriptado))
        # print("{}".format(password))
        # print(password)
        list_futuros_usuarios[posicion].contraseña=password 
       #Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
        if posicion == 0:
          variable1 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
          print(variable1)
        elif posicion == 1:
         variable2 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable2)
        elif posicion == 2:
         variable3 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable3)
        elif posicion == 3:
         variable4 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable4)
        elif posicion == 4:
         variable5 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable5)
        elif posicion == 5:
         variable6 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable6)
        elif posicion == 6:
         variable7 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable7)
        elif posicion == 7:
         variable8 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable8)
        elif posicion == 8:
         variable9 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable9)
        elif posicion == 9:
         variable10 = list_futuros_usuarios[posicion].id + list_futuros_usuarios[posicion].nombre + list_futuros_usuarios[posicion].contraseña
         print(variable10) 
         
        posicion += 1 #Suma para ubicar posisciones en lista y para condiciones (para almacenar en variables)
print("***Lista Usuario con Contraseñas asignadas al azar***") 
imprimir_productos_contraseña() 

#Fin de La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.

#Por cada cuenta debe pedir un número telefónico para contactarse.
def tiene_longitud_suficiente(fono):
    return len(fono)==8 

def tiene_numero(fono):
    # return any(c.isdigit() for c in fono) "(esta opcion consulta por digitos en el valor se deja para proyectos posteriores)""
      return fono.isnumeric()# Consulta si es un valor numerico
# evaua criterios solicitados (criterios: mayúsculas, minúsculas y números)
def evaluar_criterios(fono):
    criterios = {
        "longitud insuficiente(Se necesita 8 digitos)": tiene_longitud_suficiente,
         "Los caracteres deben ser numerico": tiene_numero,
    }
    faltantes = []
    
    for descripcion, funcion in criterios.items():
        if not funcion(fono):
            faltantes.append(descripcion)
    return faltantes

def main():
    print("El numero telefónico debe tener 8 dígitos")
    fono = ""
    for usuarios in list_futuros_usuarios:
          while True:
             nombre_usuario=usuarios.nombre
             print("Usuario: ", nombre_usuario)
             char = input("Ingrese un numero de telefono :")
             fono = char
             criterios_faltantes = evaluar_criterios(fono)
      
             if not criterios_faltantes:
              print("!Excelente! tu numero telefónico cumple con los requisitos y ha sido ingresado con exito!")
              usuarios.telefono=fono
              break
             else:
              print(f"Criterios faltantes para numero telefónico: {', '.join(criterios_faltantes)}")
    print("***Lista de Usuarios - Telefonos***")      
    imprimir_usuario_telefono()

if __name__ == "__main__":
    main()
   