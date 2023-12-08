def get_cube_count(cubes):
  cube = ''.join(cubes).split(' ')
  return cube[1], int(cube[0])


def find_minimum_set_round(round):
  round = round.strip()
  round = round.split(', ')
  dict = {
    "red": 0,
    "green": 0,
    "blue": 0
  }
  for _, cubes in enumerate(round):
    drawn = ''.join(cubes).split(',')
    color, count = get_cube_count(drawn)
    dict[color] = count
  return dict


def find_minimum_set_game(game):
  min_dict_game = {
    "red": 0,
    "blue": 0,
    "green": 0
  }
  for _, round in enumerate(game):
    min_dict_round = find_minimum_set_round(round)
    for color in min_dict_round:
      if min_dict_round[color] > min_dict_game[color]:
        min_dict_game[color] = min_dict_round[color]
  return min_dict_game

def parseLine(line):
  split = line.split(': ')
  game = ''.join(split[1]).split(';')
  min_dict = find_minimum_set_game(game)
  product = 1
  print(min_dict)
  for color in min_dict:
    product *= min_dict[color]
  return product

file = open("input.txt", "r")
sum = 0
for line in file:
  sum += parseLine(line)
print(sum)
file.close()
