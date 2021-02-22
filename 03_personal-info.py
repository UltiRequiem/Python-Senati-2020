def run():
    espacio = " "
    punto = "."

    nombre = input("Cuàl es tu nombre: ")
    apellido = input("Cuàl es tu apellido: ")
    ubicacion = input("Cuàl es tu ubicacion: ")

    print("Hola " + nombre + espacio + apellido + punto + '¿Como estas en ' + ubicacion + '?')

if __name__ == '__main__':
    run()
