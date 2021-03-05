try:
    final_list = []
    for i in range(5):
        final_list.append(list(map(int, input().split())))

    x, y = len(final_list)//2, len(final_list[0])//2
    for i in range(len(final_list)):
        for j in range(len(final_list)):
            if final_list[i][j] == 1:
                x_, y_ = i, j
                break
    total_moves = abs(x - x_) + abs(y - y_)
    print(total_moves)
except Exception as e:
    print(e)