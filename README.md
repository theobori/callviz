# Function call visualization

[![lint](https://github.com/theobori/callviz/actions/workflows/lint.yml/badge.svg)](https://github.com/theobori/callviz/actions/workflows/lint.yml) [![build](https://github.com/theobori/callviz/actions/workflows/build.yml/badge.svg)](https://github.com/theobori/callviz/actions/workflows/build.yml) [![publish](https://github.com/theobori/callviz/actions/workflows/publish.yml/badge.svg)](https://github.com/theobori/callviz/actions/workflows/publish.yml)

[![built with nix](https://builtwithnix.org/badge.svg)](https://builtwithnix.org)

It is a Python decorator that will help you visualizate the function calls, in particular for the recursive ones. Under the hood [Graphviz](https://graphviz.org/) is used to generate the graph.

## 📖 Build and run

For the build, you only need the following requirements:

- [Python](https://www.python.org/downloads/) 3+ (tested with 3.12.4)

To install it from [PyPi](https://pypi.org), you can run the following command:

```bash
python -m pip install callviz
```

## 🤝 Contribute

If you want to help the project, you can follow the guidelines in [CONTRIBUTING.md](./CONTRIBUTING.md).

## 📎 Some examples

Here is an example of how you could use the decorator.

```py
from callviz import callviz

@callviz(_format="png", memoization=True, open_file=True)
def fib(n: int):
    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)

@callviz(show_link_value=False)
def rev(arr, new):
    if arr == []:
        return new

    return rev(arr[1:], [arr[0]] + new)

fib(7)
rev(list(range(6, 0, -1)), [])
```
