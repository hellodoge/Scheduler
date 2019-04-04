from datetime import date

week = 'Понедельник Вторник Среда Четверг Пятница Суббота Воскесенье'.split()


def save(location,class_list,teacher_list):
    for tmp in class_list:
        save_schedule(location+f'/ученики {str(date.today())}.txt', tmp.get_name(), tmp.get_schedule())
    for tmp in teacher_list:
        save_schedule(location+f'/учителя {str(date.today())}.txt', tmp.get_name(), tmp.get_schedule(), True)


def save_schedule(location, name, schedule, mode=False):
    file = open(location,'a')
    file.write(name+'\n')
    for num, tmp in enumerate(schedule):
        file.write('    ' + week[num] + '\n')
        for num2, tmp2 in enumerate(tmp):
            if not mode:
                if tmp2 is None: continue
                file.write('    '*2+str(num2+1)+'. ' + tmp2.get_lesson().get_name()+'\n')
            else:
                if not tmp2: continue
                file.write('    '*2+str(num2+1)+'. '+tmp2[1].get_name()+' '+tmp2[0].get_name()+'\n')
