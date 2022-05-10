from django.db import models


class Jobs(models.Model):
    type = models.CharField(max_length=11)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    how_to_apply = models.TextField(max_length=300)

    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.type} - {self.url} - {self.title} - {self.description} - {self.how_to_apply}"
