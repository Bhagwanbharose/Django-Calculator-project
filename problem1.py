name = input('Enter String :')
k = input('check frequncy of :')

def split1(name):
	return [c for c in name]

new = split1(name)
n = 0
for i in new:
	if i == k:
		n = n + 1
print('The frequncy of {} is :{}'.format(k,n))