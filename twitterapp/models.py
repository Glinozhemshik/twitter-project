from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Twit(models.Model):
    user = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    re_twit = models.ManyToManyField(
        User,
        verbose_name="Ретвит",
        related_name="retwit")
    text = models.CharField(max_length=250)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text