class CustomList(list):
    def __add__(self, other):
        new_list = [0] * max(len(self), len(other))
        for i in range(len(new_list)):
            if i >= len(self):
                new_list[i] = other[i]
            elif i >= len(other):
                new_list[i] = self[i]
            else:
                new_list[i] = self[i] + other[i]
        return new_list

    def __radd__(self, other):
        new_list = [0] * max(len(self), len(other))
        for i in range(len(new_list)):
            if i >= len(self):
                new_list[i] = other[i]
            elif i >= len(other):
                new_list[i] = self[i]
            else:
                new_list[i] = self[i] + other[i]
        return new_list

    def __iadd__(self, other):
        for i in range(len(self)):
            if i < len(other):
                self[i] += other[i]
        i = len(self)
        while i < len(other):
            self.append(other[i])
            i += 1
        return self

    def __sub__(self, other):
        new_list = [0] * max(len(self), len(other))
        for i in range(len(new_list)):
            if i >= len(self):
                new_list[i] = -other[i]
            elif i >= len(other):
                new_list[i] = self[i]
            else:
                new_list[i] = self[i] - other[i]
        return new_list

    def __rsub__(self, other):
        new_list = [0] * max(len(self), len(other))
        for i in range(len(new_list)):
            if i >= len(self):
                new_list[i] = other[i]
            elif i >= len(other):
                new_list[i] = self[i]
            else:
                new_list[i] = self[i] - other[i]
        return new_list

    def __isub__(self, other):
        for i in range(len(self)):
            if i < len(other):
                self[i] -= other[i]
        i = len(self)
        while i < len(other):
            self.append(-other[i])
            i += 1
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
