from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_name = models.CharField(max_length=200)
    manager_email = models.EmailField(unique=True)
    manager_hpass = models.CharField(max_length=200)

    def __str__(self):
        return self.manager_name + ', ' + self.manager_email