import PySimpleGUI as sg

class GUIManager:
    def __init__(self, data):
        self.data = data

    def create_layout(self):
        # Table for movimientos and Listbox for categorias
        return [
            [sg.Text("Movimientos:")],
            [sg.Table(values=[[m["titulo"], m["monto"], m["categoria"]] for m in self.data["movimientos"]],
                    headings=["Titulo", "Monto", "Categoria"], key='-TABLE-', auto_size_columns=True)],


            [sg.Text("Categorias:")],
            [sg.Listbox(values=self.data["categorias"], size=(20, 5), key='-CATEGORIAS-')],

            [sg.Button("Agregar categoria"), sg.Button("Agregar gasto"), sg.Button("Agregar ingreso")]
        ]


    def run(self, event_handler):
        window = sg.Window("Finanzas personales", self.create_layout())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            event_handler(window, event, values)
        window.close()
