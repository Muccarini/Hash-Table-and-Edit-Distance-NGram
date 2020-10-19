class HashTable:
    def __init__(self, m, collision_type):
        self.lenght = m
        self.type = str(collision_type)

        if(self.type == 'open'):
            self.table = [None] * int(m)
        if(self.type == 'chain'):
            self.table = [[] for _ in range(int(m))]

    def __str__(self):
        return str(self.table)

    def hashing_func(self, value):
        return value % self.lenght

    def insert(self, value):
        hash_key = self.hashing_func(int(value))
        collide = False

        ##OPEN
        if(self.type == 'open'):
            i = 0
            while(self.table[hash_key] != None and self.table[hash_key] != 'DEL' and i != self.lenght):
                i = i + 1
                hash_key = self.hashing_func(int(value) + i)
                collide = True
            if(i == self.lenght):
                print("ERROR:Hash table overflow!")
                return False
            else:
                self.table[hash_key] = value
                return collide

        ##CHAIN
        if(self.type == 'chain'):
            if(self.table[hash_key]):
                collide = True
            self.table[hash_key].insert(0, value)
            return collide

            
            
    def search(self, value):
        hash_key = self.hashing_func(int(value))

        if(self.type == 'open'):
            i = 0
            while(self.table[hash_key] != None or i != self.lenght):
                if(self.table[hash_key] == value):
                    return hash_key
                i = i + 1
                hash_key = self.hashing_func(int(value) + i)

        if(self.type == 'chain'):
            return self.table[hash_key].index(value)

    
    def delete(self, value):
        
        if(self.type == 'open'):
            self.table[(self.search(value))] = 'DEL'

        hash_key = self.hashing_func(int(value))
        if(self.type == 'chain'):
            self.table[hash_key].remove(value)

