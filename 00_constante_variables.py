def run():
    # Son constantes 
    pi = 3.1416
    print('El valor de pi es: ' + str(pi) + '\n')
    nombre = "Eliaz"
    print('Mi nombre es ' + nombre + '\n')

    # Son variables numèricas
    c = 24
    print('El valor de C es '+str(c))
    print('C es de tipo ' + str(type(c)) + '\n')

    c = c + 10.5
    print('Al sumarle 10.5 ahora C vale: ' + str(c))
    print('Ahora C es de tipo ' + str(type(c)) + '\n')

    c = c + pi
    print('Al sumarle pi ahora C vale: ' + str(c))
    print('Ahora C es de tipo ' + str(type(c)) + '\n')

    c = c + 4j
    print('Al sumarle 4j ahora C vale: ' + str(c))
    print('Ahora C es de tipo ' + str(type(c)) + '\n')


    apellidos = "Bobadilla Camarena"
    print('Acabo de definir una variable "apellidos" con el string:' + apellidos)
    apellidos = nombre + " Bobadilla Camarena"
    print('Ahora he sumado la variable "nombre" con la variable "apellidos" :' + apellidos)
    print('Es de tipo' + str(type(apellidos)) + '\n')

    # Son variables booleanas
    estado = True
    print('Acabo de definir unar variable "estado" con el valor booleano de: ' + str(estado))
    print('Es de tipo' + str(type(estado)) + '\n')


    print("""No se puede poner como nombre de variable a las siguientes palabras reservadas:
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'] """)

if __name__ == '__main__':
    run()
