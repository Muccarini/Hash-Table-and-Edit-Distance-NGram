from timeit import default_timer as timer
from Edit_Distance import Edit_Distance

def Edit_Distance_Search():
    while(1):
        print("Inserisci una stringa, 0 per tornare al menu")
        query = input()
        if(query == '0'):
            return
        start = timer()
        result = None
        tmp_cost = float("inf")
        cost = tmp_cost
        alternative = []
    
        with open("60000_parole_italiane.txt", 'r') as file:
            for line in file:
                for word in line.split():
                    tmp_cost = Edit_Distance(query, word)
                    if(tmp_cost < cost):
                        cost = tmp_cost
                        result = word
                        alternative.append(result)
        end = timer()
        print(end - start)
                
        if(result == None or cost > 10):
            print("\nintendi veramente: \n" + query + "\nnon trovo niente di simile nel mio lessico \n")
        else:
            if(len(alternative) >= 4):
                print("\nforse intendevi:" + result + " o, " + alternative[len(alternative) - 4]+ ", "
                + alternative[len(alternative) - 3] + ", " + alternative[len(alternative) - 2] + ", ")
                print("hai sbagliato di",cost ,"lettere/a \n")
            else:
                print("\nforse intendevi:" + result)