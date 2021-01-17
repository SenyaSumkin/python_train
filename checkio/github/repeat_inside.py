import re


def repeat_inside(line):
    """
        first the longest repeating substring
    """

    repeat_count = 0
    sub_string = ''
    answer = ''

    for i in range(len(line)-1):
        temp_line = line[i:]
        for sub_string_len in range(1, len(temp_line)//2+1):
            substring = temp_line[:sub_string_len]
            if temp_line.find(substring) == 0:
                count = find_subline_count_in_line(temp_line, substring)
                if count > repeat_count or (count == repeat_count and sub_string_len > len(sub_string)):
                    sub_string = substring
                    repeat_count = count
                else:
                    print(f'Подстрока {substring} повторяется {repeat_count} раз. '
                          f'В топе сейчас подстрока {sub_string} с количеством повторений {repeat_count}')

        print('\n')

    if repeat_count > 1:
        answer = repeat_count * sub_string

    return answer


def find_subline_count_in_line(temp_line, subline):

    count = 0
    temp_line_2 = temp_line
    for i in range(1, len(temp_line)//len(subline)+1):
        if temp_line_2.find(subline) == 0:
            count += 1
            temp_line_2 = temp_line_2[len(subline):]
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    assert repeat_inside("rghtyjdfrtdfdf56r") == 'dfdf', "Sixth"
    print('"Run" is good. How is "Check"?')

