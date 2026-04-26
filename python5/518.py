import re

s = input()
pattern = input()

literal = re.escape(pattern)
matches = re.findall(literal, s)

print(len(matches))