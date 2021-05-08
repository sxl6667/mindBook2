from rest_framework.serializers import ModelSerializer
from functools import wraps
from app01.models import User


regists = {}


def regist(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # try:
        #     res = func(*args, **kwargs)
        #     regists[res.Meta.model] = func
        # except:
        #     res = func(*args, **kwargs)
        #     return res
        # res = func(*args, **kwargs)
        # regists[res.Meta.model] = func
        return func(*args, **kwargs)
    return inner


# @regist
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


regists2 = {
    User: UserModelSerializer
}