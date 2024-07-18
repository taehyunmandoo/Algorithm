a, b = map(int, input().split())

if a % 2 != 0 and a % 3 != 0:
  print("Yes")
elif b % 2 != 0 and a % 3 != 0:
  print("Yes")
else:
  print("No")
  