import math

otrezok = list(range(174457, 174506))

for i in otrezok:
    delitels = []
    for delitel in range(2, int(math.sqrt(i))):
        if i % delitel == 0:
            delitels.append(delitel)
        if len(delitels) > 2:
            break       # чтобы не считать лишние
    if len(delitels) == 2:
        print(f'Делители {i}: {delitels[0]}, {delitels[1]}')
