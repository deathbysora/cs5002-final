from typing import Any, List, Tuple
from matplotlib import pyplot

# x = [1, 2, 3, 4]
# y = [1, 2, 3, 4]

# pyplot.scatter(y, x)
# pyplot.show()
# x2 = [4, 5, 6, 7]
# y2 = [10, 11, 12, 13]
# pyplot.scatter(x2, y2)
# pyplot.title = "Testing Scatter"
# pyplot.xlabel = "days"
# pyplot.ylabel = "amount"

# pyplot.bar(["primos", "hell"], [5, 10])
# pyplot.show()


def display(x: List[Any], y: List[Any]):
    pyplot.xlabel("Date")
    pyplot.ylabel("Delay (in minutes)")
    pyplot.xticks
    pyplot.scatter(x, y)
    pyplot.show()
