class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        self.index = 0
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.flattened.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self) -> int:
        val = self.flattened[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)
