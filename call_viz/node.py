"""node module"""

from typing import Any, Union

class BaseNode:
    """
        `Node` parent object class representing the function arguments
        and its childrens.
    """

    def __init__(self, parent: Union["BaseNode", None], *args: tuple, **kwargs: dict):
        self.args = args
        self.kwargs = kwargs
        self.parent = parent
        self.childrens = {}

        # Preventing Graphviz to ommit nodes
        # because of duplicate names
        self.name = str(hash(self))

class Node(BaseNode):
    """
        Class representing a Graphviz node
    """

    @property
    def value(self) -> Any:
        """
            Return the node value
        """

        return (*self.args, *self.kwargs.items(),)

    @property
    def label(self) -> str:
        """
            Return the node label
        """

        ret = list(map(str, self.args))

        for k, v in self.kwargs.items():
            assert hasattr(k, "__str__")
            assert hasattr(v, "__str__")

            s = f"{k}={v}"

            ret.append(s)

        return ", ".join(ret)

    def __str__(self) -> str:
        return "(" + self.name + ", " + self.label + ")"
