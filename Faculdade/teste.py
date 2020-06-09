x = {}
x['Valor'] = [123,'casa']

y = float(input())

for c,v in x.items():
    if 'Valor' in c:
        v[0] += y
print(x)

