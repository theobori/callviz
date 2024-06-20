"""core module"""

from typing import Callable, Union, Any
from collections import defaultdict

from .tree import Tree

CALLVIZ_OUTPUT_DIR = "."

def set_output_dir(name: str):
    """Set the output directory

    Args:
        name (str): Output directory name
    """

    global CALLVIZ_OUTPUT_DIR

    CALLVIZ_OUTPUT_DIR = name

def callviz(
    filename: Union[str, None]=None,
    _format: str="svg",
    keep_dot_file: bool=False,
    memoization: bool=False,
    open_file: bool=False,
    show_link_value: bool=True,
    show_node_result: bool=False,

):
    """Python decorator that will generate a tree representing
        the function calls with the parameters.

    Args:
        filename (str, optional): Output filename. Defaults to "tree".
        format (str, optional): Output file format. Defaults to "png".
        keep_dot_file (bool, optional): Keep the DOT format file. Defaults to False.
        memoization (bool, optional): Enable memoization. Defaults to False.
        open_file (bool, optional): Open the built tree with the default image viewer. Defaults to False.
        show_link_value (bool, optional): Show every node link value. Defaults to True.
        show_node_result (bool, optional): Show every node result on the node. Defaults to True.

    Returns:
        decorator: Decorator function
    """

    tree = Tree()
    cache = {}
    count = defaultdict(int)

    def decorator(func: Callable) -> Callable:
        """Decorator

        Args:
            func (Callable): Function called in the returned function.

        Returns:
            Callable: Any object with the `__call__` method.
        """

        def inner(*args: tuple, **kwargs: dict) -> Any:
            """Decorator inner function.

            Returns:
                Any: The called function return value
            """

            value = None
            key = str((*args, kwargs,))

            if memoization and key in cache:
                value = cache[key]

            is_cached = not value is None

            tree.next(is_cached, *args, **kwargs)

            if is_cached:
                tree.set_return_value(value)
                tree.back()

                return value

            # Function return value
            value = func(*args, **kwargs)

            tree.set_return_value(value)

            if memoization:
                cache[key] = value

            tree.back()

            # End
            if tree.is_at_root:
                # Links every Graphviz node
                tree.process(show_node_result, show_link_value)

                key = filename or func.__name__
                c = count[key]

                if c > 0:
                    key += "_" + str(c)

                tree.render(
                    filename=key,
                    format=_format,
                    cleanup=not keep_dot_file,
                    view=open_file,
                    directory=CALLVIZ_OUTPUT_DIR
                )

                count[key] += 2 if c == 0 else 1

                # Reset tree for the next functions
                tree.reset()

                # Reset memoization cache
                cache.clear()

            return value
        return inner

    return decorator
