import re 

s = input()

pattern = re.compile(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])")

matches = re.findall(pattern , s) 

if matches:
    print(*matches , sep = "\n")
else:
    print(-1)



