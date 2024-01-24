a = [75,150,145,200,600,15]
for i in range(len(a)):
    if a[i] > 500:
        break
    elif a[i] > 150:
        continue
    elif a[i] % 5 == 0:
        print(a[i])


x = str(input('nhap so: '))
dem = 0
for i in range(len(x)):
    dem += 1
print('Total digits are: ',dem)


list1 = [10,20,30,40,50]
j = len(list1) - 1
for i in range(len(list1)):
    print(list1[j])
    j -= 1