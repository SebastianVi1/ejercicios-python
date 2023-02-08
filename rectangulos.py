class Punto():#se define clase llamada punto
    def __init__(self,x,y):#se define el constructor  y sus parametros
        self.x = x#variables dentro de la clase Punto
        self.y = y
    def __str__(self) -> str:#se convierte en una cadena el resultado de punto
        return "(x="+ str(self.x)+", y="+ str(self.y)+ ")"
class Linea():#clase que toma valores iniciales y finales para construir una linea
    def __init__(self,inicial, final ):#constructor inicial
        self.inicial = inicial
        self.final = final
    def __str__(self) -> str:
        return "("+ str(self.inicial)+ ", "+ str(self.final)+ ")"

#funcion que lee 8 e nteros y regresa cuatro puntos
def cordenadas(num):#funcion que pide numeros los divide y los guarda en cordenadas
    list = num.split(' ')
    cor1 = list[0:2]#de la lista(list) agarramos los primeros dos parametros
    punto1 = Punto(cor1[0], cor1[1])#las cordenadas las pasa a la variable punto1
    cor2 = list[2:4]
    punto2 = Punto(cor2[0], cor2[1])
    cor3 = list[4:6]
    punto3 = Punto(cor3[0], cor3[1])
    cor4 = list[6:8]
    punto4 = Punto(cor4[0], cor4[1])
    
    return punto1, punto2, punto3, punto4
a = input()#colocar numeros y guardarlos en cordenadas1
cordenadas1 = cordenadas(a)

b = input()#colocar numeros y guardarlos en cordenadas2
cordenadas2 = cordenadas(b)

def paralelas(linea1: Linea, linea2: Linea):#validar si las lineas introducidas son paralelas
    paraleloInicial = False#inicializar que ninguna linea hasta ahora es paralela
    paraleloFinal = False
    if linea1.inicial.x <= linea2.inicial.x:#comparamos
         if linea1.inicial.y >= linea2.inicial.y:
             paraleloInicial = True
    if linea1.final.x >= linea2.final.x:
        if linea1.final.y >= linea2.final.x:
            paraleloFinal = True

    return paraleloInicial and paraleloFinal



    
