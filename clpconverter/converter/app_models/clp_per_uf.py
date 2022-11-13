from clpconverter.base_model import BaseModel
from django.db import models

class CLPPerUFModel(BaseModel):
    value = models.FloatField()
    date = models.DateField()

    class Meta:
        unique_together = ('value', 'date',)