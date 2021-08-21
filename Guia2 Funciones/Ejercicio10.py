def tupla_ordenada (tupla):
    tupla_ord = list (tupla)
    tupla_ord.sort()
    tupla_ord = tuple(tupla_ord)
    
    if tupla_ord == tupla:
        print ("Esta ordenada")
    else:
        print ("No esta ordenada")

tupla_ordenada (1,2,3,4,8,6)