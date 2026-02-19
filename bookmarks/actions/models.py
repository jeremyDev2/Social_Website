from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models

class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='actions', on_delete=models.CASCADE)
    
    #action that the user has performed
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    #ForeignKey field that points to the ContentType model
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    #PositiveIntegerField for storing the primary key of the related object
    target_id = models.PositiveIntegerField(null=True, blank=True)
    #GenericForeignKey field to the related object based on the combination of the two previous fields
    target = GenericForeignKey('target_ct', 'target_id')
    class Meta:
        indexes = [models.Index(fields=['-created']), models.Index(fields=['target_ct', 'target_id']),]
        ordering = ['-created']

