import re 

s = input()
pattern = re.compile(r"([A-Za-z0-9])\1")
match = re.search(pattern , s)

if match:
    print(match.group(1))
else:
    print(-1)
    