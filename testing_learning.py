import SelectSubject
import SelectTeacher
import tomatchfile
import DisplayResults


tomatch_subject = SelectSubject.select_subject()
teacher_A_personal, teacher_B_personal = SelectTeacher.select_teachers(tomatch_subject)
teachers_slots_detail = tomatchfile.find_groupedteacher_slots(teacher_A_personal, teacher_B_personal)
t_slots_sequence = tomatchfile.display_selected_teacher_slots(teachers_slots_detail)
teacher_A = teacher_A_personal['Initials']
teacher_B = teacher_B_personal['Initials']
teachers_slots = len(teachers_slots_detail)

tomatch_student_list= tomatchfile.open_student_candidatelist(tomatch_subject)
candidate_student_list = tomatchfile.find_match_slots(tomatch_student_list,teachers_slots_detail)
candidate_student_list_sequence = tomatchfile.display_candidate_student(candidate_student_list)
candidate_students = len(candidate_student_list)

DisplayResults.show_results(teacher_A, teacher_B, teachers_slots, candidate_students, t_slots_sequence,
                 candidate_student_list_sequence)


