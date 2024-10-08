import re
#importar re

class MovimientosManager:
    
    def __init__(self, data):
        self.data = data
    
    # Validar caracteres
    def validar_categoria(self, categoria):
        return bool(re.match("^[A-Za-z0-9\s]+$", categoria))
    
    #nueva categoría
    def add_categoria(self, categoria):
        if not self.validar_categoria(categoria):
            raise ValueError("La categoria solo puede contener caracteres alfanumericos y espacios")
        
        if categoria not in self.data['categorias']:
            self.data['categorias'].append(categoria)
        return self.data

    # Anadir un nuevo movimiento
    def add_movimiento(self, tipo, titulo, monto, categoria):
        try:
            monto = float(monto)
        except ValueError:
            raise ValueError("El monto debe ser un numero valido.")

        if categoria in self.data['categorias']:
            self.data['movimientos'].append({
                "tipo": tipo,
                "titulo": titulo,
                "monto": monto,
                "categoria": categoria
            })
        else:
            raise ValueError("La categoraa no existe.")
        return self.data
