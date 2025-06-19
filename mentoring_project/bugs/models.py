from django.db import models
from django.contrib.auth.models import User

class Bug(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)

    def __str__(self):
        return f"Bug #{self.id}: {self.description[:20]}"

