import PySimpleGUI as sg
import readexcel
import sys



def open_student_file():
    if len(sys.argv) == 1:
        student_file = sg.popup_get_file('选择要打开的学生数据excel文件')
    else:
        student_file = sys.argv[1]

    if not student_file:
        sg.popup("NO FILE", "未选择文件")
        raise SystemExit("Cancelling: no filename supplied")
    else:
        sg.popup('选中的文件为', student_file)
        readexcel.read_student_excel(student_file)
        sg.popup('文件已生成')


def open_teacher_file():
    if len(sys.argv) == 1:
        teacher_file = sg.popup_get_file('选择要打开的老师数据excel文件')
    else:
        teacher_file = sys.argv[1]

    if not teacher_file:
        sg.popup("NO FILE", "未选择文件")
        raise SystemExit("Cancelling: no filename supplied")
    else:
        sg.popup('选中的文件为', teacher_file)
        readexcel.read_teacher_excel(teacher_file)
        sg.popup('文件已生成')
        readexcel.generate_subject_list(teacher_file)
        sg.popup('科目列表已生成')

