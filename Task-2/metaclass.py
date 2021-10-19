class CustomMeta(type):
    def __new__(metaclass, future_class_name, 
                future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict(("custom_" + name, value) for name, value in attrs)
        uppercase_attr.append("custom_" + attr.__name__, attr)
        return type.__new__(metaclass, future_class_name, 
                            future_class_parents, uppercase_attr)

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

inst = CustomClass()
inst.custom_x
inst.custom_line()
inst.custom_val

inst.x  # ошибка
inst.val  # ошибка
inst.line() # ошибка