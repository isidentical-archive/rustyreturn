import ast
import inspect
from types import FunctionType


class RLR(ast.NodeTransformer):
    """Auto returns last statement of each function definition if 
    its last statement is a returnable expression"""

    def _adjust(self, container: ast.AST, items: str = "body"):
        items = getattr(container, items) if items is not None else container
        last_stmt = items[-1]
        
        if isinstance(last_stmt, ast.Expr):
            items.append(ast.Return(value=items.pop().value))
        elif isinstance(last_stmt, ast.If):
            self._adjust(last_stmt)
            if len(last_stmt.orelse) > 0:
                self._adjust(last_stmt.orelse, None)
        else:
            return None
            
    def visit_FunctionDef(self, fdef: ast.FunctionDef) -> ast.FunctionDef:        
        self._adjust(fdef)
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
