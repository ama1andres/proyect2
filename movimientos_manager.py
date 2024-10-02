class MovimientosManager:
    
    
    def __init__(self, data):
        self.data = data
    #cat añadir
    def add_categoria(self, categoria):
        if categoria not in self.data['categorias']:
            self.data['categorias'].append(categoria)
        return self.data
    

    # mov añadir
    def add_movimiento(self, tipo, titulo, monto, categoria):
        if categoria in self.data['categorias']:
            self.data['movimientos'].append({
                "tipo": tipo,
                "titulo": titulo,
                "monto": float(monto),
                "categoria": categoria
            })
        return self.data
