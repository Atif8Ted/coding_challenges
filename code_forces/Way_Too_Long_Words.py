no_of_words = int(input())

for i in range(no_of_words):
    word = input()
    if len(word) > 10:
        final_word = word[0] + str(len(word) - 2) + word[-1]
    else:
        final_word = word
    print(final_word)
