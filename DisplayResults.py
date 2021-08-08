import PySimpleGUI as sg


def show_results(teacher_A, teacher_B, teachers_slot, candidate_students, teachers_slots_detail,
                 candidate_student_list):
    layout = [[sg.Text('当前成组的老师为：'), sg.Text(teacher_A), sg.Text(teacher_B)],
              [sg.Text('共同的空闲时段总数：'), sg.Text(teachers_slot)],
              [sg.Text('可匹配学生数量：'), sg.Text(candidate_students)],
              [sg.MLine(teachers_slots_detail, key='-ML1-', size=(40, 20)),
               sg.MLine(candidate_student_list, key='-ML2-', size=(60, 20))],

              [sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True)
    window.read()




