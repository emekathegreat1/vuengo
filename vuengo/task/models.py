from email.policy import default
from django.db import models

# Create your models here.
class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255, default= "new todo")
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default=TODO)




# In Django, Models are classes that deal with databases 
# in an object-oriented way. Each model class refers to a 
# database table and each attribute in the model class refers 
# to a database column.

