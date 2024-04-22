def COMPARE(nut, bolt):
    """Returns 1, 0, -1 depending on the relative size of the bolt to the nut, i.e. bigger, equal or smaller."""
    if nut > bolt:
        return 1
    elif nut == bolt:
        return 0
    else:
        return -1


def SORT(nuts, bolts):
    """Sorts nuts and bolts according to their size."""
    pivot = nuts[0]
    left_nuts = []
    right_nuts = []
    for nut in nuts[1:]:
        if COMPARE(nut, pivot) == 1:
            left_nuts.append(nut)
        else:
            right_nuts.append(nut)

    left_bolts = []
    right_bolts = []
    for bolt in bolts:
        if COMPARE(pivot, bolt) == 1:
            left_bolts.append(bolt)
        else:
            right_bolts.append(bolt)

    SORT(left_nuts, left_bolts)
    SORT(right_nuts, right_bolts)

    return nuts, bolts




nuts = [4, 1, 3, 2, 5, 9, 12, 17, 14]
bolts = [1, 4, 2, 3, 12, 14, 17, 9, 5]

sorted_nuts, sorted_bolts = SORT(nuts, bolts)

print(sorted_nuts)  # [1, 2, 3, 4]
print(sorted_bolts)  # [1, 2, 3, 4]
