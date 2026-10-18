def two_ukas(a, b):
    a_key = 0
    b_key = 0
    while a_key < len(a) and b_key < len(b):
        if a[a_key] == b[b_key]:
            return True
        if a[a_key] < b[b_key]:
            a_key += 1
        else:
            b_key += 1
    return False

def bin_serch(arr, element):
    l = 0
    r = len(arr) - 1
    while l <= r:
        c = (l+r)//2
        if arr[c] == element:
            return True
        if arr[c] < element:
            l = c+1
        else:
            r = c-1
    return False

def bin_serch_two_arr(a, b):
    # if len(a) > len(b):
    #     a, b = b, a
    for element in a:
        if bin_serch(b, element):
            return True
    return False

# решила сделать отдельную функцию для вставки (используется в экспотенциальном и двойном бинарном),
# а в основном бинарном оставить простую с выводом boll
def bin_serch_vstavka(arr, element, l=0, r=-1):
    if r == -1 or r >= len(arr):
        r = len(arr) - 1
    while l <= r:
        c = (l+r)//2
        if arr[c] == element:
            return c
        if arr[c] < element:
            l = c+1
        else:
            r = c-1
    return l

def exp_serch(arr, element, l):
    step = 1
    r = l
    while r < len(arr) and arr[r] <= element:
        l = r
        if arr[r] == element:
            return r
        step *= 2
        r += step

    #для поиска на оставшемся отрезке элемента или место вставки
    res = bin_serch_vstavka(arr, element, l, r)
    return res

def exp_serch_two_arr(a, b):
    # if len(a) > len(b):
    #     a, b = b, a
    a_key = 0
    b_key = 0
    while a_key < len(a) and b_key < len(b):
        res = exp_serch(b, a[a_key], b_key)
        if res < len(b):
            if b[res] == a[a_key]:
                return True
        b_key = res
        a_key += 1
    return False

def double_bin_search(a, b,la=0, ra=-1 , lb=0, rb=-1 ):
    if la > ra or lb > rb:
        return False

    ca = (la + ra) // 2
    pos = bin_serch_vstavka(b, a[ca], lb, rb)

    if pos < len(b) and b[pos] == a[ca]:
        return True

    return double_bin_search(a, b, ca + 1, ra, pos, rb) or double_bin_search(a, b, la, ca - 1, lb, pos)


def double_bin_search_two_arr(a, b):
    # if len(a) > len(b):
    #     a, b = b, a
    return double_bin_search(a, b, 0, len(a) - 1, 0, len(b) - 1)