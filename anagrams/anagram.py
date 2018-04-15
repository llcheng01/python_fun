def anagrams(text):
    if len(text) == 0:
        return []

    if len(text) == 1:
        return [text]

    result = []

    #  assume len is 2 now
    for i in range(len(text)):
        pos = text[i]
        print('pos: ', pos)
        remain = text[:i] + text[i+1:]
        for a in anagrams(remain):
            print('recur ', a)
            result.append([pos] + a)

    return result


def toString(List):
    return ''.join(List)

def permute(arr, s, e):
    if e == s:
        print(toString(arr))
    else:
        for i in xrange(s, e+1):
            arr[s], arr[i] = arr[i], arr[s]
            permute(arr, s+1, e)
            arr[s], arr[i] = arr[i], arr[s] # barrcktrarrck

