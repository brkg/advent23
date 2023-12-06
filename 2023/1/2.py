spelling_map = {
  "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}
v_map = {
  "o": ["one"], "t": ["two", "three"], "f": ["four", "five"], "s": ["six", "seven"], "e": ["eight"], "n": ["nine"]
}


def valid_digit(line, start):
  letter = line[start]
  if letter.isdigit():
    return True, letter
  else:
    try:
      if v_map[letter]:
        for number in v_map[letter]:
          if line[start: start+len(number)] == number:
            return True, spelling_map[number]
    except:
      return False, letter
  return False, letter

def parseLine(line):
  sentinel = "-1"
  first = sentinel
  last = sentinel
  for i, _ in enumerate(line):
    valid, digit = valid_digit(line, i)
    if valid:
      if first != sentinel:
        last = digit
      else:
        first = digit
        last = digit
  if first == sentinel:
    first = "0"
    last = "0"
  return first + last

file = open("input.txt", "r")
nums = []
for line in file:
  nums.append(parseLine(line))

sum = 0
for num in nums:
  sum += int(num)
print(sum)
file.close()
