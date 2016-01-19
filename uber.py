
def countGreaterNumbers(a,  b):
    # create sorted array C (sorted A) and generate counts dictionary
    c = sorted(a)  #O(nlogn)

    counts = {}
    i = 0
    curr_key = c[i]
    # curr_count = 1

    if len(c) == 1:
        counts[curr_key] = 1

    while i + 1 < len(c):
        # import pdb; pdb.set_trace()
        if c[i + 1] == c[i]:
            # curr_count += 1
            pass
        else:
            # counts[curr_key] = curr_count
            counts[curr_key] = len(c) - i - 1
            curr_key = c[i + 1]
            # curr_count = 1
        i += 1
    
    # final entry
    # counts[curr_key] = curr_count
    counts[curr_key] = 0
    
    print counts
    # Walk through B, calling dictionary for Bi-th element of A
     
    greater_than = []
    for j, item in enumerate(b):
        curr_index = item - 1 # 0 - len(a)
        if curr_index > len(a):
            raise IndexError('Index of b-ith element exceeds length of a')
        else:
            # print counts[a[curr_index]]
            greater_than.append(counts[a[curr_index]])
    print "greater_than", greater_than
    return greater_than


# a = [4, 5, 5, 2, 3, 7, 8, 1, 1, 1]
a = [3, 4, 1, 2, 4, 6]
b = [1, 2, 3, 4, 5, 6]

countGreaterNumbers(a, b)