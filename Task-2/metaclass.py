class CustomMeta(type):
    def __new__(metaclass, future_class_name,
                future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items()
                 if not name.startswith('__'))
        new_attrs = dict(("custom_" + name, value) for name, value in attrs)
        for name, value in future_class_attr.items():
            if name.startswith('__'):
                new_attrs[name] = value
        new_attrs["__setattr__"] = CustomMeta.setattr
        return type.__new__(metaclass, future_class_name,
                            future_class_parents, new_attrs)

    def setattr(self, name, value):
        if name not in self.__dict__:
            name = "custom_" + name
        self.__dict__[name] = value
