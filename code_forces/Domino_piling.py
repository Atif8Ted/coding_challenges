m, n = input().split()
size_of_dominoes = 2

box_size = int(m) * int(n)
total_no_of_pizzas = box_size // size_of_dominoes
print(total_no_of_pizzas)
