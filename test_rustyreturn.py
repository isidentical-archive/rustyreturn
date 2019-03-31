from rustyreturn import rlr


@rlr
def test(x, y):
    1 + 2
    x - y
    x + y


@rlr
def not_to_return(x, y):
    x + y
    a = x + y


assert test(2, 3) == 5
assert not_to_return(1, 2) is None


@rlr
def gt(x, y):
    if x > y:
        True
    elif x == y:
        4
    elif x + 1 == y:
        if x > y:
            True
        else:
            if True:
                33
            else:
                False
    else:
        False


assert gt(10, 2) is True
assert gt(2, 10) is False
assert gt(2, 2) == 4
assert gt(2, 3) == 33
