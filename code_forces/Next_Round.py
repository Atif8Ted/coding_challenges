n, k = input().split(' ')
n, k = int(n), int(k)

if k >= 1:

    score_list = sorted(list(map(int, input().split(' '))), reverse=True
                        )
    no_of_participants_advanced_to_next_round = len([i for i in score_list if 0 < i >= score_list[k - 1]])
    print(no_of_participants_advanced_to_next_round)

else:
    print(0)
