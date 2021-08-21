def numeros (n1,n2,n3):
    mayor = max(n1,n2,n3)
    menor = min(n1,n2,n3)
    media = sum ([n1,n2,n3])/len([n1,n2,n3])
    print (f"El mayor es {mayor}, el menor es {menor}, su media {media}")


numeros(2,10,4)