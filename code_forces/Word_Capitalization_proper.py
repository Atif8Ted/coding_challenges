# without using capitalize
ord_A = ord('A')
ord_Z = ord('Z')
ord_a = ord('a')
ord_z = ord('z')
input_string = list(input())
first_ord = ord(input_string[0])
first_word = input_string[0]
if not (ord_A <= first_ord <= ord_Z):
    first_word = chr(first_ord - 32)
rest_word = input_string[1:]
for ind, i in enumerate(rest_word):
    if not (ord_a <= ord(i) <= ord_z):
        i = chr(ord(i) + 32)
        rest_word[ind] = i
final_word = first_word + ''.join(rest_word)
print(final_word)

# with python inbuilt

# capitalized = input().capitalize()
