# Anderson S M Machado

class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None    


class LinkedList:
    def __init__(self, head):
        self.head=Node(head)

    def IndiceDe(self, value):
        lIdx = -1
        current = self.head
        while current is not None:
            lIdx+=1
            if current.data==value:
                return lIdx
            current = current.next
        return -1
    
    def inverterLista(self):
        saida = LinkedList(self.head.data)
        lIdx = -1
        current = self.head
        while current is not None:
            lIdx+=1
            if lIdx>0:
                saida.insere_no_inicio(current.data)
            current = current.next
        return saida
    
    def exibirElementos(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    
    def insere_no_inicio(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insere_no_fim(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head=new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def deletar_na_posicao(self, position):
        if self.head is None or position < 1:
            return False

        if position == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
            return True

        current = self.head
        for i in range(1, position - 1):
            if current is not None:
                current = current.next

        if current is None or current.next is None:
            return False

        temp = current.next
        current.next = current.next.next

        temp = None
        return True

Lista =  LinkedList(10)
Lista.insere_no_inicio(5)
Lista.insere_no_fim(15)
Lista.insere_no_fim(16)
Lista.deletar_na_posicao(2)
print("Exibindo lista: ")
Lista.exibirElementos()
print("O elemento 16 está na posição: "+str(Lista.IndiceDe(16)))
ListaInvertida = Lista.inverterLista()
print("Exibindo lista invertida: ")
ListaInvertida.exibirElementos()