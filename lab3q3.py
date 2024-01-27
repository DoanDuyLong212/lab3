def middle_four_chars():
    while True:
        try:
            s = input("original string ")
            if len(s) < 5:
                raise ValueError("Error: The input string must have at least 5 characters.")
            mid_index = len(s) // 2
            middle_four_chars = s[mid_index - 2:mid_index + 2]
            print("The middle four characters of the input string are:", middle_four_chars)
            break
        except ValueError as e:
            print(e)

middle_four_chars()


s1 = 'Ault'
s2 = 'Kelly'
giua_s1 = int(len(s1)/2)
print(s1[:giua_s1] + s2 + s1[giua_s1:])


s1 = 'America'
s2 = 'Japan'
mid_s1 = int(len(s1)/2)
mid_s2 = int(len(s2)/2)
print(s1[0] + s2[0] + s1[mid_s1] + s2[mid_s2] + s1[len(s1)-1] + s2[int(len(s2))-1])


str1 = 'PyNaTive'
chu_cai_thuong = ''
chu_cai_hoa = ''
for i in range(len(str1)):
    if(str1[i] >= 'a' and str1[i] <= 'z'):
        chu_cai_thuong = chu_cai_thuong + str1[i]
    elif(str1[i] >= 'A' and str1[i] <= 'Z'):
        chu_cai_hoa = chu_cai_hoa + str1[i]
print(chu_cai_thuong + chu_cai_hoa)
        
        
