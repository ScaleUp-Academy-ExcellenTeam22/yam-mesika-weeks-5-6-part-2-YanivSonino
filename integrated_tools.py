# function to interleave all the items inside a data structures from the start to end with generator
def interleave(*data_structures_to_interweaving):
    index = 0
    maxi = len(max(data_structures_to_interweaving, key=len))
    while index < maxi:
        for data_structure in data_structures_to_interweaving:
            if index >= len(data_structure):
                continue
            yield data_structure[index]  # yield the first letter
        index += 1


# function to interleave all the items inside a data structures from the start to end
def interleave(*data_structures_to_interweaving):
    interleave_list = []
    index = 0
    maxi = len(max(data_structures_to_interweaving, key=len))  # gets the maximum len of data structure
    while index < maxi:
        for data_structure in data_structures_to_interweaving:
            if index >= len(data_structure):
                continue
            interleave_list.append(data_structure[index])
        index += 1
    return interleave_list


if __name__ == '__main__':
    interleave_list = []
    generator_leave = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for item in generator_leave:
        interleave_list.append(item)  # add letter to the list from the generator
    print(interleave_list)
