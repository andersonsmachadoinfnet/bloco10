# Anderson S M Machado

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = DNode(data)

    def quantidadeItens(self):
        i = -1
        curr = self.head
        while curr is not None:
            i += 1
            curr = curr.next
        return i+1
    
    def ordernar(self):
        for i in range(self.quantidadeItens()):
            curr = self.head
            while curr is not None:
                prox = curr.next
                if prox is not None and (curr.data>prox.data):
                    curr.data, prox.data = prox.data, curr.data
                curr = prox

    def exibirElementosFrente(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print("")

    def exibirElementosVerso(self):
        curr = self.head
        while curr is not None:
            if curr.next==None:
                break
            curr = curr.next
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.prev
        print()
    
    def inserirLista(self, lista):
        curr = lista.head
        while curr is not None:
            self.inseriNoFim(curr.data)
            curr = curr.next
        self.ordernar()    

    def inseriNoInicio(self, data):
        new_node = DNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head=new_node;

    def inseriNoFim(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
        
            curr.next = new_node
            new_node.prev = curr
    
    def deletar_pos(self, pos):
        if self.head is None:
            return False
        curr = self.head
        for i in range(1, pos):
            if curr is None:
                return False
            curr = curr.next
        if curr is None:
            return False
        if curr.prev is not None:
            curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        if self.head == curr:
            self.head = curr.next

Lista = DoublyLinkedList(6)
Lista.inseriNoInicio(7)
Lista.inseriNoFim(8)
Lista.inseriNoFim(5)
print("Lista A: ")
Lista.exibirElementosFrente()
Lista.ordernar()
print("Lista A ordenada: ")
Lista.exibirElementosFrente()

ListaB = DoublyLinkedList(3)
ListaB.inseriNoInicio(4)
ListaB.inseriNoFim(2)
ListaB.inseriNoFim(1)
print("Lista B: ")
ListaB.exibirElementosFrente()

Lista.inserirLista(ListaB)
print("Lista A+B ordenada: ")
Lista.exibirElementosFrente()