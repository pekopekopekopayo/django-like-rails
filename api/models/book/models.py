import pdb
from django.db import models
from api.models.tag.models import Tag
from api.models.user.models import User
from lib.common.model_frame import ModelFrame

# Create your models here.

class Book(ModelFrame):
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    discribe = models.TextField(blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='books', db_table='books_tags')

    class Meta:
        db_table = "books"
