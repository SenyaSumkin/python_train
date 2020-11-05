from itertools import permutations

def checkio_first(words_set):

    for suffix in words_set:
        for word in words_set:
            if len(word) > len(suffix):
                if word.endswith(suffix):
                    return True

    return False


def checkio(words_set):

    for suffix, word in permutations(words_set, 2):
        if len(word) > len(suffix) and word.endswith(suffix):
            return True

    return False


if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")

