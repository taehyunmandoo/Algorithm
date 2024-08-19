n = int(input("거슬러 줘야 할 돈을 입력해주세요: "))

count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
		count = count +	n // coin
		n = n % coin

print(count)