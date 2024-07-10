
size = int(input("Enter size: ")) + 2
center = size // 2 - (1 if size % 2 == 0 else 0)

for row in range(size - 1):

    rowPattern = ''

    for col in range(size):
        if ((row == col) or (row + col == size - 1)): 
            rowPattern += ' '
        elif ((col == center) and (row > center)): 
            rowPattern += 'x'
        else: 
            rowPattern += '*'

    if ((row > center) and ('x' in rowPattern)):
        start = rowPattern.find(' ')
        end = rowPattern.rfind(' ')
        rowPattern = rowPattern[: start + 1] + rowPattern[start + 1: end].replace('*', ' ') + rowPattern[end: ]

    print(rowPattern)
