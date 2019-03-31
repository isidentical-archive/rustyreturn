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
