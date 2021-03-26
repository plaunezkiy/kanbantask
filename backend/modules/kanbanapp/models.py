from django.db import models
from django.contrib.auth import get_user_model

STATES = (
    (1, 'ON HOLD'),
    (2, 'IN PROGRESS'),
    (3, 'NEEDS REVIEW'),
    (4, 'APPROVED'),
)


class Card(models.Model):
    header = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATES)
    position = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey(get_user_model(), related_name='cards', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position',]

    def __str__(self):
        return self.header

