import numpy as np
total = 50
zc = 0
rc = 0
bc = 0
for i in range(0, total):
    r = np.random.randint(0, 37)
    if r == 0:
        zc += 1
    elif r%2 == 0:
        rc+=1
    else:
        bc+=1
print(total)
print(f'{zc + bc + rc}, {zc}, {bc}, {rc}')