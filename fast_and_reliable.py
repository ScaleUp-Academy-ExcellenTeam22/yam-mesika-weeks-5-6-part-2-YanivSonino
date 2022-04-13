import time


# function to find the average time of finding word
# in the given data structure(in our case checks set and list)
def average_runtime_to_find_word(data_structure_to_check):
    time_to_check = 1000
    start_time = time.time()
    for i in range(time_to_check):
        found = 'zwitterion\n' in data_structure_to_check
    return (time.time() - start_time) / time_to_check


if __name__ == '__main__':
    file = open("words.txt", 'r')
    words_set = {word for word in file}
    file.seek(0, 0)
    words_list = [word for word in file]
    print(average_runtime_to_find_word(words_set))  # average time for set
    print(average_runtime_to_find_word(words_list))  # average time for list

