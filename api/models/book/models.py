from django.db import models
from api.models.user.models import User
from lib.common.model_frame import ModelFrame

# Create your models here.

class Book(ModelFrame):
    user_id = models.ForeignKey(User, related_name='books')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    class Meta:
        db_table = "books"