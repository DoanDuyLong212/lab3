str1 = 'I am 25 years and 10 months old'
print(''.join(i for i in str1 if i.isdigit()))


str1 = "/* Jon is @developer & musician"
print(''.join(letter for letter in str1 if letter.isalnum()))


str_list = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
while('' in str_list):
    str_list.remove('')
while(None in str_list):
    str_list.remove(None)
print('Original list of string')
print(str_list)
print('After removing empty string')
print(str_list)


str_1 = 'Emma-is-a-data-scientist'
print(str_1.replace('-', '\n' ))