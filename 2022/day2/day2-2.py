# 1 X, 2 Y, 3 Z. 0 loss, 3 draw, 6 win
# A/X rock B/Y paper C/Z scissors

resultScore = {
  'X': 0, #lose
  'Y': 3, #tie
  'Z': 6  #win
}

def score(line):
  round = line.split(' ')
  a = round[0]
  b = round[1].strip()

  def playingScore():
    if a == 'A':
      if b == 'Y':
        return 1
      elif b == 'Z':
        return 2
      else:
        return 3
    elif a == 'B':
      if b == 'X':
        return 1
      elif b == 'Z':
        return 3
      else:
        return 2
    elif a == 'C':
      if b == 'X':
        return 2
      elif b == 'Y':
        return 3
      else:
        return 1

  return resultScore[b] + playingScore()

file = open('input.txt', 'r')
scores = [score(x) for x in file]
file.close()

print(sum(scores))