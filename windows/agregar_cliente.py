from modulos_sql.modulos import insertar_cliente
import PySimpleGUI as sg

def agregar_cliente(ventana):   
            
    '''
    Required imports!
    '''
    sg.theme('Default1')
    layout = [
        [sg.Text("Ventana de carga de clientes")],
        [sg.Frame('DATOS NUEVO CLIENTE', [
            [sg.Text('NOMBRE', size =(15, 1), ), sg.InputText(default_text = "escriba un nombre", key="-NOMBRE-",do_not_clear = False)],
            [sg.Text('APELLIDO', size =(15, 1)), sg.InputText(default_text = "escriba un apellido", key="-APELLIDO-",do_not_clear = False)],
            [sg.Text('TELEFONO', size =(15, 1)), sg.InputText(default_text = "escriba un telefono", key="-TELEFONO-",do_not_clear = False)],
            [sg.Text('DOMICILIO', size =(15, 1)), sg.InputText(default_text = "escriba un domicilio", key="-DOMICILIO-",do_not_clear = False)],
                          ],
                  background_color='lightblue', border_width = 4,     
                         )],
        [sg.Button('VOLVER'),sg.Button('GUARDAR', key="-SAVECLIENTE-", focus = True)]
             ]
    window = sg.Window("CARGA DE CLIENTES", layout, modal=True, finalize=True)
    while True:
        event, values = window.read()
        if event == "VOLVER" or event == sg.WIN_CLOSED:
            ventana.un_hide()
            break
        if event == "-SAVECLIENTE-":
            if (insertar_cliente(values["-NOMBRE-"].title(),values["-APELLIDO-"].title(),values["-TELEFONO-"],values["-DOMICILIO-"])):
                sg.popup_no_buttons("NUEVO CLIENTE AGREGADO!",auto_close = True, auto_close_duration = 2 )
            else:
                sg.popup_no_buttons("¡ERROR AL QUERER AGREGAR NUEVO CLIENTE, INTENTE NUEVAMENTE!",auto_close = True, auto_close_duration = 2, text_color = "Red" )
    window.close()