data = []
for i in range(1, 4):
    fname = f'{i}.txt'
    with open(f'sorted/{fname}') as fp:
        data.append([fname, fp.readlines()])

data = sorted(data, key=lambda x: len(x[1]))

with open('result.txt', 'w') as fp:
    for fname,  lines in data:
        fp.write(f'{fname}\n')
        fp.write(f'{len(lines)}\n')
        for line in lines:
            fp.write(f'{line}')
        # fp.write('\n')
