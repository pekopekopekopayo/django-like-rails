from django.db import models
from lib.common.model_frame import ModelFrame

class Tag(ModelFrame):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "tags"
