#dictionaries
# dict.items 
# dict.keys 
# dict.values 
# dict.pop(keys)
# dict.popitem()
# dict.clear()

contacts = {
'Atish':{'email':'ati@gmmail.com', 'phone':'3456789032'},
'Bully':{'email': 'asaddti@gmmail.com', 'phone': '34569087989032'}

}
# print(contacts['Atish'])



words_count = {
'I': 1,
'LiKE': 5,
'This':  6
}
#  To add
# print(words_count)
words_count['Atish'] = 2

# to find

print(list(words_count.items()))
print(list(words_count.keys()))
print(list(words_count.values()))

# To delete #pop
words_count.pop('I')
# print(words_count)