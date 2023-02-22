##############################
##                          ##
##        Séance n°1        ##
##                          ##
##############################


# ----------------------------------------------------------------

## exercice 1.1

class Nbr_complexe:
    def __init__(self, réel=0, imaginaire=0):
        self.__reel = réel
        self.__im = imaginaire

    @property
    def reel(self):
        return self.__reel
    
    @property
    def im(self):
        return self.__im
    
    def get_reel(self):
        return f"{self.reel}"

    def get_im(self):
        return f"{self.im}i" 
    
    def __str__(self):
        return f"{' ' if self.reel >= 0 else ''}{self.reel}{'+' if self.im >= 0 else ''}{self.im}i"
    
    def __add__(self, other):
        if isinstance(other, (int, float)) or isinstance(other, Nbr_complexe):
            if isinstance(other, (int, float)):
                other = Nbr_complexe(other, 0) 
            im_sum = self.im + other.im
            reel_sum = self.reel + other.reel
            return f"{' ' if reel_sum >= 0 else ''}{reel_sum}{'+' if im_sum >= 0 else ''}{im_sum}i"
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)) or isinstance(other, Nbr_complexe):
            if isinstance(other, (int, float)):
                other = Nbr_complexe(other, 0)
            im_mul = self.reel * other.im + self.im * other.reel
            reel_mul = self.reel * other.reel + self.im * other.im * -1
            return f"{' ' if reel_mul >= 0 else ''}{reel_mul}{'+' if im_mul >= 0 else ''}{im_mul}i"
        else:
            return NotImplemented
        
    def __iadd__(self, other):
        res = self + other # exemple : 1+2i
        if '+' in res[1:]:
            index = res[1:].index('+')
        else:
            index = res[1:].index('-')
        self.__reel, self.__im  = int(res[:index+1]), int(res[index+1:])
        return self
    
    def __imul__(self, other):
        res = self * other # exemple : 1+2i
        if '+' in res[1:]:
            index = res[1:].index('+')
        else:
            index = res[1:].index('-')
        self.__reel, self.__im  = int(res[:index+1]), int(res[index+1:len(res) -1])
        return self

# ----------------------------------------------------------------

## exercice 1.2

class MatriceComplexe:
    def __init__(self, n=1, m=1, val= Nbr_complexe(0, 0)):
        self.__n = n
        self.__m = m
        if isinstance(val, (int, float)) or isinstance(val, Nbr_complexe):
            if isinstance(val, (int, float)):
                val = Nbr_complexe(val, 0)
            self.__matrice = [[val for _ in range(m)] for _ in range(n)]
        else:
            return NotImplemented
    
    @property
    def n(self):
        return self.__n
    
    @property
    def m(self):
        return self.__m
    
    def get_lignes(self):
        return self.n
    
    def get_colonnes(self):
        return self.m
    
    def __str__(self):
        print()
        for i in range(self.n):
            for j in range(self.m):
                print(f' {self.__matrice[i][j]}', end='')
            print()
        return str()
    
    def __getitem__(self, item):
        ligne, colonne = item
        return self.__matrice[ligne][colonne]
    
    def __setitem__(self, item, value):
        ligne, colonne = item
        self.__matrice[ligne][colonne] = value
    
    def __imul__(self, other):
        for i in range(self.n):
            for j in range(self.m):
                self[i, j] = self[i, j] * other
        return self
    
# ----------------------------------------------------------------

# exercice 1. 3     ---->      liste bidirectionnelle circulaire







# ----------------------------------------------------------------

## exercice 1.4

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def __len__(self):
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
            

def palindrom():
    stack = Stack()

    element = input('Premier item : ')
    while element != '*':
        stack.push(element)
        element = input('Nouvel item (* au milieu): ')

    res = True
    print("-" * 16)
    element = input('Item mirroir (# à la fin): ')
    while element != '#':
        if not stack.is_empty() and element == stack.pop():
            element = input('Item mirroir (# à la fin): ')
        else:
            res = False
            break
    if stack.is_empty() and res:
        print("C'est un palindrom ! ✅")
    else:
        print("C'est pas un palindrom ! ❌")