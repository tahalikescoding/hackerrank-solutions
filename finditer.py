import re

s = input()
k = input()

pattern = rf"(?={k})"

m = re.finditer(pattern , s)
found = False

for match in m:
    print((match.start() , match.start() + len(k)-1))
    found = True

if not found:
    print((-1 , -1))




