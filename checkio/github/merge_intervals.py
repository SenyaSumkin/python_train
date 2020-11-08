def merge_intervals(intervals):

    if intervals == []:
        return []

    answer_list = []
    temp_interval = intervals[0]

    for i in range(1, len(intervals)):
        if intervals[i][0] > temp_interval[1] + 1:
            answer_list.append(temp_interval)
            temp_interval = intervals[i]
        else:
            if intervals[i][1] > temp_interval[1]:
                temp_interval = (temp_interval[0], intervals[i][1])
    answer_list.append(temp_interval)

    return answer_list


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')

