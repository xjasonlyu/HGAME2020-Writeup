
a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! '
b = 'ef2c601a54bd8739uvismghqlkrtonjpKLyICwxGBAHJEDzF! OYSMNWRQXZUTPV'

m = dict()
for i in range(len(a)):
    j = b.find(a[i])
    m[i] = j

c = 'pLaIjhg+{e5m$Umt!}Pnu3_imR0!ATeT'
t = [None]*len(c)

for i in range(len(c)):
    t[i] = c[m[i]]

print(''.join(t))
