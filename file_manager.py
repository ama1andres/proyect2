import json
import os

class FileManager:
    def __init__(self, filename='finanzas.json'):
        self.filename = filename


    def load_data(self):
        if os.path.exists(self.filename):
            #cargar datos al json
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {"categorias": [], "movimientos": []}


    #salvar los datos en el json
    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
