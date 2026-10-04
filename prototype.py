import math
import random

class assett():
    def __init__(self, name: str, category: str, position: tuple,) -> None:
        self._name = name
        self._category = category
        self._position = position
        assettNum = random.randint(0,100)
        assettID_format = "{}.{}"
        self._assetID = assettID_format.format(name, assettNum)

    def getX(self) -> int:
        return self._position[0]

    def getY(self) -> int:
        return self._position[1]


def computeDistance(object1: assett, object2: assett) -> float:
    xlargest = max(object1.getX(), object2.getX())
    xSmallest = min(object1.getX(), object2.getX())
    xDist = xlargest - xSmallest

    ylargest = max(object1.getY(), object2.getY())
    ySmallest = min(object1.getY(), object2.getY())
    yDist = ylargest - ySmallest

    return math.hypot(xDist, yDist)

test1 = assett("M2", "Weapon", (0,0))
test2 = assett("M2", "Weapon", (5,5))

print(computeDistance(test1, test2))

