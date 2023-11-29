#Crea un programa que donada una llista d’enters i un número n, ens digui si la suma d’elements d’aquella llista és igual a aquell número n.
lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8]

numero = int(input("Dime un numero: "))
if sum(lista_enteros) == numero:
    print("La suma d’elements de la llista és igual a el teu número")
else: 
    print("La suma d’elements de la llista no és igual a el teu número")