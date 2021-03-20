def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuantos " + tipo_pesos + " tienes?: "))
    dolares = str(round(pesos / valor_dolar, 2))
    print("Tienes $" + dolares + " dolares")


menu = """
======= Conversor de monedas =======
Seleccione una opción
1. Convertir de Bolivianos a Dolares
2. Convertir de pesos Mexicanos a Dolares
3. Convertir de Dolares a Bolivianos
"""
print(menu)
entrada = int(input("opcion: "))

if (entrada == 1):
    conversor("Bolivianos", 6.98)
elif (entrada == 2):
    conversor("Pesos Mexicanos", 24)
elif (entrada == 3):
    dolares = float(input("¿Cuantos Dolares tienes?: "))
    valor_Boliviano = 6.98
    bolvianos = str(round(dolares * valor_Boliviano, 2))
    print("Tienes $" + bolvianos + " bolvianos")
