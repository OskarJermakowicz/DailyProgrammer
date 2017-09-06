nbr = int(input('Enter a number:'))

nbrs = list(range(1,nbr*2,2))

i=1
while i < nbrs.__len__():
    k = nbrs[i]
    del nbrs[k - 1::k]
    i = i+1

if nbr in nbrs:
    print(nbr, ' is a lucky number')
else:
    j = 0
    while nbr > nbrs[j]:
        j = j+1
    print(nbrs[j-1], ' < ', nbr, ' < ', nbrs[j])