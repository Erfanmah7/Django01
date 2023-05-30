from django.db import models

class Todo(models.Model):
  Name = models.CharField(max_length=100)
  Text = models.TextField()
  DateTime = models.DateTimeField()

