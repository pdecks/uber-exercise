
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
# a = [3, 4, 1, 2, 4, 6]
# b = [1, 2, 3, 4, 5, 6]
# countGreaterNumbers(a, b)

def  maxStreak( s,  k):
    # find the highest start index where there are k-consecutive Ws
    # else find k-1 and 1 separated by 
    streaks = {}  # key = max streak, value equal starting index

    i = 0
    j = 0
    counts = 0
    start_index = j
    while i < len(s):
        if s[i] == 'W':
            if counts == 0:
                start_index = i
            counts += 1
            i += 1
        elif counts != 0:
            if streaks.get(counts, 0) == 0:
                streaks[counts] = [start_index]
            else:
                streaks[counts].append(start_index)
            counts = 0
        else:
            i += 1
    print streaks

    max_start_index = max(streaks[k]) + 1
    result = [max_start_index]
    for i in range(2,k):
        result.append(i)
    return result

string = 'WBBBWWBWWWWB'
maxStreak(string, 2)
