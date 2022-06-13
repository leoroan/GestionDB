from modulos_sql.modulos import insertar_orden
import PySimpleGUI as sg


def agregar_orden(ventana):   
            
    '''
    Required imports!
    '''
    sg.theme('Default1')
    layout = [
        [sg.Text("Ventana de carga de ordenes de  servicio")],
        [sg.Frame('DATOS NUEVO VEHÍCULO', [
            [sg.Text('ORDEN NRO', size =(15, 1), ), sg.InputText(default_text = "escriba un nro de orden", key="-ORDENNRO-")],
            [sg.Text('FECHA', size =(15, 1)), sg.InputText(default_text = "seleccione una fecha", key="-FECHA-")],
            [sg.Text('CANT. HORAS', size =(15, 1)), sg.InputText(default_text = "cantidad de horas trabajadas", key="-CANTHORAS-")],
            [sg.Text('NOMBRE DEL TERCERO', size =(15, 1)), sg.InputText(default_text = "escriba el nombre del tercero", key="-NOMTERCERO-")],
            [sg.Text('TELEFONO TERCERO', size =(15, 1)), sg.InputText(default_text = "escriba el telefono del tercero", key="-TELTERCERO-")],
            [sg.Text('ES SERVICIO?', size =(15, 1)), sg.InputText(default_text = "seleccione si es servicio o no", key="-ESSERVICIO-")],
                          ],
                  background_color='lightblue', border_width = 4,     
                         )],
        [sg.Button('VOLVER'),sg.Button('GUARDAR', key="-SAVEORDEN-", focus = True)]
             ]
    window = sg.Window("CARGA DE ORDENES", layout, modal=True, finalize=True)
    while True:
        event, values = window.read()
        if event == "VOLVER" or event == sg.WIN_CLOSED:
            ventana.un_hide()
            break
        if event == "-SAVEORDEN-":
            if (insertar_orden(values["-PATENTE-"].upper(),values["-MODELO-"].upper(),values["-ANIO-"],values["-CHASIS-"],values["-MOTOR-"],values["-DESCRIPCION-"].upper())):
                sg.popup_no_buttons("NUEVA ORDEN AGREGADA!",auto_close = True, auto_close_duration = 2 ) 
            else:
                sg.popup_no_buttons("¡ERROR AL QUERER AGREGAR NUEVA ORDEN, INTENTE NUEVAMENTE!",auto_close = True, auto_close_duration = 2, text_color = "Red" )

    window.close()
