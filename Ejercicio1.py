#1- Crea una funció que donat un string i una lletra, ens digui si la lletra està dins l’string.
palabra = input("Dime una palabra: ")
letra = input("Dime que letra quieres buscar: ")

if letra in palabra:
    print(True)
else:
    print(False)