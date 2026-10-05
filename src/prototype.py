import math
import random

class asset():
    def __init__(self, name: str, category: str, position: tuple,) -> None:
        self._name = name
        self._category = category
        self._position = position


    def getX(self) -> int:
        return self._position[0]

    def getY(self) -> int:
        return self._position[1]


def computeDistance(object1: asset, object2: asset) -> float:
    xlargest = max(object1.getX(), object2.getX())
    xSmallest = min(object1.getX(), object2.getX())
    xDist = xlargest - xSmallest

    ylargest = max(object1.getY(), object2.getY())
    ySmallest = min(object1.getY(), object2.getY())
    yDist = ylargest - ySmallest

    return math.hypot(xDist, yDist)



