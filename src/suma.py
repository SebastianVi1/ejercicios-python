
def sum_clever(a, b):
    return distancia(b)- distancia(a-1)

def distancia(n):
    return  (n*(n+1))/2



n = int(input())
for i in range(n):
    num = input()
    lista = num.split(' ')
    a = int(lista[0])
    b = int(lista[1])
    print(sum_clever(a, b))
    