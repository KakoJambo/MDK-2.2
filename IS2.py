a = [0] * 25
a [0] = a [-1] = 1
print (a)

a = [0, 1]
print (a * 10)

a = []
for i in range(1, 100, 2):
	a.append(i)
print(a)	

a = []
b = int(input('Введите занчениме начала - '))
c = int(input('Введите значение интервала - '))
for i in range (b, 100, c):
	a.append(i)
print(a)

a = []
for i in range (0, 101, 2):
	a.append(i)
print(a)

a = []
for i in range (99, 0, -3):
	a.append(i)
print(a)

a = []
b = int(input('Размер фигни - '))
for i in range(1, b):
	a.append(i)
	if i % 1 == i and i % i == 0:
		print(i)
print(a)	

a = []
for i in range(1, 100):
	a.append(i**2)
print(a)

a = []
for i in range(1,100):
	a.append(i)
	if i % 2 == 0:
		print(1)
	elif i % 2 != 0:
		print(i / 5)
print(a)

a = []
for i in range(3, 100, 3):
	a.append(i)
	if i % 3 == 0 and i % 4 == 0:
		print(i)
	elif i % 3 == 0:
		print(3)
print(a)					
