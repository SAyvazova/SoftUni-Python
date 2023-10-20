# nr_electrons = int(input())
# atom_shells = [number for number in range(1, 10)]
# electrons_per_shell = [int(2 * (nr_shell ** 2)) for nr_shell in atom_shells]
# final = []
# for electron_count in electrons_per_shell:
#     if nr_electrons - electron_count > 0:
#         final.append(electron_count)
#         nr_electrons -= electron_count
#     else:
#         final.append(nr_electrons)
#         nr_electrons -= nr_electrons
#         break
#
# print(final)

nr_electrons = int(input())
shells = []
for shell in range(1, nr_electrons):
    electron_count = 2 * (shell ** 2)
    if electron_count > nr_electrons:
        electron_count = nr_electrons
    nr_electrons -= electron_count
    shells.append(electron_count)

    if nr_electrons == 0:
        break

print(shells)