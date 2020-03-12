class List:
    def __init__(self):
        self.head = None

    def print(self):
        begin = self.head
        while begin is not None:
            print(begin.val, end=' ')
            begin = begin.next

    def append(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head

        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode

    def findKthFromEnd(self, n):
        lastNode = self.head
        primNode = self.head

        k = 0

        while lastNode is not None:
            k += 1
            lastNode = lastNode.next

        lastNode = primNode
        i = 0
        while i != (k - n):
            i += 1
            lastNode = lastNode.next

        return lastNode

    def merge(l1, l2):

        lastNode_1 = l1.head
        lastNode_2 = l2.head

        mergedList = [] #lista goala pentru a returna o lista

        while lastNode_1 is not None and lastNode_1 is not None:
            if lastNode_1 is None or lastNode_2 is None: #daca ajungem la ultimul element din una din liste
                break   #iesim din while

            if lastNode_1.val < lastNode_2.val: #testam un element din l2 daca e > din l1
                mergedList.append(lastNode_1.val) #atunci il aruncam in lista creata
                lastNode_1 = lastNode_1.next #trecem la urmatorul element din l1

            else:
                mergedList.append(lastNode_2.val)
                lastNode_2 = lastNode_2.next

        while lastNode_1 is not None: #aruncam toate elemente ramase din l1 in lista creata
            mergedList.append(lastNode_1.val)
            lastNode_1 = lastNode_1.next

        return mergedList   #returnam lista

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
