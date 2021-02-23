def run():
    nota1 = input("Ingresa tu nota: ")
    nota1 = float(nota1)
    if nota1 >= 14:
        print("Aprobaste el curso")
    elif nota1 < 14 and nota1 > 10:
        print("Vas al sustitutorio.")
    elif nota1 > 20:
        print('La maxima nota es 20.')
    else:
        print("Estas jalado.")

        
if __name__ == '__main__':
    run()