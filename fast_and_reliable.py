import time


def average_runtime(structure):
    Time_to_check = 1000
    start_time = time.time()
    for i in range(Time_to_check):
        'zwitterion\n' in structure
    return (time.time() - start_time) / Time_to_check


file = open("words.txt", 'r')
words_list = []
words_set = set()
for word in file:
    words_list.append(word)
    words_set.add(word)

print(average_runtime(words_list))
print(average_runtime(words_set))
