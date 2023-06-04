
import random
n = int(input("введите количество кустов: "))
b = list(random.randint(0, 10) 
for i in range(n))
result = []
i = 0
sum = 0
print(b)
while (i < n):
    if (i == n - 1):
        sum = b[i] + b[i - 1] + b[0]
    else:
        sum = b[i] + b[i - 1] + b[i + 1]
        result.append(sum)
        result.sort()
    i += 1
print(f"максимальное число ягод за один заход {result[-1]}")
