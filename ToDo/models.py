from django.db import models

# Create your models here.


class Task(models.Model):

    task_desc = models.CharField(max_length=25)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_desc
# __str__ tekstowa reprezentacja obieku tej klasy np w panelu admina

