"""
    python3 calculo_iva.py
"""
import os

def handling_input(value, value_type):
    try:
        entrada = value_type(value)
    except:
        entrada = None
    return entrada

def on_message(value):
    os.system('clear')
    print(value)

def calculo_iva():
    while True:
        print("""\n#############################################\n# Sistema para calcular un precio + el IVA. #\n#############################################\n""")
        print('Escriba el número de la acción a realizar.\n1 Calcular IVA.\n2 Salir.\n')
        options = handling_input(input('Ingrese una opción: '), int)
        if options == 2:
            on_message('\nHasta luego :)\nMade by Alex Cernik.\n')
            break
        elif options == 1:
            while True:
                price = handling_input(input('\nIngrese el precio a calcular: '), float)
                if not price or price <= 0:
                    on_message('\nERROR: Ingrese solo números positivos y use el punto como separador decimal de ser necesario.')
                else:
                    while True:
                        print('\nSeleccione el tipo de IVA.\n1 IVA 21%.\n2 IVA 10,5%.\n3 Salir.')
                        iva = handling_input(input('\nIngrese una opción de IVA: '), int)
                        if not iva or iva <= 0:
                            on_message('\nERROR: La opción ingresada no corresponde a ninguna de las anteriores.')
                        if iva == 1:
                            on_message(f'\nEl precio ${price:.2f} + 21% de IVA es: {price + 21 * price / 100:.2f}\n')
                            break
                        elif iva == 2:
                            on_message(f'\nEl precio ${price:.2f} + 10,5% de IVA es: ${price + 10.5 * price / 100:.2f}\n')
                            break
                        elif iva == 3:
                            on_message('\nHasta luego :)\nMade by Alex Cernik.\n')
                            break
                    break
        else:
            on_message('\nERROR: La opción ingresada no corresponde a ninguna de las anteriores.\n')
calculo_iva()
