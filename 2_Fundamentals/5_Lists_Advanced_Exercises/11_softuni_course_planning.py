initial_schedule = input().split(', ')
new_schedule = initial_schedule.copy()
exercise_list = []
command = input()
while command != "course start":
    command_parts = command.split(':')
    action = command_parts[0]
    lesson_title = command_parts[1]
    if action == 'Add':
        if lesson_title not in new_schedule:
            new_schedule.append(lesson_title)
    elif action == 'Insert':
        index_insert = int(command_parts[2])
        if lesson_title not in new_schedule:
            new_schedule.insert(index_insert, lesson_title)
    elif action == 'Remove':
        if lesson_title in new_schedule:
            new_schedule.remove(lesson_title)
            if f'{lesson_title}-Exercise' in new_schedule:
                new_schedule.remove(f'{lesson_title}-Exercise')
    elif action == 'Swap':
        lesson_title2 = command_parts[2]
        if lesson_title in new_schedule and lesson_title2 in new_schedule:
            index_lesson_title = new_schedule.index(lesson_title)
            index_lesson_title2 = new_schedule.index(lesson_title2)
            new_schedule[index_lesson_title], new_schedule[index_lesson_title2] = new_schedule[index_lesson_title2], \
                                                                                  new_schedule[index_lesson_title]
    elif action == 'Exercise':
        if lesson_title not in new_schedule:
            new_schedule.append(lesson_title)
        exercise_list.append(lesson_title)

    command = input()

for lesson_title in set(exercise_list):
    if lesson_title in new_schedule:
        index_lesson_title = new_schedule.index(lesson_title)
        new_schedule.insert(index_lesson_title + 1, f'{lesson_title}-Exercise')

for index, lesson in enumerate(new_schedule):
    print(f"{index + 1}.{lesson}")

