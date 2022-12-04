# 1 X, 2 Y, 3 Z. 0 loss, 3 draw, 6 win
# A/X rock B/Y scissors C/Z paper

def score(line):
  round = line.split(' ')
  a = round[0]
  b = round[1].strip()

  if a == 'A':
    if b == 'Y':
      return 0
    elif b == 'Z':
      return 6
    else:
      return 3
  elif a == 'B':
    if b == 'X':
      return 6
    elif b == 'Z':
      return 0
    else:
      return 3
  elif a == 'C':
    if b == 'X':
      return 0
    elif b == 'Y':
      return 6
    else:
      return 3

file = open('test.txt', 'r')
scores = [score(x) for x in file]
file.close()

print(sum(scores))