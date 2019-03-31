# Rusty Return
Return the last statement of function if it is a expression. Depends on `ast.NodeTransformer` and `inspect.getsource`.
## Example
```py
@rlr
def add(x, y):
    x + y
    
assert add(2, 3) == 5
```

```py
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
```

```py
@rlr
class Calculator:
    def add(self, x, y):
        x + y
    
    def sub(self, x, y):
        x - y
    
    def mul(self, x, y):
        result = 0
        for _ in range(y):
            result += x
        
        result

assert Calculator().add(2, 3) == 5
```
