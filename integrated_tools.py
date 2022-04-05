def interleave(*integrated):
    i = 0
    maxi = len(max(integrated, key=len))
    while i < maxi:
        for item in integrated:
            if i >= len(item):
                continue
            yield item[i]  # yield the first letter
        i += 1

# interLeave without generator
# def interleave(*integrated):
#     lst = []
#     i = 0
#     maxi = len(max(integrated, key=len))
#     while i < maxi:
#         for item in integrated:
#             if i >= len(item):
#                 continue
#             lst.append(item[i])
#         i += 1
#     return lst
#


inter_leave_list = []
generator_leave = interleave('abc', [1, 2, 3], ('!', '@', '#'))
for item in generator_leave:
    inter_leave_list.append(item)
print(inter_leave_list)
