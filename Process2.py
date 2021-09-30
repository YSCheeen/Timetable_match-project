import SelectSubject as S_subject
import MatchProcess as mp
import tomatchfile
import PySimpleGUI as sg
import RemoveMatched as rm

# 这一行：将老师和学生按照专业分组（只有第一次需要运行，之后请通过添加#把它注释掉/删去#这一行即可运行）
#tomatchfile.groupby_subject()


# Process2的说明：根据所选的科目，对该科目下的师生进行匹配
tomatch_subject = S_subject.select_subject()
# 一次匹配-删去已匹配人员完成后，再点击三角形 ▶ 运行即可
student_list = tomatchfile.open_student_candidatelist(tomatch_subject)
teacher_list = tomatchfile.load_teacher_list(tomatch_subject)
if len(student_list) == 0:
    sg.popup_no_frame('所选科目已无学生待匹配，程序结束。')
elif len(teacher_list) == 0:
    sg.popup_no_frame('所选科目已无老师可匹配，程序结束。')
else:
    mp.find_slots(tomatch_subject)
    rm.renew_student_candidate_list(tomatch_subject, student_list)
    rm.renew_teacher_candidate_list(tomatch_subject, teacher_list)






