n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
	# A의 원소가 B의 원소보다 작은경우
	if a[i] < b[i]:
		a[i], b[i] = b[i], a[i]
	else:
		break
	
print(sum(a))