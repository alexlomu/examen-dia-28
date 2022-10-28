class Nodo(object):
    # Clase nodo simplemente enlazado
    info, sig = None, None
aux = Nodo()
aux.info = "Primer nodo"
palabra = input("Ingrese una palabra: ")
naux = aux
while (palabra != ""):
    nodo = Nodo()
    nodo.info = palabra
    naux.sig = nodo
    naux = nodo
    palabra = input("Ingrese una palabra: ")

while (aux is not None):
    print(aux.info)
    aux = aux.sig

class datoPolinomio(object):
    def __init__(self,valor,termino):
        self.valor = valor
        self.termino = termino
    
class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1
    
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux 
    
    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0

def restar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            nuevo_mayor = polinomio1 if (polinomio1.valor > polinomio2.valor) else polinomio2
            if nuevo_mayor == polinomio1:
                menor = polinomio2
            else:
                menor = polinomio1
            total = Polinomio.obtener_valor(nuevo_mayor,i) - Polinomio.obtener_valor(menor,i)
            if total != 0:
                Polinomio.agregar_termino(paux, i, total)
        return paux

def dividir(Polinomio1,Polinomio2):
        lista = []
        dividendo = Polinomio1
        divisor = Polinomio2
        while dividendo.grado >= divisor.grado:
            resultado = Polinomio.obtener_valor(dividendo,i) / Polinomio.obtener_valor(divisor,i)
            lista.append(resultado)
            dividendo = dividendo - (Polinomio([resultado]) * divisor)
 
 
        return lista

def eliminar_termino(polinomio, termino, valor, eliminar):
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if polinomio.termino == eliminar:
        Polinomio.modificar_termino(polinomio, termino, None)



def buscar_termino(polinomio, buscado):
    if polinomio.termino == buscado:
        print("Se ha encontrado el termino introducido en el polinomio")
    else:
        print("No se ha encontrado el termino introducido en el polinomio")