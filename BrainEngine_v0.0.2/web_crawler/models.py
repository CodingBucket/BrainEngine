from django.db import models

class Links(models.Model):
    page_id = models.IntegerField()
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.link
