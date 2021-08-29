import SelectSubject as S_subject
import MatchProcess as mp
import tomatchfile

# Process2的说明：根据所选的科目，对该科目下的师生进行匹配

var = 1
while var == 1:
    tomatch_subject = S_subject.select_subject()
    if tomatch_subject == '':
        break
    else:
        mp.find_slots(tomatch_subject)




