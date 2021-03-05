name = input()
dist_char_list = []

for char_ in name:
    if char_ not in dist_char_list:
        dist_char_list.append(char_)

if len(dist_char_list) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
