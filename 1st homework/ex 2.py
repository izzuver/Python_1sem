n = int(input())
v = n
s = ""

for i in range(2, n + 1):
    if i > n:
        break
    if n % i == 0:
        k = 0
        while n % i == 0:
            k += 1
            n /= i
        s += "(" + str(i) + "^" + str(k) + ")"
print(s)