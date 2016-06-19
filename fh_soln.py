# python3

def fibmod(n,m):
	l=[0,1]
	p=0
	i=2
	while i<m**2:
		l.append((l[i-1]+l[i-2])%m)
		if l[i-1]==0 and l[i]==1:
			p=+1
			break
		i+=1
	if p==0:
		pr = l[:-1]
	if p==1:
		pr=l[:-2]
	period = len(pr)
	r=n%period
	return pr[r]

input = input();
n, m = map(int, input.split())
print(fibmod(n, m))