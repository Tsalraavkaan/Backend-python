class CustomList(list):

    def add(self, other):
        new_list = [0] * max(len(self), len(other))
        for i in range(len(new_list)):
            if i >= len(self):
                new_list[i] = other[i]
            elif i >= len(other):
                new_list[i] = self[i]
            else:
                new_list[i] = self[i] + other[i]
        return CustomList(new_list)

    def __add__(self, other):
        return CustomList.add(self, other)

    def __radd__(self, other):
        return CustomList.add(other, self)

    def __iadd__(self, other):
        self = CustomList.add(self, other)
        return self

    def sub(self, other):
        new_list = [0] * max(len(self), len(other))
        for i in range(len(new_list)):
            if i >= len(self):
                new_list[i] = -other[i]
            elif i >= len(other):
                new_list[i] = self[i]
            else:
                new_list[i] = self[i] - other[i]
        return CustomList(new_list)

    def __sub__(self, other):
        return CustomList.sub(self, other)

    def __rsub__(self, other):
        return CustomList.sub(other, self)

    def __isub__(self, other):
        self = CustomList.sub(self, other)
        return self

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
