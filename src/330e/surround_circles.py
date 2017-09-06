input = input().split('\n')
#input = "1,1,2\n2,2,0.5\n-1,-3,2\n5,2,1".split('\n')

borders = [[] for x in range(4)]
for circle in input:
    vals = circle.split(',')
    borders[0].append(float(vals[0]) + float(vals[2]))
    borders[1].append(float(vals[0]) - float(vals[2]))
    borders[2].append(float(vals[1]) + float(vals[2]))
    borders[3].append(float(vals[1]) - float(vals[2]))

print("(" + '{:.{prec}f}'.format(max(borders[0]), prec=3) + ", " + '{:.{prec}f}'.format(max(borders[2]), prec=3) + "), (" + '{:.{prec}f}'.format(max(borders[0]), prec=3) + ", " + '{:.{prec}f}'.format(min(borders[3]), prec=3) + "), (" + '{:.{prec}f}'.format(min(borders[1]), prec=3) + ", " + '{:.{prec}f}'.format(max(borders[2]), prec=3) + "), (" + '{:.{prec}f}'.format(min(borders[1]), prec=3) + ", " + '{:.{prec}f}'.format(min(borders[3]), prec=3) + ")")