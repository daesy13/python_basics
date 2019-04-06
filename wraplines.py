#input
# 13
# abc
# xyz
# foobar
# cuckoo
# seven
# hello

# expected
# abc xyz
# foobar cuckoo
# seven hello

import sys

# Prints to standard output.
def wrapLines(line_length, words):
    # IMPLEMENTATION GOES HERE
    curr_line = ""
    result = []
    for word in words:
        if len(curr_line) + len(word) + 1 >= line_length:
                result.append(curr_line)
                curr_line = ""
            else:
                curr_line += " " + word
    if curr_line:
        result.append(currline)
    return result

# DO NOT MODIFY BELOW THIS LINE
def main():
  first_line = None
  words = []

  first_arg = True
  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    if first_arg:
      lineLength = line
      first_arg = False
    else:
      words.append(line)

  wrapLines(lineLength, words)

main()