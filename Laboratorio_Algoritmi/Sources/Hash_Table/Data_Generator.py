import json

def Data_Generator(data, x, y):
    f = open(data, "a")

    f.write(str(x))
    f.write(' ')
    f.write(str(y) + "\n")
    
    f.close()