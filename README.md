# Rusty Return
Return the last statement of function if it is a expression. Depends on `ast.NodeTransformer` and `inspect.getsource`.
## Example
```py
@rlr
def add(x, y):
    x + y
    
assert add(2, 3) == 5
```

```
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
