def size(txt):
    tmp = []
    for x in txt:
        tmp.append(x)

    return len(tmp)

def get_left(txt,my_mid) -> str:
    tmp = []
    for x in txt:
        tmp.append(x)
    return tmp[:my_mid]

def get_mid(txt,my_mid) -> str:
    tmp = []
    for x in txt:
        tmp.append(x)
    return tmp[my_mid]

def get_right(txt,my_mid) -> str:
    tmp = []
    for x in txt:
        tmp.append(x)
    return tmp[(my_mid+1):]


def left(text, lf_buf, left) -> list:  # make json of this data
    text.insert(0, left[lf_buf])
    return text

def right(text, rt_buf, right) -> list:  # make json of this data
    text.insert(len(text), right[rt_buf])
    return text
