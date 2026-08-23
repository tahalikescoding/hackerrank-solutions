'''
You are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
-+4.5

Number must contain at least 1 decimal value.
For example:
✖
 12.
✔
12.0  

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using float(N)

Input Format

The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N .


Sample Input 

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 

False
True
True
False
'''

import re

t = int(input())
nums = []
for _ in range(t):
    n = input()
    nums.append(n)

pattern = re.compile(r"^[+-]?\d*[.]{1}\d+$")

result = list(map(lambda x: True if re.search(pattern , x) else False , nums))
print(*result , sep = "\n")
