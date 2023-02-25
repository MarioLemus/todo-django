from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.TextField(null=True)
    isDone = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True)