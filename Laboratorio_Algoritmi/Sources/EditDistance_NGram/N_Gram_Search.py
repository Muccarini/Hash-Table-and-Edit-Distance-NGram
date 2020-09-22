import json
from timeit import default_timer as timer
from Ngram_Word import Ngram_Word
from Edit_Distance import Edit_Distance

def N_Gram_Search(choice):
    n_gram = 0
    if(choice == '2_gram'):
        lexicon = json.load( open( "lessico_2_gram.json" ) )
        n_gram = 2
    else:
        lexicon = json.load( open( "lessico_3_gram.json" ) )
        n_gram = 3
    
    while(1):
        print("Inserisci una stringa, 0 per tornare al menu")
        query = input()

        if(query == '0'):
            return
        start = timer()
        Q = Ngram_Word(n_gram, query)
        E = []
        alternative = []
        for i in Q:
            if(i in lexicon.keys()):
                E.append(lexicon[i])
    
        result = None
        tmp_cost = float("inf")
        cost = tmp_cost
        for i in range(0, len(E)):
            for j in range(0, len(E[i])):
                tmp_cost = Edit_Distance(query, E[i][j])
                if(tmp_cost < cost):
                    cost = tmp_cost
                    result = E[i][j]
                    alternative.append(result)
        end = timer()
        print(end - start, "sec")
                
        if(result == None or cost > 10):
            print("\nintendi veramente: \n" + query + "\nnon trovo niente di simile nel mio lessico \n")
        else:
            if(len(alternative) >= 4):
                print("\nforse intendevi:" + result + " o, " + alternative[len(alternative) - 4]+ ", "
                + alternative[len(alternative) - 3] + ", " + alternative[len(alternative) - 2] + ", ")
                print("hai sbagliato di",cost ,"lettere/a \n")
            else:
                print("\nforse intendevi:" + result)