from .models import *


def act_start(user_id, username=None, first_name=None, last_name=None):
    checked = Users.objects.filter(user_id=user_id).exists()
    if checked:
        get = Users.objects.get(user_id=user_id)
        get.username = username
        get.first_name = first_name
        get.last_name = last_name
        get.step = 0
        get.save()
    else:
        Users.objects.create(user_id=user_id,
                             first_name=first_name,
                             username=username,
                             last_name=last_name)
