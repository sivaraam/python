def cumulative_sum(int_list):
    length = len(int_list)
    res = [0] * length

    for i in range(length):
        for j in range(i, length):
            res[j] += int_list[i]

    return res

print cumulative_sum([1, 1, 1])
