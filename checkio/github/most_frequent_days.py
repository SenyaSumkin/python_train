def most_frequent_days(a):

    from datetime import datetime, timedelta

    year_string = '0'*(4-len(str(a))) + str(a)

    answer_list = []
    day_dict = [["Monday", 0],
                ["Tuesday", 0],
                ["Wednesday", 0],
                ["Thursday", 0],
                ["Friday", 0],
                ["Saturday", 0],
                ["Sunday", 0]
                ]

    now_datetime = datetime.strptime(year_string, '%Y')
    while now_datetime.year == a:
        day_dict[now_datetime.weekday()][1] += 1
        now_datetime = now_datetime + timedelta(days=1)

    day_dict.sort(key=lambda x: x[1], reverse=True)
    max_days_count = day_dict[0][1]

    for days in day_dict:
        if days[1] == max_days_count:
            answer_list.append(days[0])

    return answer_list


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")

