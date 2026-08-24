
import collections
t = int(input())
for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))[:n]
    cubes = collections.deque(blocks)
    if cubes[0] >= cubes[-1]:
        top = cubes.popleft()
    if cubes[0]< cubes[-1]:
        top = cubes.pop()
    while cubes:
        choice = 0 
        if cubes[0]>=cubes[-1]:
            choice = cubes.popleft()
        else:
            choice = cubes.pop()
        if choice>top:
            print("NO")
            break
        top = choice 

if not cubes:
    print("Yes")