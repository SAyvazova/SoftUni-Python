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
