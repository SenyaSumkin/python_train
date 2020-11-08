from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:

    main_dictionary = {}
    final_costs_list = []
    for item in costs:
        key1, key2 = item[0]+item[1], item[1]+item[0]
        main_dictionary[key1] = item[2]
        main_dictionary[key2] = item[2]

    for i in range(len(costs)):
        main_dictionary = update_flight_dictionary(main_dictionary)
        print(main_dictionary)

    for key in main_dictionary:
        if key.startswith(a) and key.endswith(b):
            final_costs_list.append(main_dictionary[key])

    if len(final_costs_list) > 0:
        return min(final_costs_list)
    else:
        return 0

def update_flight_dictionary(flight_dictionaty):

    from itertools import permutations
    for key1, key2 in permutations(flight_dictionaty.keys(), 2):
        if key1.endswith(key2[0]) and len(key2)==2 and (key1[0] not in key2):
            flight_dictionaty[key1+key2[1:]] = flight_dictionaty[key1] + flight_dictionaty[key2]
    return flight_dictionaty


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]], 'A', 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")

