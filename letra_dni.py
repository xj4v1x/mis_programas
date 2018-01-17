"""
Programa para calcular la letra del DNI
"""

numeros = "0123456789"
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
exit = False

while exit == False:
    dni = input("Introduce el número de DNI (sin letra): ")
    if len(dni) < 8:
        print("Faltan números")
    else:
        exit = True
        for i in dni:
            if i not in numeros:
                print ("Sólo números")
                exit = False

dni = int(dni)
codigo_letra = dni%23


print("El DNI es : {}-{}".format(dni, letras[codigo_letra]))