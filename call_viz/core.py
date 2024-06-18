"""core module"""

from typing import Callable

from .tree import Tree

def call_viz(
    filename: str="tree",
    format: str="png",
    keep_dot_file: bool=False,
):
    """
        Python decorator that will generate a tree representing
        the function calls with the parameters.
    """

    tree = Tree()

    def decorator(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            tree.next(*args, **kwargs)

            value = func(*args, **kwargs)

            tree.back()

            if tree.is_at_root:
                tree.process()

                # render show etc
                tree.render(
                    filename=filename,
                    format=format,
                    cleanup=not keep_dot_file,
                )

                # Reset tree for the next functions
                tree.reset()

            return value
        return inner

    return decorator
