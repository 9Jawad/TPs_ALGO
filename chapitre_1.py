##############################
##                          ##
##      Chapitre n°1        ##
##                          ##
##############################


################    CLASS NODE    ################ 

class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None
        self.previous = None
    
    def getData(self):  # lecture
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setData(self, newData): # écriture
        self.data = newData
        
    def setNext(self, newData):
        self.next = newData
    
    def setPrevious(self, newData):
        self.previous = newData
        
        
################    Stack    ################ 
# AVEC LIST

class StackV1:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        print()
        print(" Stack : ")
        print()
        for i in range(len(self.items)):
            index = len(self.items) - i -1   
            print( "|       |")
            print(f"|  {' ' if self.items[index] >= 0 else ''}{self.items[index]}   |")
            print( "|_______|")
        print()
        return str()


# AVEC LIST (sens différent)

class StackV2:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def top(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        print()
        print(" Stack : ")
        print()
        for i in range(len(self.items)):
            index = len(self.items) - i -1   
            print( "|       |")
            print(f"|  {' ' if self.items[index] >= 0 else ''}{self.items[index]}   |")
            print( "|_______|")
        print()
        return str()
    
    
 # AVEC CLASS NODE
    
class StackV3:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.n
    
    def top(self):
        return self.head.getData()
    
    def push(self, item):
        p = Node(item)
        p.setNext(self.head)
        self.head = p
        self.n += 1
    
    def pop(self):
        res = self.top()
        self.head = self.head.getNext()
        self.n -= 1
        return res


################    Heap    ################ 
# AVEC LIST

class HeapV1:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def insert(self, item):
        self.items.insert(0, item)
    
    def head(self):
        return self.items[-1]
    
    def remove(self):
        return self.items.pop()


# AVEC CLASS NODE

class HeapV2:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0
    
    def head(self):
        return self.first.getData()
    
    def size(self):
        return self.n
    
    def isEmpty(self):
        return self.first == None
    
    def insert(self, item):
        p = Node(item)
        if self.isEmpty():
            self.first = p
            self.last = p
        else:
            self.last.setNext(p)
            self.last = p
        self.n += 1
        
    def remove(self):
        res = self.head()
        self.first = self.first.getNext()
        self.n -= 1
        return res
    
    
################    PostFixe    ################ 

def postfixeEval(expression):
    stack = StackV1()
    list_token = expression.split()
    for token in list_token:
        if token in '0123456789':
            stack.push(int(token))
        elif token in '*/+-' and stack.size() >= 2:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            result = Math(token, operand_1, operand_2)
            stack.push(result)
        else:
            return NotImplemented
    return stack.pop()


def Math(token, operand_1, operand_2):
    if token == '*':
        return operand_1 * operand_2
    elif token == '/':
        return operand_1 / operand_2
    elif token == '+':
        return operand_1 + operand_2
    elif token == '-':
        return operand_1 - operand_2
        
        
################    Parenthésage Checker    ################ 

def parChecker(expression):
    stack = StackV1()
    i = 0
    res = True
    
    while i < len(expression) and res:
        token = expression[i]
        if token in '([{':
            stack.push(token)
        elif token in ')]}':
            if not stack.isEmpty():
                op = stack.pop()
                res = matches(op, token)
            else:
                res = False
        i += 1
        
    if stack.isEmpty() and res:
        return True
    else:
        return False
    
def matches(open, close):
    return '([{'.index(open) == ')]}'.index(close)


################    inFixe to postFixe    ################ 

import string

def infixToPostfix(infix):
    stack = StackV1()
    result = []
    prio = {}
    prio['*'] = 3
    prio['/'] = 3
    prio['+'] = 2
    prio['-'] = 2
    prio['('] = 1
    
    infix = infix.split()
    for token in infix:
        if token in string.lowercase or token in string.digits :
            result.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            topToken = stack.pop()
            while topToken != '(':
                result.apprend(topToken)
                topToken = stack.pop()
        else:
            while not stack.isEmpty() and prio[stack.top()] >= prio[token]:
                result.append(stack.pop())
            stack.push(token)
    while not stack.isEmpty:
        result.append(stack.pop())
    return string.join(result)
    

################    liste linéaire    ################ 

class lineaire:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def lenghtV1(self):
        return self.count
    
    def lenghtV2(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.count += 1
    
    def addAfter(self, base: Node, item):
        temp = Node(item)
        temp.setNext(base.getNext())
        base.setNext(temp)
        self.count += 1
    
    def search(self, item):
        current = self.head
        found = False
        while current!= None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self, base: Node):
        current = self.head
        previous = None
        found = False
        while current!= None and not found:
            if current is base:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous != None:
            previous.setNext(base.getNext())
        else:
            self.head = base.getNext()
    

################    liste bidirectionnelle    ################ 

class bidirect:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def lenght(self):
        return self.count
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.head != None:
            self.head.setPrevious(temp)
        self.head = temp
        self.count += 1
    
    def addAfter(self, base: Node, item):
        temp = Node(item)
        temp.setNext(base.getNext())
        temp.setPrevious(base)
        if base.getNext() != None:
            base.getNext().setPrevious(temp)
        base.setNext(temp)
        self.count += 1
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self, base):
        previous = base.getPrevious()
        if base.getNext() != None:
            base.getNext().setPrevious(previous)
        if previous != None:
            previous.setNext(base.getNext())
        else:
            self.head = base.getNext()
        self.count -= 1


################    liste circulaire    ################ 

class circ:
    def __init__(self):
        self.head = Node(-1)
        self.head.setNext(self.head)
        self.count = 0
    
    def isEmpty(self):
        return self.head.getNext() == self.head
    
    def lenght(self):
        return self.count
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)
        self.count += 1
    
    def addAfter(self, base: Node, item):
        temp = Node(item)
        temp.setNext(base.getNext())
        base.setNext(temp)
        self.count += 1
    
    def search(self, item):
        current = self.head.getNext()
        found = False
        while current!= self.head and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self, base: Node):
        current = self.head.getNext()
        previous = self.head
        found = False
        while current!= self.head and not found:
            if current is base:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            previous.setNext(base.getNext())
            self.count -= 1