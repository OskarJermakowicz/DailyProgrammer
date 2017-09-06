import numpy as np

def is_latin_square(mx, uniques):
    for row in mx:
        if set(row) != set(uniques):
            return False
    for i in range(uniques.__len__()):
        if set(mx[:,i]) != set(uniques):
            return False
    return True

l = int(input("Enter length of array"))
nbrs = [int(n) for n in input("Enter array content").split(' ')]

uniques = []
[uniques.append(i) for i in nbrs if not uniques.count(i)]
mx = np.array(nbrs).reshape((l, l))

print(is_latin_square(mx, uniques))