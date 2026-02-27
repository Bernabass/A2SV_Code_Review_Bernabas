I=input
for _ in[0]*int(I()):s=I();print(''.join(c for c
in sorted(set(s))if s.count(c)>2*s.count(c+c)))