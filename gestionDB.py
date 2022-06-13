import PySimpleGUI as sg
import windows.agregar_cliente as w2
import windows.config_window as w1
import windows.agregar_vehiculo as w3
import windows.agregar_orden as w4



def main():
    '''
    
    '''
    sg.theme('Default1')   # Add a touch of color
    sg.SetOptions(element_padding=(45, 15), margins = (10, 2))
    # All the stuff inside your window.
    layout = [  
        [sg.Push(),sg.Text('Welcome to GestionDB!'),sg.Push()],
        [sg.Frame('MENU', [
            [sg.Button('CARGAR ORDEN', size = (25), border_width = 2, key="-ORDEN-")],
            [sg.Button('CARGAR CLIENTE', size = (25), border_width = 2, key="-CLIENTE-")],
            [sg.Button('CARGAR VEHICULO', size = (25), border_width = 2, key="-VEHICULO-")],
            [sg.Button('CONFIGURACION', size = (25), border_width = 2, key="-CONFIG-")]
                          ],
                  background_color='lightblue', border_width = 4,     
                         )],
        [sg.Push(),sg.Button('SALIR', mouseover_colors = ("Red"), size = (10), key="-EXIT-"),sg.Push()] 
            ]        

    # Create the Window
    window = sg.Window('GestionDB', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break
        if event == "-CONFIG-":
            window.hide()
            w1.config_window(window)
        if event == "-CLIENTE-":
            window.hide()
            w2.agregar_cliente(window)
        if event == "-VEHICULO-":
            window.hide()
            w3.agregar_vehiculo(window)
        if event == "-ORDEN-":
            window.hide()
            w4.agregar_orden(window)
                

    window.close()

if __name__ == "__main__":
    main()