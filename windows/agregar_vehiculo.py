from modulos_sql.modulos import insertar_vehiculo
import PySimpleGUI as sg


#PARA CARGAR un auto necesito un cliente previamente


def agregar_vehiculo(ventana):   
            
    '''
    Required imports!
    '''
    sg.theme('Default1')
    layout = [
        [sg.Text("Ventana de carga de vehiculos")],
        [sg.Frame('DATOS NUEVO VEHÍCULO', [
            [sg.Text('PATENTE', size =(15, 1), ), sg.InputText(default_text = "escriba una patente", key="-PATENTE-")],
            [sg.Text('MODELO', size =(15, 1)), sg.InputText(default_text = "escriba un modelo", key="-MODELO-")],
            [sg.Text('AÑO', size =(15, 1)), sg.InputText(default_text = "escriba un año de fabricacion", key="-ANIO-")],
            [sg.Text('NRO CHASIS', size =(15, 1)), sg.InputText(default_text = "escriba el numero de chasis", key="-CHASIS-")],
            [sg.Text('NRO MOTOR', size =(15, 1)), sg.InputText(default_text = "escriba el numero de motor", key="-MOTOR-")],
            [sg.Text('DESCRIPCION', size =(15, 1)), sg.InputText(default_text = "escriba una descripcion/mensaje", key="-DESCRIPCION-")],
                          ],
                  background_color='lightblue', border_width = 4,     
                         )],
        [sg.Button('VOLVER'),sg.Button('GUARDAR', key="-SAVEVEHICULO-", focus = True)]
             ]
    window = sg.Window("CARGA DE CLIENTES", layout, modal=True, finalize=True)
    while True:
        event, values = window.read()
        if event == "VOLVER" or event == sg.WIN_CLOSED:
            ventana.un_hide()
            break
        if event == "-SAVEVEHICULO-":
            if (insertar_vehiculo(values["-PATENTE-"].upper(),values["-MODELO-"].upper(),values["-ANIO-"],values["-CHASIS-"],values["-MOTOR-"],values["-DESCRIPCION-"].upper())):
                sg.popup_no_buttons("NUEVO VEHÍCULO AGREGADO!",auto_close = True, auto_close_duration = 2 ) 
            else:
                sg.popup_no_buttons("¡ERROR AL QUERER AGREGAR NUEVO VEHICULO, INTENTE NUEVAMENTE!",auto_close = True, auto_close_duration = 2, text_color = "Red" )

    window.close()
