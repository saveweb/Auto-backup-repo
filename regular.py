import os

with open('repos.csv', 'r') as f:
  file = f.read()
lines = file.splitlines()
lines = set(lines)
lines.discard('')
lines = list(lines)
lines.sort()

with open('repos.csv', 'w') as f:
  for line in lines:
    f.write(line.replace("https://", "").replace("/", ",")+'\n')