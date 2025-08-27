"""
This class is used to create a new node. It has 7 functions.
"""
class DoublyLinkedListNode:
    
    def __init__(self, data):
        '''
        This function create a new node and assigns data into it. The previous and next of this node is assigned None.
        Inputs:
            -self: refers to the instance of class.
            -data (str): The newly created node is assigned this data.
        Output: NA
        '''
        self.data = data
        self.previous = None
        self.next = None

    def getData(self):
        '''
        This function is to retrive data from a node.
        Inputs:
            -self: refers to the instance of class
        Output:
            -data (str): The data is retrived from the node. 
        '''
        return self.data

    def setData(self, newData):
        '''
        This function is to assign a data to a node. 
        Inputs:
            -self: refers to the instance of class
            -newData (str): The data is assigned to the node.
        Output: NA
        '''
        self.data = newData

    def getNext(self):
        '''
        This function is move to the next node. 
        Inputs:
            -self: refers to the instance of class
        Output:
            -self.next: refers to the instance of class of next node.
        '''
        return self.next

    def getPrevious(self):
        '''
        This function is to move to the previous node.
        Inputs:
            -self: refers to the instance of class
        Output:
            -self.previous: refers to the instance of class of previous node.
        '''
        return self.previous

    def setNext(self, newNext):
        '''
        This function is to set data to the next node.
        Inputs:
            -self: refers to the instance of class
            -newNext (str): The data that is to be assigned to the next node.
        Output: NA
        '''
        self.next = newNext

    def setPrevious(self, newPrevious):
        '''
        This function is to set data to the previous node.
        Inputs:
            -self: refers to the instance of class
            -newPrevious (str): The data that is to be assigned to the previous node.
        Output: NA
        '''
        self.previous = newPrevious

