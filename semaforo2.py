import os

SEMAFORO = []

ROJO = 1
AMARILLO = 2
VERDE = 3


def imprimir_menu ():
    os.system('cls')
    print(f'''           ~~~~~~SEMAFORO~~~~~
{ROJO}) ROJO
{AMARILLO}) AMARILLO
{VERDE}) VERDE''')  

def mostrar_rojo():
    print('\U0001F6D1')
    print('ALTO..¡¡DETENGA AHORA SU MARCHA...¡¡')
    print('Peatones pueden cruzar la via.')
    
def mostrar_amarillo():
    print('\U0001F7E1')
    print('Luz de precaucion de movimiento')
    

def mostrar_verde():
    print('\U0001F7E2')
    print('AVANCE...VIAJE CON CUIDADO...')
    print('Gracias por su respeto')
    print('\U0001F6A5')
       

def main():
    continuar = "true"
    while continuar:

        imprimir_menu()

        opc = int (input('Selecciona una opcion: '))
        os.system ('cls')
        if opc == ROJO:
            mostrar_rojo()
        elif opc == AMARILLO:
            mostrar_amarillo()
        elif opc == VERDE: 
            mostrar_verde()
            continuar = True
        else:
            print('Gracias')
            input('Presiona enter para continuar...')
        
            
        input('presiona enter para continuar...por favor...')

if __name__ == '__main__':
    main()

