notes_list = []
note = input()
while note != 'End':
    notes_list.append(note)
    note = input()

sorted_notes = sorted(notes_list, key=lambda x: int(x.split('-')[0]))
final_list = [note.split('-')[1] for note in sorted_notes]
print(final_list)
