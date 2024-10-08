from proyect2.file_manager import FileManager
from proyect2.movimientos_manager import MovimientosManager
from gui_manager import GUIManager
import PySimpleGUI as sg

def main():
    # Cargar datos
    file_manager = FileManager()
    data = file_manager.load_data()

    movimientos_manager = MovimientosManager(data)
    gui_manager = GUIManager(data)
    
    #  eventos
    def handle_event(window, event, values):
        # Agregar Categoria
        if event == "Agregar Categoria":
            category = sg.popup_get_text("Ingrese la nueva categoria:")
            if category:
                try:
                    movimientos_manager.add_categoria(category)
                    window['-CATEGORIAS-'].update(values=data["categorias"])
                    file_manager.save_data(data)
                    sg.popup("Categoria anadida correctamente.", title="exito")
                except ValueError as e:
                    sg.popup_error(str(e))
        
        # Agregar Gasto
        elif event == "Agregar Gasto":
            title = sg.popup_get_text("Ingrese el titulo del gasto:")
            amount = sg.popup_get_text("Ingrese el monto del gasto:")
            # Ahora podemos seleccionar la categoría directamente desde las disponibles
            category = sg.popup_get_text("Ingrese la categoria del gasto o seleccione una existente:", default_text=", ".join(data["categorias"]))

            if title and amount and category:
                try:
                    movimientos_manager.add_movimiento("gasto", title, amount, category)
                    window['-TABLE-'].update(values=[[m["titulo"], m["monto"], m["categoria"]] for m in data["movimientos"]])
                    file_manager.save_data(data)
                    sg.popup("Gasto anadido correctamente.", title="exito")
                except ValueError as e:
                    sg.popup_error(str(e))

        # Agregar Ingreso
        elif event == "Agregar Ingreso":
            title = sg.popup_get_text("Ingrese el titulo del ingreso:")
            amount = sg.popup_get_text("Ingrese el monto del ingreso:")
            # Ahora podemos seleccionar la categoría directamente desde las disponibles
            category = sg.popup_get_text("Ingrese la categoria del ingreso o seleccione una existente:", default_text=", ".join(data["categorias"]))

            if title and amount and category:
                try:
                    movimientos_manager.add_movimiento("ingreso", title, amount, category)
                    window['-TABLE-'].update(values=[[m["titulo"], m["monto"], m["categoria"]] for m in data["movimientos"]])
                    file_manager.save_data(data)
                    sg.popup("Ingreso anadido correctamente.", title="exito")
                except ValueError as e:
                    sg.popup_error(str(e))

    gui_manager.run(handle_event)

if __name__ == "__main__":
    main()

