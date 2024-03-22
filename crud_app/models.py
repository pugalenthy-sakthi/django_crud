from typing import Any
from django.db import models


class Base(models.Model):

  id = models.AutoField(primary_key = True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class User(Base):
  
  name = models.CharField(max_length = 50)
  email = models.EmailField()
  password = models.TextField()