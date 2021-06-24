from django.db import models
import datetime


STATUS = [
    ("upcoming", "upcoming"),
    ("done", "done"),
    ("deleting", "deleting"),
    ("deleted", "deleted"),

]

class Channel(models.Model):
    title=models.CharField(max_length=1000)
    slack_id=models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class CountDown(models.Model):
    channel=models.ForeignKey(Channel, related_name='related_countdowns', on_delete=models.CASCADE)
    c_happening=models.CharField(max_length=1000)
    slack_timestamp=models.CharField(max_length=1000, default="not migrated yet")
    #c_description=models.TextField(max_length=20000)
    c_status=models.CharField(max_length=20, default="0", choices=STATUS)
    c_start = models.DateTimeField(null=True, blank=True)#, default = datetime.datetime.utcnow().isoformat())

    def __str__(self):
        return self.c_happening