"""
This class is used to perform operations on a Circular Doubly Linked List and has 13 functions.
"""
class CircularDoublyLinkedList:
    def __init__(self, capacity):
        '''
        This function initialises all the pointers when a circular linked is created.
        Inputs:
            -self: refers to the instance of class.
            -capacity (int): The maximum size of the circular linked list.
        Output: NA
        '''
        self.head = None
        self.current = None
        self.capacity=capacity
        self.size = 0
        
    def get_size(self):
        '''
        This function is set data to the next node.
        Inputs:
            -self: refers to the instance of class
        Output:
            -size (int): Returns the size of the circular linked list
        '''
        return self.size
    
    def is_empty(self):
        '''
        This function checks if the Circular Linked list is empty or not.
        Inputs:
            -self: refers to the instance of class
        Output:
            -(bool): True if empty/ False is not empty
        '''
        return self.size==0

    def is_full(self):
        '''
        This function checks if the Circular Linked list is full or not.
        Inputs:
            -self: refers to the instance of class
        Output:
            -(bool): True if full/ False is not full
        '''
        return self.size == self.capacity
    
    def add_at_beginning(self, data):
        '''
        This function is used to add a node to the beggining of the circular linked list.
        Inputs:
            -self: refers to the instance of class
            -data (str): the data that is to be added at the beginning.
        Output:NA
        '''
        if self.is_full():
            raise Exception("Carousel if full. It has reached its maximum capacity")    #If the circular linked list is full, raise an exception   
        else:
            new_node = DoublyLinkedListNode(data)                                       #Creating a new node with the given data                              
            if not self.head:                                                           #Add the new node at the beginning, as the circular linked list was empty                                                  
                self.head = new_node
                self.head.setNext(self.head)
                self.head.setPrevious(self.head)
                self.current = self.head
            else:
                new_node.setNext(self.head)                                             #If the list is not empty, it inserts the new node to the left of the current head node.                           
                new_node.setPrevious(self.head.getPrevious())
                self.head.previous.setNext(new_node)
                self.head.setPrevious(new_node)
                self.head = new_node
                self.current = new_node
            self.size += 1                                                              #Incrementing the size of the circular linked list

    def add_left(self, data):
        '''
        This function is used to add a node to the left of current node.
        Inputs:
            -self: refers to the instance of class
            -data (str): the data that is to be added to the right.
        Output:NA
        '''
        if self.is_full():
            raise Exception("Carousel if full. It has reached its maximum capacity")    #If the circular linked list is full, raise an exception
        else:
            
            new_node = DoublyLinkedListNode(data)                                       #Creating a new node with the given data                                           
            if not self.current:                                                        #Add the new node at the beginning, as the circular linked list was empty
                self.add_at_beginning(data)
            else:
                new_node.setPrevious(self.current.getPrevious())                        #Inserting the new node to the left of the current node
                new_node.setNext(self.current)
                self.current.previous.setNext(new_node)
                self.current.setPrevious(new_node)
                self.current = new_node
                self.size += 1                                                          #Incrementing the size of the circular linked list

    def add_right(self, data):
        '''
        This function is used to add a node to the right of current node.
        Inputs:
            -self: refers to the instance of class
            -data (str): the data that is to be added to the right.
        Output:NA
        '''
        if self.is_full():
            raise Exception("Carousel if full. It has reached its maximum capacity")     #If the circular linked list is full, raise an exception
        
        else:
            new_node = DoublyLinkedListNode(data)                                        #Creating a new node with the given data
            if not self.current:                                                         #Add the new node at the beginning, as the circular linked list was empty
                self.add_at_beginning(data)
            else:
                new_node.setNext(self.current.getNext())                                 #Inserting the new node to the right of the current node
                new_node.setPrevious(self.current)
                self.current.next.setPrevious(new_node)
                self.current.setNext(new_node)
                self.current = new_node
                self.size += 1                                                           #Incrementing the size of the circular linked list

    def remove_current(self):
        '''
        This function is used to delete the current node. 
        Inputs:
            -self: refers to the instance of class
        Output:NA
        '''
        if self.is_empty():                                                              #raise exception when circular linked list is empty
            raise Exception("Carousel is empty")
        else:
            if self.size == 1:                                                           #If there is only one node in the list
                self.head = None
                self.current = None
            else:
                self.current.previous.setNext(self.current.getNext())                    #Adjusting pointers to skip the current node
                self.current.next.setPrevious(self.current.getPrevious())
                if self.head == self.current:                                            #Updating head pointer, if necessary
                    self.head = self.current.getPrevious()
                self.current = self.current.getPrevious()                                #Moving current pointer to the previous node                 
            self.size -= 1                                                               #Decreasing the size of the circular linked list

    def go_left(self):
        '''
        This function sets previous node as the current node if a node exists else, it raises exception. The circular linked list moves left.
        Inputs:
            -self: refers to the instance of class
        Output:NA
        '''
        if self.is_empty():                                                              #raise exception when circular linked list is empty
            raise Exception("Carousel is empty")
        else:
            self.current = self.current.getPrevious()                                    #Sets previous node as the current node                   
        
    def go_right(self):
        '''
        This function sets next node as the current node if a node exists else, it raises exception. The circular linked list moves right.
        Inputs:
            -self: refers to the instance of class
        Output:NA
        '''
        if self.is_empty():                                                              #raise exception when circular linked list is empty
            raise Exception("Carousel is empty")
        else:
            self.current = self.current.getNext()                                        #Sets next node as the current node                  
                    
    def get_current(self):
        '''
        This function returns the data of the current node if a node exists else, it raises exception.
        Inputs:
            -self: refers to the instance of class
        Output:
            -data (str): The data of the current node is retrived, if current node exist.
        '''
        if self.is_empty():                                                              #raise exception when circular linked list is empty
            raise Exception("Carousel is empty")
        else:
            return self.current.data                                                     #The data of the current node is retrived                                             
       
    def get_next_node(self):
        '''
        This function returns the data of the next node from crrent node if a node exists else, it raises exception.
        Inputs:
            -self: refers to the instance of class
        Output:
            -data (str): The data of the next node from crrent node is retrived, if current node exist.
        '''
        if self.is_empty():                                                              #raise exception when circular linked list is empty
            raise Exception("Carousel is empty")
        else:
            return self.current.getNext()                                                #The data of the next node from crrent node is retrived
       
    def get_previous_node(self):
        '''
        This function returns the data of the previous node from current node if a node exists else, it raises exception.
        Inputs:
            -self: refers to the instance of class
        Output:
            -data (str): The data of the previous node from crrent node is retrived, if current node exist.
        '''
        if self.is_empty():                                                              #raise exception when circular linked list is empty
            raise Exception("Carousel is empty")                                         #The data of the previous node from crrent node is retrived
        else:
            return self.current.getPrevious()

# Example Testing:
if __name__ == "__main__":
    cll = CircularDoublyLinkedList(5)
    cll.add_at_beginning(1)
    cll.add_right(2)
    print(cll.get_current())  # Output: 2
    print(cll.get_next_node().data)  # Output: 1
    print(cll.get_previous_node().data)  # Output: 1
    cll.add_right(3)
    cll.add_left(0)
    print(cll.get_current())  # Output: 0
    print(cll.get_next_node().data)  # Output: 1
    print(cll.get_previous_node().data)  # Output: 3
    cll.go_right()
    print(cll.get_current())  # Output: 1
    cll.remove_current()
    print(cll.get_current())  # Output: 2
    cll.go_right()
    print(cll.get_current())  # Output: 3
    cll.go_right()
    print(cll.get_current())  # Output: 0
    print('size',cll.get_size())
