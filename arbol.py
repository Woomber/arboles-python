"""
Clases Nodo y Árbol
Yael Chavoya
"""
from typing import List, Tuple


class Nodo:
    """
    Clase Nodo
    """

    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo: Nodo or None = None
        self.derecho: Nodo or None = None

    def __str__(self):
        return f'Nodo({self.valor})'

    def es_hoja(self):
        """
        Determina si el nodo es un nodo hoja

        :return: True si es un nodo hoja
        """
        return not self.izquierdo and not self.derecho


class Arbol:
    """
    Clase Árbol, representa un árbol binario de búsqueda
    """

    def __init__(self, raiz: Nodo = None):
        self.raiz: Nodo or None = raiz

    def insertar(self, valor: int) -> bool:
        """
        Inserta un nodo con el valor especificado al árbol

        :param valor: El valor del nodo a insertar
        :return: True si el valor se insertó
        """

        # Si el árbol está vacío, el nuevo nodo es la raíz
        if not self.raiz:
            self.raiz = Nodo(valor)
            return True

        padre: Nodo or None = None
        actual: Nodo or None = self.raiz

        # Buscar la posición donde insertar el nuevo nodo
        while actual:
            # Si ya existe, no insertar
            if actual.valor == valor:
                return False

            # Navegar por el árbol según los valores de los nodos
            padre = actual
            if valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        if not padre:
            return False

        actual = Nodo(valor)

        # Insertar el nodo en la posición correcta
        if valor < padre.valor:
            padre.izquierdo = actual
        else:
            padre.derecho = actual

        return True

    @staticmethod
    def _eliminar_hoja(nodo: Nodo, padre: Nodo or None):
        """
        Función auxiliar para el método eliminar, elimina un nodo hoja del árbol

        :param nodo: El nodo hoja a eliminar
        :param padre: El padre de nodo
        """

        if padre:
            if padre.derecho == nodo:
                padre.derecho = None
            elif padre.izquierdo == nodo:
                padre.izquierdo = None

    @staticmethod
    def _eliminar_interno(nodo: Nodo) -> Tuple[Nodo, Nodo]:
        """
        Función auxiliar para el método eliminar, elimina un nodo interno del árbol.
        Intercambia el valor del nodo a eliminar por el de otro nodo más fácil de eliminar

        :param nodo: El nodo interno a eliminar
        :return: una tupla con el siguiente nodo a eliminar y su respectivo padre
        """

        padre: Nodo = nodo
        aux_nodo: Nodo
        aux_valor: int

        # Buscar el menor nodo del subárbol derecho
        if nodo.derecho:
            aux_nodo = nodo.derecho
            while aux_nodo.izquierdo:
                padre = aux_nodo
                aux_nodo = aux_nodo.izquierdo

        # Si no tiene subárbol derecho, buscar el mayor nodo del subárbol izquierdo
        else:
            aux_nodo = nodo.izquierdo
            while aux_nodo.derecho:
                padre = aux_nodo
                aux_nodo = aux_nodo.derecho

        # Intercambiar los valores del nodo a eliminar y del nodo encontrado
        aux_valor = nodo.valor
        nodo.valor = aux_nodo.valor
        aux_nodo.valor = aux_valor

        return aux_nodo, padre

    def eliminar(self, valor: int) -> bool:
        """
        Elimina un nodo con el valor especificado del árbol

        :param valor: El valor del nodo a eliminar
        :return: Verdadero si se eliminó un nodo
        """

        if not self.raiz:
            return False

        if self.raiz.valor == valor and self.raiz.es_hoja():
            self.raiz = None
            return True

        padre: Nodo or None = None
        actual: Nodo or None = self.raiz

        # Repetir hasta que se elimine el nodo o no se encuentre
        while actual:
            # Si el nodo se encuentra
            if actual.valor == valor:
                if actual.es_hoja():
                    # Eliminar el nodo hoja y finalizar el proceso
                    self._eliminar_hoja(actual, padre)
                    actual = None
                else:
                    # Intercambiar el nodo por otro para facilitar su eliminación como hoja
                    actual, padre = self._eliminar_interno(actual)
            else:
                # Continuar buscando
                padre = actual
                if valor < actual.valor:
                    actual = actual.izquierdo
                else:
                    actual = actual.derecho

        return True

    def buscar(self, valor: int):
        """
        Busca si un valor determinado existe en el árbol

        :param valor: El valor a buscar
        :return: True si el valor fue encontrado
        """

        actual: Nodo or None = self.raiz

        # Repetir hasta que no quede nada más qué buscar
        while actual:
            if actual.valor == valor:
                # Se encontró
                return True
            if valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        # No se encontró
        return False

    def pre_orden(self) -> List[Nodo]:
        """
        Crear una lista con los nodos ordenados de acuerdo al recorrido pre orden

        :return: Una lista de nodos en pre orden
        """

        # Lista con los nodos en pre orden
        orden: List[Nodo] = []

        # Pila LIFO para navegar iterativamente en pre orden
        stack: List[Nodo] = []

        if not self.raiz:
            return orden

        # Empezar con la raíz
        stack.append(self.raiz)

        # Mientras aún queden elementos por procesar
        while len(stack) > 0:
            # Agregar a la lista el último elemento de la pila
            item = stack.pop()
            orden.append(item)

            # Agregar sus hijos a la pila en orden inverso a como se analizarán
            if item.derecho:
                stack.append(item.derecho)
            if item.izquierdo:
                stack.append(item.izquierdo)

        return orden

    def _altura(self, nodo: Nodo) -> int:
        """
        Función auxiliar de altura. Calcula recursivamente la altura de un subárbol

        :param nodo: El nodo raíz del subárbol del que se calcula su altura
        :return: La altura del nodo, calculada recursivamente
        """

        if not nodo:
            return 0

        # Retornar la altura mayor de sus subárboles más uno
        return max(self._altura(nodo.izquierdo), self._altura(nodo.derecho)) + 1

    def altura(self) -> int:
        """
        Calcula la altura del árbol, auxiliándose de _altura, empezando por la raíz

        :return: La altura del árbol
        """
        return self._altura(self.raiz)

    def num_nodos(self):
        """
        Obtiene el número de nodos en el árbol

        :return: EL número de nodos
        """
        return len(self.pre_orden())

    def nodos_hoja(self) -> List[Nodo]:
        """
        Obtiene los nodos hoja en el árbol

        :return: Una lista con los nodos hoja
        """

        # Lista por comprensión de items en la lista de preorden que son nodos hoja
        return [item for item in self.pre_orden() if item.es_hoja()]

    def num_nodos_hoja(self) -> int:
        """
         Obtiene el número de nodos hoja en el árbol

        :return: El número de nodos hoja
        """
        return len(self.nodos_hoja())

    def menor(self) -> Nodo or None:
        """
        Obtiene el nodo con el valor más pequeño del árbol

        :return: El nodo menor
        """

        if not self.raiz:
            return None

        actual: Nodo or None = self.raiz

        # Como para cada nodo su hijo izquierdo siempre es menor, buscar el elemento más a la izquierda
        while actual.izquierdo:
            actual = actual.izquierdo

        return actual

    def mayor(self) -> Nodo or None:
        """
        Obtiene el nodo con el valor más grande del árbol

        :return: El nodo mayor
        """

        if not self.raiz:
            return None

        actual: Nodo or None = self.raiz

        # Como para cada nodo su hijo derecho siempre es mayor, buscar el elemento más a la derecha
        while actual.derecho:
            actual = actual.derecho

        return actual
