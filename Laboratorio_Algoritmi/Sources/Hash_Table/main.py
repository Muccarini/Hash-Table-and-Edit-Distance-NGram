import inquirer ##pip install inquirer
import sys
import os.path
import random
from HashTable import HashTable
from Data_Generator import Data_Generator

print (sys.version)

##COLLISION
questions = [inquirer.List('collision',
            message="Scegli come vuoi gestire le collisioni",
            choices=['open', 'chain'],),]
collision = inquirer.prompt(questions)

##KEYS

print("Inserire QUANTE keys m")
m = input()

##VALUES
if(collision['collision'] == 'open'):
    print("Inserire QUANTI valori n,  LEN(N) <= M")
else:
    print("Inserire QUANTI valori n")
n_values = input()

questions = [inquirer.List('values',
            message="Inserire QUALI valori n",
            choices=['random', 'manuale'],),]
values = inquirer.prompt(questions)

n = []

if(values['values'] == 'manuale'):
    for j in range(0, int(n_values)):
        print("inserisci valore " + str(j))
        k = input()
        n.append(int(k))

if(values['values'] == 'random'):
        for j in range(0, int(n_values)):
            k = random.randint(0, 100000)
            n.append(k)

##HASH
hash = HashTable(int(m), collision['collision'])

##CHECK DATA
if(os.path.isfile('./data.txt')):
    os.remove("data.txt")
    print("\nSONO STATI CANCELLATI I DATI DELL' ULTIMO TEST\n")

data = "data.txt"
alpha = 0
collision_count = 0

##INSERT/STORING DATA/COLLISION COUNT
for v in range(0, len(n)):
    Data_Generator(data, v / int(m), collision_count)
    if(hash.insert(n[v])):
        collision_count = collision_count + 1

alpha = len(n) / int(m)

##RESULTS
print("\nQuesto è il numero di collisioni:")
print(collision_count)
print("\nQuesto è il numero di chiavi m:")
print(m)
print("\nQuesto è il numero di valori n:")
print(len(n))
print("\nQuesto è il tuo fattore di carico:")
print(alpha)

print("\nE' STATO GENERATO UN FILE 'data.txt' CONTENENTE LE COORDINATE X = FATTORE DI CARICO, Y = NUMERO COLLISIONI\n\n")

print("\nVuoi stampare l' HASH, si o no?\n")
yn = input()
if(yn == 'si'):
    print(hash)

end = input()
