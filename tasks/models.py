from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=100)
    description =   models.TextField(blank=True)
    due_date =  models.DateField(null = True, blank=True)
    is_completed =  models.BooleanField(default=False)
    
    def str(self):
        return self.title