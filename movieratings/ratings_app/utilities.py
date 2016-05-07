# from .models import Rater
from django.contrib.auth.models import User
from django.db.models import Count
# import django

# django.setup()


def get_unassigned_user():
    regular_users = User.objects.filter(is_superuser=False)
    unassigned_user = regular_users.annotate(count=Count('rater_set')).get(count=0)
    return unassigned_user
