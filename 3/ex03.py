nFiles = 500
files = []

for i in range(nFiles):
    files.append(open('Katalog/plik%i.txt' % i, 'w'))

for i in range(nFiles):
    f = open('Katalog/plik%i.txt' % i, 'w')
    files.append(f)
    f.close()

for i in range(nFiles):
    with open('Katalog/plik%i.txt' % i, 'w') as f:
        files.append(f)