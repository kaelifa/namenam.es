import django.db.models
from django.contrib.auth.models import User, Group, UserManager

# Create your models here.

class SuggestedName(django.db.models.Model):
    name = django.db.models.TextField(max_length=255)
    user = django.db.models.ForeignKey(User)


class UserToUser(django.db.models.Model):
    user = django.db.models.ForeignKey(User)
    linked_user = django.db.models.ForeignKey(User, related_name='linked_user')