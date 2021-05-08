from app01.models import User
from app01 import models
def test(Serializer):
    data = Serializer.Meta.model.objects.all()
    data = Serializer(instance=data, many=True)
    print(data.data)
    print(get_class(models))

import inspect
def get_class(arg):
    classes = []
    clsmember = inspect.getmembers(arg, inspect.isclass)
    print(clsmember)
    for (name, _) in clsmember:
        classes.append(name)
    return classes
