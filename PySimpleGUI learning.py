import PySimpleGUI as sg

layout = [
            [sg.Text('1. '), sg.InputText()],
            [sg.Text('2. '), sg.InputText()],
            [sg.Text('3. '), sg.InputText()],
            [sg.Button('Save'), sg.Button('Exit')]
         ]

window = sg.Window('To Do List Example', layout)

while True:
    event, values = window.read()
    if event  == sg.WIN_CLOSED:
        break
    elif event == 'Exit':
        break
    elif event == 'Save':
        sg.Print(values[0])