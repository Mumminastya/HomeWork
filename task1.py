import numpy as np
for i in range(0, 10):
    r = np.random.randint(0, 37)
    if r == 0:
        print(f'zero {r}')
    elif r%2 == 0:
        print(f'black {r}')
    else:
        print(f'red {r}')