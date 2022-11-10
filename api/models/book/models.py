import pdb
from django.db import models
from api.models.user.models import User
from lib.common.model_frame import ModelFrame
from lib.errors.not_found import NotFound

# Create your models here.

class Book(ModelFrame):
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    discribe = models.TextField(blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "books"
