class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):

        if target == self.value:
            return True

        if target != self.value:

            if target < self.value:

                if self.left is not None:
                    return self.left.contains(target)
            else:
                if self.right is not None:
                    return self.right.contains(target)

        return False

    def get_max(self):
        max_value = self.value

        if self.value >= max_value:
            if self.value > max_value:
                max_value = self.value
                return self.get_max()

        if self.left is not None and self.left.value > max_value:
            return self.left.get_max()
        else:
            if self.right is not None:
                return self.right.get_max()

        return max_value

    def for_each(self, fn):

        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)
