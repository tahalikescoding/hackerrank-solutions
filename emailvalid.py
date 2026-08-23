import re

pattern = re.compile(r"^[a-zA-Z][A-Za-z0-9-._]+@[A-Za-z]+[.][A-Za-z]{1,3}$")
result = []
n = int(input())
for _ in range(n):
    name , email = tuple(input().split())
    emailnew = email.lstrip("<")
    emailraw = emailnew.rstrip(">")
    if re.search(pattern , emailraw):
        result.append([name , email])

for valids in result:
    print(*valids)