"""node module"""

from typing import Union, Dict

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
        """Constructor

        Args:
            parent (Union[BaseNode, None]): Node parent or None
        """

        # Arguments
        self.args = args
        self.kwargs = kwargs

        # Parent node
        self.parent = parent

        # Children nodes
        self.childrens = {}

        # Preventing Graphviz to ommit nodes
        # because of duplicate names
        self._name = str(hash(self))

        # Memoization
        self.memoization = memoization

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
            Any: Node value as a tuple
        """

        return (*self.args, *self.kwargs.items(),)

    @property
    def label(self) -> str:
        """Node label getter

        Returns:
            str: Node label as a string
        """

        ret = list(map(str, self.args))

        for k, v in self.kwargs.items():
            assert hasattr(k, "__str__")
            assert hasattr(v, "__str__")

            s = f"{k}={v}"

            ret.append(s)

        return ", ".join(ret)

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
