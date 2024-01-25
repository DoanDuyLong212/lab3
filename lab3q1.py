for i in range(1,6):
    print(*range(1,i+1))
    
tong = 0
x = int(input('Enter number '))
for i in range(x+1):
    tong += i
print('Sum is ',tong)