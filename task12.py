import math

count = 0
num = 300000000
while count <= 5:
    count += 1
    num += 1
    for i in range(2, math.sqrt(num)):
        