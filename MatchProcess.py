import tomatchfile
import SelectTeacher as S_teacher
import DisplayResults as dr

def find_slots(tomatch_subject):
    teacher_A, teacher_B = S_teacher.select_teachers(tomatch_subject) #【有界面】根据选定科目选择两位老师指定为一组 / teacher_A 和 teacher_B都是字典
    student_candidatelist = tomatchfile.open_student_candidatelist(tomatch_subject) #打开所选学科的学生列表
    teacher_group_slots = tomatchfile.find_groupedteacher_slots(teacher_A, teacher_B) # 所选两位老师共同空闲段列表
    candidate_students = tomatchfile.find_match_slots(student_candidatelist, teacher_group_slots) # 将A、B老师的空闲时间段与每个学生匹配

    teacher_A_initial = teacher_A['Initials']
    teacher_B_initial = teacher_B['Initials']
    teacher_slots_no = len(teacher_group_slots)
    candidate_students_no = len(candidate_students)
    teacher_slots_detail = tomatchfile.display_selected_teacher_slots(teacher_group_slots) # 对展示格式进行了规定，稍微对眼睛友好一些
    candidate_students_detail = tomatchfile.display_candidate_student(candidate_students)

    dr.show_results(teacher_A_initial, teacher_B_initial, teacher_slots_no, candidate_students_no, teacher_slots_detail,
                 candidate_students_detail)



