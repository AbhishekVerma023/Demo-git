class Node(object):
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # inserting the node at the beginning
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # inserting at the end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         
            temp = temp.next
        temp.next = newNode
        
    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next
​
                # node not found
                if temp == None:
                    return
​
                prev.next = temp.next
                return
​
    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)
