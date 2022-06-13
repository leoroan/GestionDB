def config_window(ventana):
    '''
    
    '''
    import PySimpleGUI as sg

    sg.theme('Default1')
    layout = [
        [sg.Text("Ventana de Configuracion")],
        [sg.Frame('OPCIONES', [
            [sg.Button('CARGAR DB', size = (25), border_width = 2, key="-CDB-")],
            [sg.Button('GENERAR DB', size = (25), border_width = 2, key="-GDB-")],
            [sg.Button('OTRA CONFIG.', size = (25), border_width = 2, key="-OTRA-")]
                          ],
                  background_color='lightblue', border_width = 4,     
                         )],
        [sg.Button('VOLVER')]
             ]
    window = sg.Window("Configuracion", layout, modal=True, finalize=True)
    while True:
        event, values = window.read()
        if event == "VOLVER" or event == sg.WIN_CLOSED:           
            ventana.un_hide()
            break
                  
    window.close()