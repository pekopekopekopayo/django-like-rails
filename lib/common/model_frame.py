from django.db import models
from django.forms import ValidationError

from lib.errors.bad_request import UnprocessableEntity

class ModelFrame(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_clean(self):
        try:
            super().full_clean()
        except ValidationError as e:
            raise UnprocessableEntity(e.message_dict)
        
    class Meta:
        abstract = True