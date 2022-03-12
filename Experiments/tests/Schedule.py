weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
work = [True, True, True, True, True, False, False]
plans = ["за покупками", "отдыхать", "играть", "лениться", "гулять", "кутить", "страдать"]

for i in range(len(weekdays)):
    day = weekdays[i]
    plan = plans[i]
    if work[i] == True:
        work_day = 'рабочий'
    elif work[i] == False:
        work_day = 'выходной'
    print(f'{day} — это {work_day} день, а вечером {plan}.')
#print(f'{day} — это {work_day} день, а вечером {plan}.')



