from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.pilha.Node import Node

class Stack():
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elemento):
        # Inserir elemento na pilha
        node = Node(elemento)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        # Remover elemento que está no topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            return None

    def peek(self):
        # Retorna o topo da pilha para observação
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia")

    def isEmpty(self):
        # Verifica se a pilha está vazia
        return self._size == 0

    def __len__(self):
        # Retorna o tamanho da pilha
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r += str(pointer.data) + '<-'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
