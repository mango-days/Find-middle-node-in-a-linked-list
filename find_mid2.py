# Find the middle of a given linked list

# Given a singly linked list, find the middle of the linked list. For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 

# If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4.

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )
    
    def size ( self ) :
        temp = self.head
        n = 0
        while ( temp ) :
            n += 1
            temp = temp.next
        return n
    
    def midElement ( self ) :
        temp = self.head
        half_length = self.head
        while ( temp ) :
            if temp.next != None :
                temp = temp.next.next
                half_length = half_length.next
            else : break
        print ( half_length.data )

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 3 )
llist.add ( 4 )
llist.add ( 5 )
llist.midElement()