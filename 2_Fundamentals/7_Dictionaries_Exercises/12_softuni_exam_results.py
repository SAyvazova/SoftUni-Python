exam_results = {}
total_submissions = {}
command = input()

while command != "exam finished":
    if "banned" in command:
        command_parts = command.split("-")
        username = command_parts[0]
        del exam_results[username]

    else:
        username, language, points = command.split("-")
        points = int(points)
        if username not in exam_results:
            exam_results[username] = {}
        if language not in exam_results[username]:
            exam_results[username][language] = 0
        if points > exam_results[username][language]:
            exam_results[username][language] = points
        if language not in total_submissions:
            total_submissions[language] = 0
        total_submissions[language] += 1

    command = input()

print("Results:")
for user, result in exam_results.items():
    for points in result.values():
        print(f"{user} | {points}")

print("Submissions:")
for language, submissions_count in total_submissions.items():
    print(f"{language} - {submissions_count}")
