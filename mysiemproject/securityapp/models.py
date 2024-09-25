from django.db import models
from auditlog.registry import auditlog

class SensitiveModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.name

auditlog.register(SensitiveModel)
