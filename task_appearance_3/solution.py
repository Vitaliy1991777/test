def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']
    
    # Создаем массивы для хранения времени входа и выхода
    timeline = []
    
    # Добавляем события для ученика
    for i in range(0, len(pupil_intervals), 2):
        start = max(pupil_intervals[i], lesson_start)
        end = min(pupil_intervals[i+1], lesson_end)
        if start < end:
            timeline.append((start, 1))
            timeline.append((end, -1))
    
    # Добавляем события для учителя
    for j in range(0, len(tutor_intervals), 2):
        start = max(tutor_intervals[j], lesson_start)
        end = min(tutor_intervals[j+1], lesson_end)
        if start < end:
            timeline.append((start, 2))
            timeline.append((end, -2))
    
    # Сортируем события
    timeline.sort()
    
    total_time = 0
    pupil_present = 0
    tutor_present = 0
    last_time = None
    
    for time, event in timeline:
        # Если есть пересечение присутствия
        if pupil_present > 0 and tutor_present > 0 and last_time is not None:
            total_time += time - last_time
        
        # Обновляем счетчики присутствия
        if event > 0:
            if event == 1:
                pupil_present += 1
            else:
                tutor_present += 1
        else:
            if event == -1:
                pupil_present -= 1
            else:
                tutor_present -= 1
        
        last_time = time
    
    return total_time