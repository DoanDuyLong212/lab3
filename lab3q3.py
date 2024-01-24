a = input('Original string is: ')
vi_tri_giua = int(len(a)/2)
print('Middle four chars are: ',a[(vi_tri_giua - 2) : (vi_tri_giua + 2)])


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
        
        