import PySimpleGUI as sg
import tomatchfile


def select_subject():
    subjects_list = tomatchfile.obtain_subjectlist()

    layout = [[sg.Text('选择学科(点一下就选上了)')],
              [sg.Listbox(subjects_list, size=(40, 8), enable_events=True, key='-LIST-')],
              [sg.Button('Exit')]]

    window = sg.Window('Listbox for selecting subject', layout)
    # Event Loop
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):  # always check for closed window
            break
        # if a list item is chosen
        elif event == '-LIST-' and len(values['-LIST-']):
            sg.popup('你选择的科目是：', values['-LIST-'])

    window.close()
    tomatch_subject = values['-LIST-'][0]
    return tomatch_subject

