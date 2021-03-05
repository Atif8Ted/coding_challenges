# without using capitalize
ord_A = ord('A')
ord_Z = ord('Z')
ord_a = ord('a')
ord_z = ord('z')
input_string = list(input())
first_ord = ord(input_string[0])

if not (ord_A <= first_ord <= ord_Z):
    first_word = chr(first_ord - 32)
else:
    first_word = input_string[0]
final_output = first_word + ''.join(input_string[1:])
print(final_output)
