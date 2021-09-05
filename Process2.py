import SelectSubject as S_subject
import MatchProcess as mp
import tomatchfile
import PySimpleGUI as sg
import RemoveMatched as rm

# Process2的说明：根据所选的科目，对该科目下的师生进行匹配
tomatch_subject = S_subject.select_subject()
var = 1
while var == 1:
    student_list = tomatchfile.open_student_candidatelist(tomatch_subject)
    teacher_list = tomatchfile.open_teacher_list(tomatch_subject)
    if len(student_list) == 0:
        sg.popup_no_frame('所选科目已无学生待匹配')
    elif len(teacher_list) == 0:
        sg.popup_no_frame('所选科目已无老师可匹配')
    else:
        mp.find_slots(tomatch_subject)
        rm.renew_student_candidate_list(tomatch_subject,student_list)
        rm.renew_teacher_candidate_list(tomatch_subject,teacher_list)






