no_of_stones = int(input())
stone_string = list(input())

# 'RRRGR'
no_of_stone_removed = 0

# 
# for ind in range(len(stone_string) - 2):
#     if stone_string[ind] == stone_string[ind + 1]:
#         del stone_string[ind]
#         no_of_stone_removed += 1
# print(no_of_stone_removed)
# # print(stone_string)
ind = 0
while ind < int(len(stone_string) - 1):
    if stone_string[ind] == stone_string[ind + 1]:
        del stone_string[ind]
        no_of_stone_removed += 1
        ind = 0
        # print(stone_string)
        # print(ind)
    else:
        ind += 1

print(no_of_stone_removed)
# print(stone_string)
