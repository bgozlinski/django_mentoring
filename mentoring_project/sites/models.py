from django.db import models


class Site(models.Model):
    site_name = models.CharField(max_length=100, help_text="Site name")
    url = models.URLField(max_length=100, help_text="Site URL")

    def __str__(self) -> str:
        return f"{self.site_name}"