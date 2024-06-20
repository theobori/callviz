"""tree module"""

from typing import Any

import graphviz

from .node import Node
from .utility import try_get_copy

class BaseTree:
    """`Tree` parent object class"""

    def __init__(self):
        """Constructor"""

        self._root = Node(None, False)
        self.__current = self._root

    def reset(self):
        """Reset the `BaseTree` variables (essentially nodes)"""

        self.__init__()

    def __next(self, node: Node):
        """Add a children node if not exist,
            then change the current node to the new node

        Args:
            node (Node): Node
        """

        value = str(node.value)

        # set it as a children of the current node
        if value not in self.__current.childrens:
            self.__current.childrens[value] = node

        # replace the current
        self.__current = node

    def next(self, memoization: bool, *args: tuple, **kwargs: dict):
        """Same as `self._next` but with function arguments"""

        node = Node(self.__current, memoization, *args, **kwargs)

        self.__next(node)

    @property
    def is_at_root(self) -> bool:
        """Return if the current node is the root node

        Returns:
            bool: Is root
        """

        return self.__current == self._root

    def back(self) -> bool:
        """Update the current node with its parent if it exists

        Returns:
            bool: Has parent
        """

        if self.__current.parent is None:
            return False

        self.__current = self.__current.parent

        return True

    def set_return_value(self, value: Any):
        """Set the the return_value member of the current node

        Args:
            value (Any): Value
        """
        assert hasattr(value, "__str__")

        self.__current.return_value = try_get_copy(value)

    def _debug(self):
        """BFS used to display line by line"""

        line = [self._root]

        while line:
            size = len(line)

            display = []

            for i in range(size):
                childrens = line[i].childrens

                for _, children in childrens.items():
                    display.append(children)
                    line.append(children)

            line = line[size:]

            if display:
                print(", ".join(map(str, display)))

class Tree(graphviz.Graph, BaseTree):
    """Graphviz controller inheriting `BaseTree`

    Args:
        graphviz (graphviz.Graph): graphviz.Graph
        BaseTree (BaseTree): BaseTree
    """

    def __init__(self, _format="png"):
        super().__init__(format=_format)

    def process(self, show_node_result: bool, show_link_value: bool):
        """Link every node with Graphviz"""

        def dfs(node: Node):
            """Link every node with Graphviz

            Args:
                node (Node): Node
            """

            if node.parent is None:
                for children in node.childrens.values():
                    dfs(children)

                return

            # Parent
            self.node(
                node.name,
                node.label(show_node_result),
                **node.attrs,
            )

            # Childrens
            for children in node.childrens.values():
                self.node(
                    children.name,
                    children.label(show_node_result),
                    **children.attrs,
                )

                label = None

                if show_link_value:
                    label = str(children.return_value)

                self.edge(node.name, children.name, label=label)

                dfs(children)

        dfs(self._root)
