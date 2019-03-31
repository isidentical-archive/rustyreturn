import ast
import inspect
from types import FunctionType


class RLR(ast.NodeTransformer):
    """Auto returns last statement of each function definition if 
    its last statement is a returnable expression"""

    def visit_FunctionDef(self, fdef: ast.FunctionDef) -> ast.FunctionDef:
        if isinstance(fdef.body[-1], ast.Expr):
            fdef.body.append(ast.Return(value=fdef.body.pop().value))

        fdef.decorator_list = list(
            filter(lambda decorator: decorator.id != "rlr", fdef.decorator_list)
        )
        return fdef


def rlr(f: FunctionType) -> FunctionType:
    """Monkeypatchs given function with transforming its source via
    `RLR`."""
    tree = ast.parse(inspect.getsource(f))
    tree = RLR().visit(tree)
    ast.fix_missing_locations(tree)

    frame = inspect.currentframe()
    exec(compile(tree, "<ast>", "exec"), frame.f_globals, frame.f_locals)
    return frame.f_locals.get(f.__name__)
