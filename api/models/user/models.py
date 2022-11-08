import pdb
import bcrypt

from django.db import models
from lib.common.model_frame import ModelFrame

# Create your models here.

class User(ModelFrame):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def to_hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        self.password = self.password.decode('utf-8')
    
    def valid_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
        
    class Meta:
        db_table = "users"