# Function call visualization

[![lint](https://github.com/theobori/call-viz/actions/workflows/lint.yml/badge.svg)](https://github.com/theobori/call-viz/actions/workflows/lint.yml) [![build](https://github.com/theobori/call-viz/actions/workflows/build.yml/badge.svg)](https://github.com/theobori/call-viz/actions/workflows/build.yml) [![publish](https://github.com/theobori/call_viz/actions/workflows/publish.yml/badge.svg)](https://github.com/theobori/call_viz/actions/workflows/publish.yml)

It is a Python decorator that will help you visualizate the function calls, in particular for the recursive ones. Under the hood [Graphviz](https://graphviz.org/) is used to generate the graph.

## 📖 Build and run

For the build, you only need the following requirements:

- [Python](https://www.python.org/downloads/) 3+ (tested with 3.12.4)

## 🤝 Contribute

If you want to help the project, you can follow the guidelines in [CONTRIBUTING.md](./CONTRIBUTING.md).

## 📎 Some examples

Here is an example of how you could use the decorator.

```py
from call_viz import call_viz

@call_viz(_format="png", memoization=True, view=True)
def fib(n: int):
    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)

@call_viz()
def rev(arr, new):
    if arr == []:
        return new

    return rev(arr[1:], [arr[0]] + new)

fib(7)
rev(list(range(6, 0, -1)), [])
```
