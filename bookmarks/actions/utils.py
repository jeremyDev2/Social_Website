from django.contrib.contenttypes.models import ContentType
from .models import Action
from django.contrib.admin import action
from django.utils import timezone
import datetime

#create actions that optionally include a target object
def create_action(user, verb, target=None):
    action = Action(user=user, verb=verb, target=target)
    action.save()
