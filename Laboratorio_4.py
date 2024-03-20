#Clase Nodo simple
class Node:
    def __init__(self, data, next, e):
        self.data = e
        self.next = None
    def getData(self):
        return self.data
    def setData(self, e):
        self.data = e
    def getNext(self):
        return self.next
    def setNext(self, n):
        self.next = n
#Clase lista simple
class List:
    def __init__(self, head, tail, size):
        self.head = None
        self.tail = None
        self.size = 0
    def size(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def setSize(self, s):
        self.size = s
    def First(self):
        return self.head
    def Last(self):
        return self.tail
    def addFirst(self, e):
        n = Node(e)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self.size += 1
    def addLast(self, e):
        n = Node(e)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self.size += 1
    def removeFirst(self):
        if not self.isEmpty():
            temp = self.head
            self.head = temp.getNext()
            temp.setNext(None)
            self.size -= 1
            return temp.getData()
        else:
            return None
    def removeLast(self):
        if self.size==1:
            return self.removeFirst()
        else:
            temp = self.tail
            anterior = self.head
            while anterior.getNext() !=self.tail:
                anterior = anterior.getNext()
            anterior.setNext(None)
            self.tail = anterior
            self.size -= 1
            return temp.getData()

#Clase nodo doble
class DoubleNode:
    def __init__(self, data, next, prev, d):
        self.data = d
        self.next = None
        self.prev = None
    def setData(self, d):
        self.data = d
    def setNext(self, n):
        self.next = n
    def setPrev(self, p):
        self.prev = p
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev

#Clase lista doble
class DoubleList:
    def __init__(self, head, tail, size):
        self.head = None
        self.tail = None
        self.size = 0
    def size(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def First(self):
        return self.head
    def Last(self):
        return self.tail
    def addFirst(self, e):
        n = DoubleNode(e)
        if self.isEmpty(self):
            self.head = n
            self.tail = n
        else:
            n.setNext(self.head)
            self.head.setPrev(n)
            self.head = n
        self.size += 1
    def addLast(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.setNext(n)
            n.setPrev(self.tail)
            self.tail = n
        self.size += 1
    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = temp.getNext()
            temp.setNext(None)
            self.head.setPrev(None)
            self.size -= 1
            return temp.getData()
    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp = self.tail
            tail = temp.getPrev()
            tail.setNext(None)
            temp.setPrev(None)
            self.size -= 1
            return temp.getData()
    def remove(self, n):
        if n==self.head:
            return self.removeFirst()
        elif n==self.tail:
            return self.removeLast()
        else:
            e = n.getData()
            p = n.getPrev()
            nx = n.getNext()
            p.setNext(nx)
            nx.setPrev(p)
            n.setNext(None)
            n.setPrev(None)
            self.size -= 1
            return e
    def addBefore(self, n, e):
        if n == self.head:
            self.addFirst(e)
        else:
            m = DoubleNode(e)
            p = n.getPrev()
            p.setNext(m)
            m.setPrev(p)
            m.setNext(n)
            n.setPrev(m)
            self.size += 1
    def addAfter(self, n, e):
        if n == self.tail:
            self.addLast(e)
        else:
            m = DoubleNode(e)
            nx = n.getNext()
            n.setNext(m)
            m.setPrev(n)
            m.setNext(nx)
            nx.setPrev(m)
            self.size += 1