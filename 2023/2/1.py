def cube_possible(cubes):
  cube_count_map = {
    "red": 12,
    "green": 13,
    "blue": 14
  }
  cube = ''.join(cubes).split(' ')
  return int(cube[0]) <= cube_count_map[cube[1]]


def round_possible(round):
  round = round.strip()
  round = round.split(', ')
  for _, cubes in enumerate(round):
    drawn = ''.join(cubes).split(',')
    if not cube_possible(drawn):
      return False
  return True

def is_game_possible(game):
  for i, round in enumerate(game):
    if not round_possible(round):
      return False
  return True

def parseLine(line):
  split = line.split(': ')
  game_num = split[0]
  game = ''.join(split[1]).split(';')
  if is_game_possible(game):
    return int(''.join(game_num).split(' ')[1])
  return 0

file = open("input.txt", "r")
sum = 0
for line in file:
  sum += parseLine(line)
print(sum)
file.close()
