str = "Harkirat"
for i in str:
    print(i, end=" ")

count = 0
print()

while count < 8:
    print(count, end = " ")
    count = count + 1
print()

num = 64
while num%2 == 0:
    print(num, end=" ")
    num = num//2
print()

odd = 11
for i in range (odd, 0, -1):
    if i % 2 == 0:
        continue 
    print(i, end=" ")
print()

