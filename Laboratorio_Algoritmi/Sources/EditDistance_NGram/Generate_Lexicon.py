def Generate_Lexicon(data, n_gram):
    from itertools import product
    from string import ascii_lowercase
    import json

    keywords = [''.join(i) for i in product(ascii_lowercase, repeat = n_gram)]

    lexicon = {}

    for j in keywords:
        with open(data,'r') as file:
            for line in file:
                for word in line.split():
                    if(j in word):
                        if(j in lexicon.keys()):
                            lexicon[j].append(word)
                        else:
                            lexicon[j] = []
                            lexicon[j].append(word)
    
    ##json leggibile, pesa di piu' se leggibile
    json.dump( lexicon, open( "lessico.json", 'w' ) )