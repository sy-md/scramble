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
