from django.db import models


class Proffy(models.Model):
    fullName = models.CharField(max_length=250)
    whatsapp = models.CharField(max_length=250)
    email = models.CharField(max_length=250, blank = True)
    estado = models.CharField(max_length=250, blank = True)
    cidade = models.CharField(max_length=250, blank = True)
    bio = models.TextField()
    time_from = models.CharField(max_length=250, blank = True)
    cost = models.IntegerField("R$ ")
    subject = models.CharField(max_length=250)
    weekday = models.CharField(max_length=250)
    avatar = models.URLField(("url"), max_length=250)
    show = models.BooleanField('Ocultar Proffy', default=False)

    def __str__(self):
        return self.fullName