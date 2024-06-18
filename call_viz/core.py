"""core module"""

from typing import Callable, Union

from .tree import Tree

def call_viz(
    filename: Union[str, None]=None,
    _format: str="svg",
    keep_dot_file: bool=False,
):
    """Python decorator that will generate a tree representing
        the function calls with the parameters.

    Args:
        filename (str, optional): Output filename. Defaults to "tree".
        format (str, optional): Output file format. Defaults to "png".
        keep_dot_file (bool, optional): Keep the DOT format file. Defaults to False.

    Returns:
        decorator: Decorator function
    """

    tree = Tree()

    def decorator(func: Callable) -> Callable:
        def inner(*args: tuple, **kwargs: dict):
            tree.next(*args, **kwargs)

            value = func(*args, **kwargs)

            tree.back()

            if tree.is_at_root:
                tree.process()

                # render show etc
                tree.render(
                    filename=filename or func.__name__,
                    format=_format,
                    cleanup=not keep_dot_file,
                )

                # Reset tree for the next functions
                tree.reset()

            return value
        return inner

    return decorator
