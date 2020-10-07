"""
Interfaz de comandos
Yael Chavoya
"""
from arbol import Arbol
import gui


def _clear_screen():
    """
    Colocar espaciado entre menú y menú
    """
    print('\n'*3)


def _wait_enter():
    """
    Esperar a que el usuario presione ENTER
    """
    input('Presione ENTER para continuar...')
    _clear_screen()


def _tiene_nodos(arbol: Arbol):
    if arbol.num_nodos() == 0:
        print('No hay nodos en el árbol')
        _wait_enter()
        return False
    return True


def _agregar_nodo(arbol: Arbol):
    """
    Agregar un nodo al árbol

    :param arbol: El árbol donde se agregará el nodo
    """
    while True:
        num = input('Ingrese un número a insertar (ENTER para cancelar): ')
        if len(num) == 0:
            _clear_screen()
            break
        try:
            num_int = int(num)
            if arbol.insertar(num_int):
                print(f'Nodo "{num}" agregado correctamente\n')
                _wait_enter()
                break
            else:
                print(f'El nodo "{num}" ya existe\n')
        except ValueError:
            print('Por favor ingrese un número entero')


def _cantidad_nodos(arbol: Arbol):
    """
    Ver la cantidad de nodos en el árbol

    :param arbol: El árbol
    """
    if not _tiene_nodos(arbol):
        return

    print(f'El árbol tiene {arbol.num_nodos()} nodos,')
    print(f'de los cuales {arbol.num_nodos_hoja()} son nodos hoja')
    _wait_enter()


def _pre_orden(arbol: Arbol):
    """
    Ver el recorrido pre orden del árbol

    :param arbol: El árbol
    """
    if not _tiene_nodos(arbol):
        return

    pre = [item.valor for item in arbol.pre_orden()]

    print(f'El recorrido pre orden del árbol es: {pre}')
    _wait_enter()


def _altura(arbol: Arbol):
    """
    Ver la altura del árbol

    :param arbol: El árbol
    """
    if not _tiene_nodos(arbol):
        return

    print(f'El árbol tiene altura {arbol.altura()}')
    _wait_enter()


def _mayor_valor(arbol: Arbol):
    """
    Ver el número mayor del árbol

    :param arbol: El árbol
    """
    if not _tiene_nodos(arbol):
        return

    print(f'El número mayor del árbol es {arbol.mayor().valor}')
    _wait_enter()


def _eliminar_nodo_menor(arbol: Arbol):
    """
    Eliminar el menor nodo del árbol

    :param arbol: El árbol donde se eliminará el nodo
    """
    if not _tiene_nodos(arbol):
        return

    menor = arbol.menor().valor
    arbol.eliminar(menor)

    print(f'El número {menor} fue eliminado')
    _wait_enter()


def _mostrar_arbol(arbol: Arbol):
    if arbol.num_nodos() < 2:
        print('Para visualizar el árbol necesita al menos 2 nodos')
    else:
        print('Mostrando en pyplot...')
        gui.visualizar_arbol(arbol)
    _wait_enter()


def main_menu():
    """
    Menú principal
    """

    arbol = Arbol()

    # datos ejemplo
    for item in [15, 7, 18, 12, 10, 5, 14, 25, 23]:
        arbol.insertar(item)

    entrada: str = ''

    while entrada != '0':
        print('====== Árboles binarios ======\nAutor: Yael Chavoya\n')
        print('Seleccione una opción:')
        print('1: Agregar número al árbol')
        print('2: Ver cantidad de nodos y nodos hoja')
        print('3: Ver nodos en pre orden')
        print('4: Ver altura del árbol')
        print('5: Ver número mayor')
        print('6: Eliminar número menor')
        print('7: Ver árbol')
        print('0: Salir')

        entrada = input('> ')
        print()

        if entrada == '0':
            break
        elif entrada == '1':
            _agregar_nodo(arbol)
        elif entrada == '2':
            _cantidad_nodos(arbol)
        elif entrada == '3':
            _pre_orden(arbol)
        elif entrada == '4':
            _altura(arbol)
        elif entrada == '5':
            _mayor_valor(arbol)
        elif entrada == '6':
            _eliminar_nodo_menor(arbol)
        elif entrada == '7':
            _mostrar_arbol(arbol)
        else:
            print('Opción no reconocida.')
            _wait_enter()
