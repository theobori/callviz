"""node module"""

from typing import Union, Dict

from .utility import try_get_copy

MEMOIZATION_ATTR = {
    "style": "filled",
    "fillcolor": "lightgrey",
}

class BaseNode:
    """`Node` parent object class representing the function arguments
        and its childrens."""

    def __init__(
        self,
        parent: Union["BaseNode", None],
        memoization: bool,
        *args: tuple,
        **kwargs: dict,
    ):
        """_summary_

        Args:
            parent (Union[BaseNode;, None]): Node parent or None
            memoization (bool): Tell if the node is memoized
        """

        # Arguments
        self.args = try_get_copy(args)
        self.kwargs = try_get_copy(kwargs)

        # Parent node
        self.parent = parent

        # Children nodes
        self.childrens = {}

        # Preventing Graphviz to ommit nodes
        # because of duplicate names
        self._name = str(hash(self))

        # Memoization
        self.memoization = memoization

        # Return value
        self.return_value = None

class Node(BaseNode):
    """Class representing a Graphviz node"""

    @property
    def name(self) -> str:
        """RNode name getter

        Returns:
            str: Node name
        """

        return self._name

    @property
    def value(self) -> tuple:
        """Node value getter

        Returns:
            tuple: Node value as a tuple
        """

        return (*self.args, *self.kwargs.items(),)

    def label(self, show_result: bool=False) -> str:
        """Node label getter

        Args:
            show_result (bool, optional): Add the node result. Defaults to False.

        Returns:
            str: Node label as a string
        """

        ret = list(map(str, self.args))

        for k, v in self.kwargs.items():
            assert hasattr(k, "__str__")
            assert hasattr(v, "__str__")

            s = f"{k}={v}"

            ret.append(s)

        ret = ", ".join(ret)

        if show_result:
            ret += f"\n({self.return_value})"

        return ret

    @property
    def attrs(self) -> Dict[str, str]:
        """Return Graphviz attributes

        Returns:
            Dict[str, str]: attributes
        """

        if not self.memoization:
            return {}

        return MEMOIZATION_ATTR

    def __str__(self) -> str:
        """Return `Node` as a string

        Returns:
            str: Node as a string
        """

        return "(" + self.name + ", " + self.label + ")"
