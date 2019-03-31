# Rusty Return
Return the last statement of function if it is a expression. Depends on `ast.NodeTransformer` and `inspect.getsource`.
## Example
```py
@rlr
def add(x, y):
    x + y
    
assert add(2, 3) == 5
```
