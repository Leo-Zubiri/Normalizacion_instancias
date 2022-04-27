
import archivo as f
from normalizacion import normalizar

instancia = f.cargarInstancia(ruta='InstanciaClase.txt',delimiter='\t')

normalizar(instancia)