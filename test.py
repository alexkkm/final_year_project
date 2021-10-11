# Python program to remove all special characters from list

# take list
my_list = ['@know*', 'pr#ogra!m^', '(py_th@on_3}']

# initializing special characters
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
english_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_char = special_char+english_char

# using filter() to remove special characters
out_list = [''.join(filter(lambda i: i not in all_char, string))
            for string in my_list]

# print list without special characters
print('List after removal of special characters:', out_list)
