def parseLine(line):
  first = "-1"
  last = "-1"
  for letter in line:
    if letter.isdigit():
      if first != "-1":
        last = letter
      else:
        first = letter
        last = letter
  if first == "-1":
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
