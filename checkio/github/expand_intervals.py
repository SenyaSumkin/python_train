from typing import Iterable


def expand_intervals1(items: Iterable) -> Iterable:

    answer = []
    for pair in items:
        addition_number = pair[0]
        if pair[0] == pair[1]:
            answer.append(addition_number)
        else:
            for i in range(pair[1]-pair[0]+1):
                answer.append(addition_number)
                addition_number += 1
    return answer

def expand_intervals(items: Iterable) -> Iterable:
    return [num for upper, lower in items for num in range(upper, lower+1)]


if __name__ == '__main__':
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]
    print("Coding complete? Click 'Check' to earn cool rewards!")

