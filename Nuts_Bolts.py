def matchPairs(nuts, bolts):
    if len(nuts) != len(bolts):
        return None

    matches = {}  

    for nut in nuts:
        for bolt in bolts:
            if nut == bolt:
                matches[nut] = bolt

    return matches  


nuts = [4,3,5,2,1,6,7,8,9,11]
bolts = [5,6,8,9,7,1,11,3,2,4]

matched_pairs = matchPairs(nuts, bolts)

if matched_pairs:
    print("Matched nuts and bolts are :")
    for nut, bolt in matched_pairs.items():
        print(f"Nut: {nut}, Bolt: {bolt}")
else:
    print("Number of nuts and bolts do not match. Matching not possible.")