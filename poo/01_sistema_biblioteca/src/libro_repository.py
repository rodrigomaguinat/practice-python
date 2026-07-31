# copied code

import json
import os
from src.libro import Libro

class LibroRepository:
    def __init__(self, path_json="data/libros_prueba.json"):
        self.path_json = path_json

    def obtener_todos(self):
        """Lee el JSON y devuelve una lista de objetos de tipo Libro"""
        if not os.path.exists(self.path_json):
            return []

        # Forzamos UTF-8 para leer correctamente tildes y eñes
        with open(self.path_json, "r", encoding="utf-8") as archivo:
            datos_planos = json.load(archivo)
        
        libros_objetos = []
        for item in datos_planos:
            # Mapeamos las llaves exactas con tildes de tu JSON a la clase Libro
            nuevo_libro = Libro(
                código=item["código"],
                ISBN=item["isbn"],
                título=item["título"],
                autor=item["autor"],
                editorial=item["editorial"],
                año=item["año"],
                categoría=item["categoría"],
                cantidad=item["cantidad"]
            )
            libros_objetos.append(nuevo_libro)
            
        return libros_objetos
