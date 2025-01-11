# Anderson S M Machado

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = DNode(data)
    
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

Lista = DoublyLinkedList(5)
Lista.inseriNoInicio(2)
Lista.inseriNoFim(10)
Lista.inseriNoFim(11)
Lista.deletar_pos(3)
Lista.exibirElementosFrente()
Lista.exibirElementosVerso()