from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()

    def __str__(self):
        return self.name
