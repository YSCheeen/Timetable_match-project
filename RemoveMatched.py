import PySimpleGUI as sg
import tomatchfile

teacher_remove_list = []


def student_remove_input_window():
    justification = 'l'  # start left justified

    layout = [[sg.Text('输入已经匹配好的学生的ID，以半角逗号分割')],
              [sg.Text('注意：1.最后一个不加逗号；2.不要加任何空格。')],
              [sg.Multiline(size=(40, 10), key='-MLINE-', justification=justification, enable_events=True,
                            autoscroll=True)],
              # We'll be fancy and allow user to choose which justification to use in the demo
              [sg.Button('确认'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, keep_on_top=True, resizable=True, finalize=True)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # This is the important bit of code. It sets the current contents of the multiline to be the correct justification
        if event == '确认':
            return values['-MLINE-']  # 这个输入的值可以直接拿到，是一个字符串

    window.close()


def teacher_remove_input_window():
    justification = 'l'  # start left justified

    layout = [[sg.Text('输入已达匹配上限的老师姓名缩写，以半角逗号分割')],
              [sg.Text('注意：1.最后一个不加逗号；2.不要加任何空格。')],
              [sg.Multiline(size=(40, 10), key='-MLINE-', justification=justification, enable_events=True,
                            autoscroll=True)],
              # We'll be fancy and allow user to choose which justification to use in the demo
              [sg.Button('确认'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, keep_on_top=True, resizable=True, finalize=True)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # This is the important bit of code. It sets the current contents of the multiline to be the correct justification
        if event == '确认':
            return values['-MLINE-']  # 这个输入的值可以直接拿到，是一个字符串

    window.close()


def turn_into_list(item_to_remove):  # 将这个字符串转化为列表
    item_remove_list = []
    item_to_remove = item_to_remove.strip('\n')  # 字符串最后一定会有一个空格，去掉这个空格
    if item_to_remove == '':
        sg.popup_no_frame('没有输入任何内容')
    else:
        item_remove_list = item_to_remove.split(',')

    return item_remove_list


def renew_student_candidate_list(tomatch_subject, student_list):
    key = '#ID'
    matched_students_string = student_remove_input_window()
    toremove_students_list = turn_into_list(matched_students_string)
    if toremove_students_list == []:
        sg.popup('没有输入任何内容')
    else:
        renewed_student_list = tomatchfile.remove_matched(toremove_students_list, student_list, key)
        tomatchfile.renew_student_candidatelist(tomatch_subject, renewed_student_list)  # 更新学生列表的json文件

def renew_teacher_candidate_list(tomatch_subject, teacher_list):
    key = 'Initials'
    matched_teachers_string = teacher_remove_input_window()
    toremove_teachers_list = turn_into_list(matched_teachers_string)
    if not toremove_teachers_list:
        sg.popup('没有输入已匹配老师')
    else:
        renewed_teacher_list = tomatchfile.remove_matched(toremove_teachers_list, teacher_list, key)
        tomatchfile.renew_student_candidatelist(tomatch_subject, renewed_teacher_list)  # 更新老师列表的json文件