line1 = input().split()
line2 = input().split()
line3 = input().split()
winner = 0

if line1.count('1') == 3 or line2.count('1') == 3 or line3.count('1') == 3:
    winner = 1
elif line1.count('2') == 3 or line2.count('2') == 3 or line3.count('2') == 3:
    winner = 2
elif line1.index('1') == line2.index('1') == line3.index('1'):
    winner = 1
elif line1.index('2') == line2.index('2') == line3.index('2'):
    winner = 2
elif line1.index('1') == line2.index('1') - 1 and line1.index('1') == line3.index('1') - 2:
    winner = 1
elif line1.index('1') == line2.index('1') + 1 and line1.index('1') == line3.index('1') + 2:
    winner = 1
elif line1.index('2') == line2.index('2') - 1 and line1.index('2') == line3.index('2') - 2:
    winner = 2
elif line1.index('2') == line2.index('2') + 1 and line1.index('2') == line3.index('2') + 2:
    winner = 2


if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
