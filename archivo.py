"""
Diseñado para trabajar con instancias en listas con formato:
[
    [[atb1,atb2...],clase/accion],
    [[atb1,atb2...],clase/accion],
    [[atb1,atb2...],clase/accion]...
]
"""

def cargarInstancia(ruta='',hasHeader=False,hasIndex=False,delimiter=','):
    file = open(ruta)
    fileContent = file.readlines()

    lista = [linea.split(delimiter) for linea in fileContent]  #instancia wine
    #lista = [linea.split("\t") for linea in trainContent] #Instancia clase

    instancia = [ [ list(map(float,x[:len(lista[0])-1])), x[len(lista[0])-1].replace("\n","") ] for x in lista ]
    file.close()

    return instancia

def crearCsv(instancia=[],fileName="normalizados\\archivo.csv"):
    file = open(fileName,"w")
    file.write("")
    for inst in instancia:
        for atbs in inst[0]:
            file.write(str(atbs)+",")
        file.write(inst[1]+"\n")
    file.close()
