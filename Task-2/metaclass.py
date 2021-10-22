class CustomMeta(type):
    def __new__(metaclass, future_name,future_parents, future_attr):
        new_future_attr = dict((name, value)
                               if name.startswith("__") and name[-2:] == "__"
                               else ("custom_" + name, value)
                               for name, value in future_attr.items())
        new_future_attr["__setattr__"] = CustomMeta.setattr
        return super().__new__(metaclass, future_name,
                            future_parents, new_future_attr)

    def setattr(self, name, value):
        if name not in self.__dict__:
            name = "custom_" + name
        self.__dict__[name] = value
