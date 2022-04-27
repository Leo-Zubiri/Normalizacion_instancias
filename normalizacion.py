from numpy import transpose
import archivo

"""
dataset
[
[[atb1,atb2...],clase/accion],
[[atb1,atb2...],clase/accion],
[[atb1,atb2...],clase/accion]...
]

caracts:
Solo las caracteristicas sin respuesta/accion
[80.0, 90.0, 75.0, 70.0, 85.0, 90.0]
[75.0, 59.0, 73.0, 90.0, 79.0, 90.0]
....

cols:
Obtiene las columnas en listas
"""

def normalizar(dataset = []):

    caracts = [x[0] for x in dataset]
    cols = transpose(caracts)
    colsNorm = []
    colsComp = []

    for col in cols:
        minCol = min(col)
        mayCol = max(col)
        dif = mayCol-minCol
        auxNorm = []
        auxComp = []

        for Xi in col:
            XNorm = round((Xi-minCol)/dif,3)
            XComp = round(1-XNorm,3)
            auxNorm.append(XNorm)
            auxComp.append(XComp)

        colsNorm.append(auxNorm)
        colsComp.append(auxComp)

        #print("min: {} may:{}".format(minCol,mayCol))

    colsNorm = transpose(colsNorm)
    colsComp = transpose(colsComp)

    instanciaNormalizada = [[list(colsNorm[i]),dataset[i][1]] for i in range(len(dataset))]
    instanciaComplemento = [[list(colsComp[i]),dataset[i][1]] for i in range(len(dataset))]

    archivo.crearCsv(instanciaNormalizada,"normalizados\\inst_norm.csv")
    archivo.crearCsv(instanciaComplemento,"normalizados\\inst_comp.csv")

    #print(instanciaNormalizada)
    #print(colsNorm)
    #print(colsComp)