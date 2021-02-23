def run():
  x = input("Ingrese un numero para contar: ")
  x = int(x)
  y = 1
  while y <= x:
    print(y)
    y = y+1

if __name__ == '__main__':
  run()