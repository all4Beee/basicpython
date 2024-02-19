
number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jany', 'Wasan']
mixed = [10, 25.75, True, 'Samit']


print(number[1])
print(name[3])
print(mixed[2], mixed[3])
print(number)

print("สมาชืกทั้งหมดของ number ", len(number))

data = []

data.append(10)
data.append(15)
data.append(20)

print(data)

data[1] = 12

print(data)

for n in number:
    print(n)

sum = 0
for num in number:
    sum += num

print(sum)
