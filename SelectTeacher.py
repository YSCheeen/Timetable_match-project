import PySimpleGUI as sg
import tomatchfile


def select_teachers(tomatch_subject):
    teachers_initials_list = tomatchfile.open_teacher_list(tomatch_subject)
    teachers_list = tomatchfile.load_teacher_list(tomatch_subject)

    layout = [[sg.Text('选择老师')],
              [sg.OptionMenu(teachers_initials_list, size=(40, 8), key='-OPTION MENU-')],
              [sg.OptionMenu(teachers_initials_list, size=(40, 8), key='-OPTION MENU-0')],
              [sg.Button('Save'), sg.Button('Cancel')]]

    window = sg.Window('Select teachers', layout)
    # Event Loop
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):  # always check for closed window
            break
        # if a list item is chosen
        elif event == 'Save':
            sg.popup('你选择的老师是：', values['-OPTION MENU-'], '和', values['-OPTION MENU-0'])
            teacher_A = values['-OPTION MENU-']
            teacher_B = values['-OPTION MENU-0']
        window.close()

    teacher_A_personal = tomatchfile.selected_teacher_personal(teachers_list,teacher_A)
    teacher_B_personal = tomatchfile.selected_teacher_personal(teachers_list,teacher_B)

    return teacher_A_personal, teacher_B_personal





