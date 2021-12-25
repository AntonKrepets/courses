class Stack:

    def __init__(self):
        self.__elements = []
    
    def __iter__(self):
        self.__elem = 0
        return self

    def push(self, elements):
        self.__elements.append(elements)

    def __next__(self):
         if len(self.__elements) > 0:
             return self.pop()
         else:
             raise StopIteration
    
    def get_elements(self):
        return self.__elements
    
    def pop(self):
        if len(self.__elements) < 1:
            return None
        else:
            return self.__elements.pop()
    
    def peek(self):
        return self.__elements[(len(self.__elements)) - 1]
    
    def size(self):
        return f'size is {len(self.__elements)}'

    

class Queue:

    def __init__(self):
        self.__elements = []
    
    def __iter__(self):
        self.__elem = 0
        return self
    
    def push(self, elements):
        self.__elements.append(elements)
    
    def get_elements(self):
        return self.__elements
    
    def __next__(self):
         if len(self.__elements) > 0:
             return self.pop()
         else:
             raise StopIteration
    
    def size(self):
        return f'size is {len(self.__elements)}'
    
    def pop(self):
        if len(self.__elements) == 0:
            return None
        else:
            return self.__elements.pop(0)



if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(2)
    s.push(1)
    for i in s:
        print(i)


    q = Queue()
    q.push(5)
    q.push(3)
    q.push(2)
    q.push(1)
    for i in q:
        print(i)

    



                


