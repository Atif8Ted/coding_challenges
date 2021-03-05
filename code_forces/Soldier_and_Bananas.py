# 1k +2k+3k+4k
# = k(1+2+3+4)


cost, total_dollar, no_of_banana = list(map(int, input().split()))
total_cost = cost * sum([i + 1 for i in range(no_of_banana)])
# print(total_cost)
amount_to_borrow = total_cost-total_dollar
if amount_to_borrow>0:
    print(amount_to_borrow)
else:
    print(0)
