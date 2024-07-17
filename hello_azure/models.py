from django.db import models

# Create your models here.

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField(default=20)
    field3 = models.IntegerField(default=200)
    # Add more fields as needed

def __str__(self):
        return f"{self.field1}({self.field2}・{self.field3})"
