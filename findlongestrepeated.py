# Given a list of strings comprising capital letters, find (for each string) the longest consecutive substring containing a single repeated letter, and print out the letter along with the number of times it repeats itself in that substring. If there is a tie, choose the letter that comes earliest in the alphabet.

# Example input
#   AAABBBBAABBBCCCCCCCDDAAAAAAAAAADEFGCC
#   BBBA
#   RUNDMC
#   DDADDDADDDDA
#   ABBA
#   ZZTOP
#   MISSISSIPPI
# Example output
#   A 10
#   B 3
#   C 1
#   D 4
#   B 2
#   Z 2
#   P 2
# Clarifications
# Strings contain letters only (no symbols, numbers, or white space).
# Your function should be case-sensitive. Capital and lowercase letters are treated as different letters.
# There will be no null or empty strings.
# There will always be at least one string in the input.

import sys

def findLongestRepeatedLetters(lines):
  # alphabet=['A','B','C','D','E','F','G','H',
  #           'I','J','K','L','M','N','O','P',
  #           'Q','R','S','T','U','V','W','X'
  #           'Y','Z']
  # for item.upper() in lines:
  #   new_value = list(item)
  #   count_score=0
  #   for i in new_value:
  #     if new_value.count(i) > count_score:
  #       count_score = new_value.count(i)
  #   print(i + count_score)
  for item in lines:
    item = item.upper()
    new_value = list(item)

    print("new value", new_value)
    temp_string = []
    count_score = 0

    for item in lines:
    item = item.upper()
    new_value = list(item)

    temp_string = []
    count_score = 0

    for i, j in enumerate(new_value[:-1]):
      if j  == new_value[i+1]:
        print(new_value[i], new_value[i+1])
        new_value[i] == new_value[i+1]
        temp_string.append(new_value[i])
        count_score = len(temp_string)+1

      else:
        temp_string.append(new_value[:-1])
        temp_string = new_value[-1]
        count_score = 1

      print(temp_string[0], count_score)


# DO NOT MODIFY BELOW THIS LINE
def main():
  lines = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()
    lines.append(line)

  findLongestRepeatedLetters(lines)

main()

sample_list = ["AAABBBBAABBBCCCCCCCDDAAAAAAAAAADEFGCC", "BBBA", "RUNDMC", "DDADDDADDDDA", "ABBA", "ZZTOP", "MISSISSIPPI"]
