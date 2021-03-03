string_1 = input()
string_2 = input()
final = None
for i in range(len(string_1)):
    if string_1[i].upper() > string_2[i].upper():
        final = 1
        break
    elif string_1[i].upper() < string_2[i].upper():
        final = -1
        break
if final is None:
    print(0)
else:
    print(final)